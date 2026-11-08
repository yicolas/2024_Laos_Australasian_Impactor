"""
Reversible-jump MCMC source unmixing, following the formulation of Carter et al. (2025, G-cubed 26,
e2024GC011924; Berkeley Geochronology Center):

  forward model   Y = C . M          C [D x K] component compositions, M [K x N] per-analysis mixing weights
  priors          K ~ Poisson(lambda) truncated to 1..Kmax
                  component type ~ Uniform(dictionary); composition ~ independent truncated normals per oxide
                  (mean, sd, bounds per dictionary type), closed to 100 %
                  per-analysis weights ~ Dirichlet(alpha)   (implemented as normalised Gamma(alpha,1) variates)
  likelihood      Gaussian on centred-log-ratio (clr) transformed data and model, relative sigma per oxide
  sampler         Metropolis-Hastings; within-model moves: composition perturbation, weight perturbation,
                  component-type swap (new composition drawn from the new type's prior); between-model moves:
                  birth (new component drawn from the prior) and death. Step sizes adapted toward an acceptance of
                  0.234 during burn-in only. Multiple chains with independent random starts (K = 2..Kmax).
Differences from Carter et al.: no merge move (birth/death alone keeps the chain reversible); the relative
sigma is a per-oxide EPMA precision rather than a uniform 0.5 %.
"""
import numpy as np
from scipy.stats import truncnorm, poisson
from scipy.special import gammaln, betaln

class Dictionary:
    def __init__(self, names, mu, sd, lo, hi):
        self.names = list(names); self.mu = np.asarray(mu, float); self.sd = np.asarray(sd, float)
        self.lo = np.asarray(lo, float); self.hi = np.asarray(hi, float)
        a = (self.lo-self.mu)/self.sd; b = (self.hi-self.mu)/self.sd
        self.logZ = np.log(np.clip(_ncdf(b)-_ncdf(a),1e-300,None))
    @property
    def T(self): return len(self.names)
    def logprior(self, t, v):
        if np.any(v < self.lo[t]) or np.any(v > self.hi[t]): return -np.inf
        z = (v-self.mu[t])/self.sd[t]
        return float(np.sum(-0.5*z*z - np.log(self.sd[t]) - 0.5*np.log(2*np.pi) - self.logZ[t]))
    def draw(self, t, rng):
        a = (self.lo[t]-self.mu[t])/self.sd[t]; b = (self.hi[t]-self.mu[t])/self.sd[t]
        return truncnorm.rvs(a, b, loc=self.mu[t], scale=self.sd[t], random_state=rng)

def _ncdf(x):
    from scipy.special import ndtr
    return ndtr(x)

def clr(x):
    lx = np.log(x); return lx - lx.mean(axis=0, keepdims=True)

class RJMCMC:
    def __init__(self, data, sigma_rel, dic, lam=10, kmax=20, alpha=0.3, beta_birth=20.0, seed=0):
        self.D, self.N = data.shape                 # data: D x N, closed to 100
        self.clrd = clr(data); self.sig = np.asarray(sigma_rel)[:,None]
        self.dic = dic; self.lam = lam; self.kmax = kmax; self.alpha = alpha; self.beta = beta_birth
        self.rng = np.random.default_rng(seed)
        self.logpK = poisson.logpmf(np.arange(kmax+2), lam); self.logpK[0] = -np.inf; self.logpK[kmax+1:] = -np.inf
        # log-step for weights, step for compositions (per type x oxide, relative to sd)
        self.sw = 0.3; self.bt = 1.0; self.sc = np.full((dic.T, self.D), 0.5); self.n_acc = {}; self.n_try = {}

    # ---------- state helpers
    def init(self):
        K = int(self.rng.integers(2, self.kmax+1))   # Carter et al. start chains at K = 2-30
        self.types = list(self.rng.integers(0, self.dic.T, K))
        self.V = np.array([self.dic.draw(t, self.rng) for t in self.types])        # K x D
        self.U = self.rng.gamma(self.alpha, 1.0, (K, self.N))
        self.ll_n = self._ll_spots(self.V, self.U)
        self.lp_comp = np.array([self.dic.logprior(t, v) for t, v in zip(self.types, self.V)])

    def _model(self, V, U):
        C = (V/V.sum(1, keepdims=True)).T*100       # D x K
        W = U/U.sum(0, keepdims=True)                 # K x N
        return C @ W

    def _ll_spots(self, V, U):
        y = np.clip(self._model(V, U), 1e-6, None)
        r = (clr(y) - self.clrd)/self.sig
        return -0.5*np.sum(r*r, axis=0)               # per spot

    def _logprior_U(self, U):
        a = self.alpha
        return np.sum((a-1)*np.log(U) - U) - U.size*gammaln(a)   # Gamma(a,1) log-density

    def _acc(self, key, ok):
        self.n_try[key] = self.n_try.get(key, 0)+1; self.n_acc[key] = self.n_acc.get(key, 0)+int(ok)

    # ---------- moves
    def move_weights(self, adapt):
        K = len(self.types)
        for k in range(K):
            eps = self.rng.normal(0, self.sw, self.N)
            U2 = self.U.copy(); U2[k] = self.U[k]*np.exp(eps)
            ll2 = self._ll_spots(self.V, U2)
            # gamma prior ratio + log-normal proposal Jacobian (u'/u)
            a = self.alpha
            lpr = (a-1)*eps - (U2[k]-self.U[k]) + eps
            acc = np.log(self.rng.random(self.N)) < (self.bt*(ll2 - self.ll_n) + lpr)
            self.U[k, acc] = U2[k, acc]; self.ll_n[acc] = ll2[acc]
            r = acc.mean(); self.n_try['w']=self.n_try.get('w',0)+1; self.n_acc['w']=self.n_acc.get('w',0)+r
            if adapt: self.sw *= np.exp(0.02*(r-0.234))

    def move_comp(self, adapt):
        for k in list(range(len(self.types)))*3:
            t = self.types[k]; j = int(self.rng.integers(self.D))
            v2 = self.V[k].copy(); v2[j] += self.rng.normal(0, self.sc[t, j]*self.dic.sd[t, j])
            lp2 = self.dic.logprior(t, v2)
            if not np.isfinite(lp2): self._acc('c', False); ok = False
            else:
                V2 = self.V.copy(); V2[k] = v2
                ll2 = self._ll_spots(V2, self.U)
                ok = np.log(self.rng.random()) < (self.bt*(ll2.sum()-self.ll_n.sum()) + lp2 - self.lp_comp[k])
                if ok: self.V = V2; self.ll_n = ll2; self.lp_comp[k] = lp2
                self._acc('c', ok)
            if adapt: self.sc[t, j] *= np.exp(0.05*((1.0 if ok else 0.0)-0.234))

    def move_type(self):
        k = int(self.rng.integers(len(self.types))); t2 = int(self.rng.integers(self.dic.T))
        if self.rng.random() < 0.5:      # relabel: keep composition, accept on prior ratio (likelihood unchanged)
            lp2 = self.dic.logprior(t2, self.V[k])
            ok = np.isfinite(lp2) and np.log(self.rng.random()) < lp2 - self.lp_comp[k]
            if ok: self.types[k] = t2; self.lp_comp[k] = lp2
            self._acc('t_relabel', ok); return
        v2 = self.dic.draw(t2, self.rng); V2 = self.V.copy(); V2[k] = v2
        ll2 = self._ll_spots(V2, self.U)
        ok = np.log(self.rng.random()) < self.bt*(ll2.sum()-self.ll_n.sum())   # prior/proposal cancel
        if ok:
            self.V = V2; self.ll_n = ll2; self.types[k] = t2; self.lp_comp[k] = self.dic.logprior(t2, v2)
        self._acc('t_redraw', ok)

    def move_birth_death(self):
        K = len(self.types)
        birth = (K == 1) or (K < self.kmax and self.rng.random() < 0.5)
        pb = lambda k: 1.0 if k == 1 else (0.0 if k == self.kmax else 0.5)
        if birth:
            t = int(self.rng.integers(self.dic.T)); v = self.dic.draw(t, self.rng)
            u = self.rng.gamma(self.alpha, 1.0, self.N)
            pos = int(self.rng.integers(K+1))
            V2 = np.insert(self.V, pos, v, axis=0); U2 = np.insert(self.U, pos, u, axis=0)
            ll2 = self._ll_spots(V2, U2)
            logA = self.bt*(ll2.sum()-self.ll_n.sum()) + self.logpK[K+1]-self.logpK[K] + np.log((1-pb(K+1))/pb(K))
            ok = np.log(self.rng.random()) < logA
            if ok:
                self.V, self.U, self.ll_n = V2, U2, ll2
                self.types.insert(pos, t); self.lp_comp = np.insert(self.lp_comp, pos, self.dic.logprior(t, v))
            self._acc('b', ok)
        else:
            k = int(self.rng.integers(K)); u = self.U[k]
            V2 = np.delete(self.V, k, axis=0); U2 = np.delete(self.U, k, axis=0)
            ll2 = self._ll_spots(V2, U2)
            logA = self.bt*(ll2.sum()-self.ll_n.sum()) + self.logpK[K-1]-self.logpK[K] + np.log(pb(K-1)/(1-pb(K)))
            ok = np.log(self.rng.random()) < logA
            if ok:
                self.V, self.U, self.ll_n = V2, U2, ll2
                del self.types[k]; self.lp_comp = np.delete(self.lp_comp, k)
            self._acc('d', ok)


    # ---------- split / merge (Carter et al. 2025 "merging two similar components"; split is its reverse)
    def _lg(self, x):   # log Gamma(alpha,1) density
        a = self.alpha; return (a-1)*np.log(x) - x - gammaln(a)

    def move_split_merge(self, tau=0.3):
        K = len(self.types); a = self.alpha
        pb = lambda k: 1.0 if k == 1 else (0.0 if k == self.kmax else 0.5)
        split = self.rng.random() < pb(K)
        if split:
            i = int(self.rng.integers(K)); t = self.types[i]; v = self.V[i]
            sd = tau*self.dic.sd[t]; delta = self.rng.normal(0, sd)
            v2 = v + delta; lpv2 = self.dic.logprior(t, v2)
            if not np.isfinite(lpv2): self._acc('split', False); return
            r = np.clip(self.rng.beta(a, a, self.N), 1e-12, 1-1e-12); u = self.U[i]
            pos = int(self.rng.integers(K+1))
            U2 = self.U.copy(); U2[i] = u*r
            V2 = np.insert(self.V, pos, v2, axis=0); U2 = np.insert(U2, pos, u*(1-r), axis=0)
            types2 = list(self.types); types2.insert(pos, t)
            m = sum(1 for k, tt in enumerate(types2) if tt == t and k != pos)
            ll2 = self._ll_spots(V2, U2)
            lq_delta = np.sum(-0.5*(delta/sd)**2 - np.log(sd) - 0.5*np.log(2*np.pi))
            lbeta = np.sum((a-1)*np.log(r) + (a-1)*np.log(1-r) - betaln(a, a))
            lw = np.sum(self._lg(u*r) + self._lg(u*(1-r)) - self._lg(u) + np.log(u))
            logA = self.bt*(ll2.sum()-self.ll_n.sum()) + self.logpK[K+1]-self.logpK[K] - np.log(self.dic.T) + lpv2 \
                   - lq_delta - lbeta + lw + np.log((1-pb(K+1))/pb(K)) + np.log(K/m)
            ok = np.log(self.rng.random()) < logA
            if ok:
                self.V, self.U, self.ll_n, self.types = V2, U2, ll2, types2
                self.lp_comp = np.insert(self.lp_comp, pos, lpv2)
            self._acc('split', ok)
        else:
            j = int(self.rng.integers(K)); t = self.types[j]
            cands = [k for k, tt in enumerate(self.types) if tt == t and k != j]
            if not cands: self._acc('merge', False); return
            i = cands[int(self.rng.integers(len(cands)))]; m = len(cands)
            v, v2 = self.V[i], self.V[j]; sd = tau*self.dic.sd[t]; delta = v2 - v
            u = self.U[i] + self.U[j]; r = np.clip(self.U[i]/u, 1e-12, 1-1e-12)
            U2 = self.U.copy(); U2[i] = u
            V2 = np.delete(self.V, j, axis=0); U2 = np.delete(U2, j, axis=0)
            ll2 = self._ll_spots(V2, U2)
            lq_delta = np.sum(-0.5*(delta/sd)**2 - np.log(sd) - 0.5*np.log(2*np.pi))
            lbeta = np.sum((a-1)*np.log(r) + (a-1)*np.log(1-r) - betaln(a, a))
            lw = np.sum(self._lg(u*r) + self._lg(u*(1-r)) - self._lg(u) + np.log(u))
            logA_split = -self.bt*(ll2.sum()-self.ll_n.sum()) + self.logpK[K]-self.logpK[K-1] - np.log(self.dic.T) + self.lp_comp[j] \
                   - lq_delta - lbeta + lw + np.log((1-pb(K))/pb(K-1)) + np.log((K-1)/m)
            ok = np.log(self.rng.random()) < -logA_split
            if ok:
                self.V, self.U, self.ll_n = V2, U2, ll2
                del self.types[j]; self.lp_comp = np.delete(self.lp_comp, j)
            self._acc('merge', ok)

    def logpost(self):
        return self.ll_n.sum() + self.logpK[len(self.types)] + self.lp_comp.sum() + self._logprior_U(self.U)

    def run(self, n_iter, burn, thin=100):
        self.init(); out = []; trace = []
        for it in range(n_iter):
            adapt = it < burn
            self.bt = 1.0
            if it == burn: self.n_acc = {}; self.n_try = {}
            self.move_weights(adapt); self.move_comp(adapt)
            if self.rng.random() < 0.2: self.move_type()
            if self.rng.random() < 0.3: self.move_birth_death()
            if self.rng.random() < 0.5: self.move_split_merge()
            if it % thin == 0:
                trace.append((it, len(self.types), self.logpost(), self.ll_n.sum()))
                if it >= burn:
                    W = self.U/self.U.sum(0, keepdims=True)
                    out.append(dict(K=len(self.types), types=list(self.types), V=self.V.copy(),
                                    W=W.copy(), ll=self.ll_n.sum(), Y=self._model(self.V, self.U)))
        return out, np.array(trace), {k: self.n_acc[k]/self.n_try[k] for k in self.n_try}
