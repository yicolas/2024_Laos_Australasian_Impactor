import os
import numpy as np, pandas as pd, pickle, sys, time
from multiprocessing import Pool
from load import epma, sources_all as sources, OX, PAAS
from rjmcmc import Dictionary, RJMCMC

# EPMA 1-sigma relative precision used as clr-space sigma (d ln x = dx/x)
SIG_PREC = dict(SiO2=0.005,TiO2=0.04,Al2O3=0.01,FeOt=0.02,MnO=0.20,MgO=0.02,CaO=0.02,Na2O=0.03,K2O=0.02)
# EPMA accuracy (1 sigma, relative) combined in quadrature with a 5 % mixing-model error
ACC = dict(SiO2=0.01,TiO2=0.05,Al2O3=0.02,FeOt=0.03,MnO=0.20,MgO=0.03,CaO=0.03,Na2O=0.05,K2O=0.03)
SIG_MODEL = {o: (ACC[o]**2+0.05**2)**0.5 for o in ACC}
SIG = SIG_MODEL
RANDOM_HI = dict(SiO2=100,TiO2=5,Al2O3=40,FeOt=30,MnO=1,MgO=40,CaO=60,Na2O=10,K2O=10)

def build_dictionary(include_paas=True, include_random=True, oxides=OX):
    s = sources(); names=[]; mu=[]; sd=[]; lo=[]; hi=[]
    for t, g in s.groupby('type'):
        x = g[oxides].values; m = np.median(x, 0)                     # robust: median and 1.4826*MAD
        sdev = 1.4826*np.median(np.abs(x-m), 0) if len(x) > 1 else np.zeros_like(m)
        rel = 0.25 if len(x) < 5 else 0.15                           # widen poorly-sampled lithologies
        sdev = np.maximum.reduce([sdev, rel*m, np.full_like(m, 0.05)])
        names.append(t); mu.append(m); sd.append(sdev)
        lo.append(np.maximum(1e-3, x.min(0)-3*sdev)); hi.append(np.minimum(100, x.max(0)+3*sdev))
    if include_paas:
        m = np.array([PAAS[o] for o in oxides]); sdev = np.maximum(0.2*m, 0.05)
        names.append('Unweathered shale (PAAS)'); mu.append(m); sd.append(sdev)
        lo.append(np.maximum(1e-3, m-3*sdev)); hi.append(m+3*sdev)
    if include_random:
        h = np.array([RANDOM_HI[o] for o in oxides])
        names.append('Random'); mu.append(h/2); sd.append(h*100); lo.append(np.full_like(h,1e-3)); hi.append(h)
    return Dictionary(names, mu, sd, lo, hi)

def one_chain(args):
    cfg, seed = args
    ox = cfg.get('oxides', OX)
    e = epma(); data = e[ox].values.T; data = data/data.sum(0)*100
    dic = build_dictionary(cfg.get('paas', True), cfg.get('random', True), ox)
    sig = SIG_PREC if cfg.get('sigma')=='precision' else SIG_MODEL
    m = RJMCMC(data, [sig[o] for o in ox], dic, lam=cfg.get('lam',10), kmax=30, seed=seed)
    t0 = time.time(); out, trace, acc = m.run(cfg['n'], cfg['burn'], thin=cfg.get("thin",200))
    return dict(seed=seed, out=out, trace=trace, acc=acc, names=dic.names, time=time.time()-t0, spots=e.spot.tolist(),
                tektite=e.tektite.tolist(), oxides=ox)

if __name__ == '__main__':
    name = sys.argv[1]; n = int(sys.argv[2]); chains = int(sys.argv[3])
    cfgs = {'main':dict(), 'precision':dict(sigma='precision'), 'no_random':dict(random=False), 'local_only':dict(paas=False, random=False),
            'no_alkali':dict(oxides=[o for o in OX if o not in ('Na2O','K2O')])}
    cfg = dict(cfgs[name], n=n, burn=n//2)
    with Pool(min(chains, 8)) as p: res = p.map(one_chain, [(cfg, 1000+i) for i in range(chains)])
    pickle.dump(res, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), f'res_{name}.pkl'),'wb'))
    for r in res: print(name, r['seed'], round(r['time'],1),'s', {k:round(v,3) for k,v in r['acc'].items()},
                        'K_final', r['trace'][-1,1], 'll', round(r['trace'][-1,3],1))
