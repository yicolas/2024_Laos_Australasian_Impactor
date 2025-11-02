Last login: Mon Oct  6 17:56:48 on ttys008
(base) nicolasanderson@Mac ~ % which python
/opt/anaconda3/bin/python
(base) nicolasanderson@Mac ~ % cd /Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py sam_NWF-A_block.csv
(base) nicolasanderson@Mac SAM_Header-master % python
Python 3.13.5 | packaged by Anaconda, Inc. | (main, Jun 12 2025, 11:23:37) [Clang 14.0.6(base) n(b(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py sam_NWF-A_block.csv
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py sam_NWF-A_block.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - sam_NWF-A_block.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWF-A-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +1.10

NWF-A-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    -0.80

NWF-A-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    -10.50
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWF-A-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -0.70

NWF-A-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +2.30


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWF-A-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
Traceback (most recent call last):
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 488, in <module>
    main()
    ~~~~^^
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 236, in main
    assert (len(site_id) <= 5),\
            ^^^^^^^^^^^^^^^^^
AssertionError: Locality ID exceeds 5 characters: refer to:http://cires.colorado.edu/people/jones.craig/PMag_Formats.html (although that says that 4 is the limit)
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py sam_NWF-A_block.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - sam_NWF-A_block.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWF-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +1.10

NWF-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    -0.80

NWF-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    -10.50
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWF-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -0.70

NWF-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +2.30


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWF-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWF-1
Writing file - NWF-2
Writing file - NWF-3
Writing file - NWF-4
Writing file - NWF-5
Writing file - NWF-.csv
Writing file - NWF-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py A-.csv         
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - A-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
A-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +1.10

A-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    -0.80

A-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    -10.50
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

A-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -0.70

A-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +2.30


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - A-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - A-1
Writing file - A-2
Writing file - A-3
Writing file - A-4
Writing file - A-5
Writing file - A-.csv
Writing file - A-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFA-.csv 
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFA-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +1.10

NWFA-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    -0.80

NWFA-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    -10.50
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -0.70

NWFA-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +2.30


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFA-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFA-1
Writing file - NWFA-2
Writing file - NWFA-3
Writing file - NWFA-4
Writing file - NWFA-5
Writing file - NWFA-.csv
Writing file - NWFA-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFA-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWF-A-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +96.10
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWF-A-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    +3.20

NWF-A-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    +14.50
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWF-A-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +7.30
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWF-A-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -125.70
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWF-A-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
Traceback (most recent call last):
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 488, in <module>
    main()
    ~~~~^^
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 236, in main
    assert (len(site_id) <= 5),\
            ^^^^^^^^^^^^^^^^^
AssertionError: Locality ID exceeds 5 characters: refer to:http://cires.colorado.edu/people/jones.craig/PMag_Formats.html (although that says that 4 is the limit)
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFA-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFA-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +95.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    +4.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    +25.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +8.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -128.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFA-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFA-1
Writing file - NWFA-2
Writing file - NWFA-3
Writing file - NWFA-4
Writing file - NWFA-5
Traceback (most recent call last):
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 488, in <module>
    main()
    ~~~~^^
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 343, in main
    raise KeyError('there is no item: ' + header[i])
KeyError: 'there is no item: original'
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFA-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFA-1 has local IGRF declination of: 
-1.3787129014886546
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +95.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-2 has local IGRF declination of: 
-1.3787142512838955
The local declination calculated through magnetic and sun compass comparison is:
    +4.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-3 has local IGRF declination of: 
-1.3787081772051124
The local declination calculated through magnetic and sun compass comparison is:
    +25.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-4 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    +8.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFA-5 has local IGRF declination of: 
-1.3787156010791364
The local declination calculated through magnetic and sun compass comparison is:
    -128.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.378713306427187

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFA-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFA-1
Writing file - NWFA-2
Writing file - NWFA-3
Writing file - NWFA-4
Writing file - NWFA-5
Writing file - NWFA-.csv
Writing file - NWFA-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFB-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFB-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFB-1 has local IGRF declination of: 
-1.3635918178120505
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

NWFB-2 has local IGRF declination of: 
-1.3635931562571386
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

NWFB-3 has local IGRF declination of: 
-1.3635933793312915
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.363592784466827

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFB-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFB-1
Writing file - NWFB-2
Writing file - NWFB-3
Writing file - NWFB-.csv
Writing file - NWFB-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFB-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFB-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
Traceback (most recent call last):
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 488, in <module>
    main()
    ~~~~^^
  File "/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py", line 106, in main
    raise ValueError("not enough data to calculate IGRF to correct "
                     "bedding please input at least GMT_offset, "
                     "year, month, day of measurement\n")
ValueError: not enough data to calculate IGRF to correct bedding please input at least GMT_offset, year, month, day of measurement

(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFB-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFB-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:114: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  sdf[sample][time_type] = 1
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFB-1 has local IGRF declination of: 
-1.363480392170402
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

NWFB-2 has local IGRF declination of: 
-1.363480392170402
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

NWFB-3 has local IGRF declination of: 
-1.363480392170402
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.363480392170402

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFB-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFB-1
Writing file - NWFB-2
Writing file - NWFB-3
Writing file - NWFB-.csv
Writing file - NWFB-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFB-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFB-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFB-1 has local IGRF declination of: 
-1.363480392170402
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

NWFB-2 has local IGRF declination of: 
-1.363480392170402
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

NWFB-3 has local IGRF declination of: 
-1.363480392170402
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.363480392170402

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFB-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFB-1
Writing file - NWFB-2
Writing file - NWFB-3
Writing file - NWFB-.csv
Writing file - NWFB-.inp
(base) nicolasanderson@Mac SAM_Header-master %  python mk_sam_file.py NWFC-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFC-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFC-1 has local IGRF declination of: 
-1.3528881569966984
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +0.60

NWFC-2 has local IGRF declination of: 
-1.352888939293166
The local declination calculated through magnetic and sun compass comparison is:
    -6.30

NWFC-3 has local IGRF declination of: 
-1.3528896098330279
The local declination calculated through magnetic and sun compass comparison is:
    -3.40

NWFC-4 has local IGRF declination of: 
-1.3528908391560321
The local declination calculated through magnetic and sun compass comparison is:
    -6.30

NWFC-5 has local IGRF declination of: 
-1.352891174425963
The local declination calculated through magnetic and sun compass comparison is:
    -4.50

NWFC-6 has local IGRF declination of: 
-1.3528917332091623
The local declination calculated through magnetic and sun compass comparison is:
    +0.70

NWFC-7 has local IGRF declination of: 
-1.3528941918550572
The local declination calculated through magnetic and sun compass comparison is:
    -7.30
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-8 has local IGRF declination of: 
-1.3528929625321098
The local declination calculated through magnetic and sun compass comparison is:
    -5.30


Site averages:
Average of local IGRF declination is: -1.352890950912652

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFC-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFC-1
Writing file - NWFC-2
Writing file - NWFC-3
Writing file - NWFC-4
Writing file - NWFC-5
Writing file - NWFC-6
Writing file - NWFC-7
Writing file - NWFC-8
Writing file - NWFC-.csv
Writing file - NWFC-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFC-.csv      
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFC-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFC-1 has local IGRF declination of: 
-1.3528881569966984
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +0.60

NWFC-2 has local IGRF declination of: 
-1.352888939293166
The local declination calculated through magnetic and sun compass comparison is:
    -6.30

NWFC-3 has local IGRF declination of: 
-1.3528896098330279
The local declination calculated through magnetic and sun compass comparison is:
    -3.40

NWFC-4 has local IGRF declination of: 
-1.3528908391560321
The local declination calculated through magnetic and sun compass comparison is:
    -6.30

NWFC-5 has local IGRF declination of: 
-1.352891174425963
The local declination calculated through magnetic and sun compass comparison is:
    -4.50

NWFC-6 has local IGRF declination of: 
-1.3528917332091623
The local declination calculated through magnetic and sun compass comparison is:
    +0.70

NWFC-7 has local IGRF declination of: 
-1.3528941918550572
The local declination calculated through magnetic and sun compass comparison is:
    -7.30
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-8 has local IGRF declination of: 
-1.3528929625321098
The local declination calculated through magnetic and sun compass comparison is:
    -5.30


Site averages:
Average of local IGRF declination is: -1.352890950912652

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFC-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFC-1
Writing file - NWFC-2
Writing file - NWFC-3
Writing file - NWFC-4
Writing file - NWFC-5
Writing file - NWFC-6
Writing file - NWFC-7
Writing file - NWFC-8
Writing file - NWFC-.csv
Writing file - NWFC-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFC-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFC-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFC-1 has local IGRF declination of: 
-1.3528881569966984
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    -35.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-2 has local IGRF declination of: 
-1.352888939293166
The local declination calculated through magnetic and sun compass comparison is:
    -62.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-3 has local IGRF declination of: 
-1.3528896098330279
The local declination calculated through magnetic and sun compass comparison is:
    -217.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-4 has local IGRF declination of: 
-1.3528908391560321
The local declination calculated through magnetic and sun compass comparison is:
    +6.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-5 has local IGRF declination of: 
-1.352891174425963
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:145: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec - 360
    -123.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-6 has local IGRF declination of: 
-1.3528917332091623
The local declination calculated through magnetic and sun compass comparison is:
    +172.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-7 has local IGRF declination of: 
-1.3528941918550572
The local declination calculated through magnetic and sun compass comparison is:
    -136.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-8 has local IGRF declination of: 
-1.3528929625321098
The local declination calculated through magnetic and sun compass comparison is:
    -156.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.352890950912652

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFC-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFC-1
Writing file - NWFC-2
Writing file - NWFC-3
Writing file - NWFC-4
Writing file - NWFC-5
Writing file - NWFC-6
Writing file - NWFC-7
Writing file - NWFC-8
Writing file - NWFC-.csv
Writing file - NWFC-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKQA-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKQA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:114: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  sdf[sample][time_type] = 1
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKQA-0 has local IGRF declination of: 
-1.2929551585191916
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
PKQA-1 has local IGRF declination of: 
-1.2930273839924098
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    -2.50

PKQA-2 has local IGRF declination of: 
-1.293028256807247
The local declination calculated through magnetic and sun compass comparison is:
    -0.10

PKQA-3 has local IGRF declination of: 
-1.2930188740465383
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKQA-4 has local IGRF declination of: 
-1.2930192013521946
The local declination calculated through magnetic and sun compass comparison is:
    +3.40

PKQA-5 has local IGRF declination of: 
-1.2930220380009132
The local declination calculated through magnetic and sun compass comparison is:
    +1.40

PKQA-6 has local IGRF declination of: 
-1.2930232381214637
The local declination calculated through magnetic and sun compass comparison is:
    -2.30

PKQA-7 has local IGRF declination of: 
-1.2930309843537202
The local declination calculated through magnetic and sun compass comparison is:
    -3.10

PKQA-8 has local IGRF declination of: 
-1.2930312025574722
The local declination calculated through magnetic and sun compass comparison is:
    -11.70
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

PKQA-9 has local IGRF declination of: 
-1.2930313116593197
The local declination calculated through magnetic and sun compass comparison is:
    -8.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.293018764941047

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKQA-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKQA-0
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
Writing file - PKQA-1
Writing file - PKQA-2
Writing file - PKQA-3
Writing file - PKQA-4
Writing file - PKQA-5
Writing file - PKQA-6
Writing file - PKQA-7
Writing file - PKQA-8
Writing file - PKQA-9
Writing file - PKQA-.csv
Writing file - PKQA-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSJ-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSJ-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSJ-1 has local IGRF declination of: 
-1.3436219569743457
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

PKSJ-2 has local IGRF declination of: 
-1.3436224046679968
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSJ-3 has local IGRF declination of: 
-1.3436227404382066
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.343622367360183

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSJ-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSJ-1
Writing file - PKSJ-2
Writing file - PKSJ-3
Writing file - PKSJ-.csv
Writing file - PKSJ-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSK-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSK-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSK-1 has local IGRF declination of: 
-1.3434844081797905
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

PKSK-2 has local IGRF declination of: 
-1.3434846320184874
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.343484520099139

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSK-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSK-1
Writing file - PKSK-2
Writing file - PKSK-.csv
Writing file - PKSK-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSI-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSI-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSI-1 has local IGRF declination of: 
-1.3366204526063825
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +6.70
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.3366204526063825

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSI-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSI-1
Writing file - PKSI-.csv
Writing file - PKSI-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSB-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSB-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSB-1 has local IGRF declination of: 
-1.3269903543554165
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +1.40


Site averages:
Average of local IGRF declination is: -1.3269903543554165

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSB-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:208: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['correct_bedding_using_local_dec'] = 'yes'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSB-1
Writing file - PKSB-.csv
Writing file - PKSB-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSB-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSB-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSB-1 has local IGRF declination of: 
-1.3269903543554165
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    -76.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different


Site averages:
Average of local IGRF declination is: -1.3269903543554165

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSB-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:226: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['corrected_bedding_strike'] = (float(df[sample]['bedding_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSB-1
Writing file - PKSB-.csv
Writing file - PKSB-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSF-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSF-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSF-1.0 has local IGRF declination of: 
-1.3256429940250314
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +9.40
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

PKSF-2.0 has local IGRF declination of: 
-1.3256445527060237
The local declination calculated through magnetic and sun compass comparison is:
    -1.50

PKSF-3.0 has local IGRF declination of: 
-1.325645109377831
The local declination calculated through magnetic and sun compass comparison is:
    +5.30
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

PKSF-4.0 has local IGRF declination of: 
-1.3256458887182703
The local declination calculated through magnetic and sun compass comparison is:
    +62.00
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

PKSF-5.0 has local IGRF declination of: 
-1.3256467793930824
The local declination calculated through magnetic and sun compass comparison is:
    -5.70

PKSF-6.0 has local IGRF declination of: 
-1.3256474473992057
The local declination calculated through magnetic and sun compass comparison is:
    -6.90
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

PKSF-7.0 has local IGRF declination of: 
-1.3256484494083338
The local declination calculated through magnetic and sun compass comparison is:
    -0.70

PKSF-8.0 has local IGRF declination of: 
-1.3256488947457115
The local declination calculated through magnetic and sun compass comparison is:
    -2.00

PKSF-9.0 has local IGRF declination of: 
-1.3256492287487731
The local declination calculated through magnetic and sun compass comparison is:
    -1.00

PKSF-0.0 has local IGRF declination of: 
-1.3256497854205236
The local declination calculated through magnetic and sun compass comparison is:
    +4.90
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

PKSF-1.1 has local IGRF declination of: 
-1.325651900773039
The local declination calculated through magnetic and sun compass comparison is:
    -1.70


Site averages:
Average of local IGRF declination is: -1.3256473664287114

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSF-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSF-1.0
Writing file - PKSF-2.0
Writing file - PKSF-3.0
Writing file - PKSF-4.0
Writing file - PKSF-5.0
Writing file - PKSF-6.0
Writing file - PKSF-7.0
Writing file - PKSF-8.0
Writing file - PKSF-9.0
Writing file - PKSF-0.0
Writing file - PKSF-1.1
Writing file - PKSF-.csv
Writing file - PKSF-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py NWFC-.csv        
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - NWFC-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
NWFC-1 has local IGRF declination of: 
-1.3528881569966984
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +0.60

NWFC-2 has local IGRF declination of: 
-1.352888939293166
The local declination calculated through magnetic and sun compass comparison is:
    -6.30

NWFC-3 has local IGRF declination of: 
-1.3528896098330279
The local declination calculated through magnetic and sun compass comparison is:
    -3.40

NWFC-4 has local IGRF declination of: 
-1.3528908391560321
The local declination calculated through magnetic and sun compass comparison is:
    -6.30

NWFC-5 has local IGRF declination of: 
-1.352891174425963
The local declination calculated through magnetic and sun compass comparison is:
    -4.50

NWFC-6 has local IGRF declination of: 
-1.3528917332091623
The local declination calculated through magnetic and sun compass comparison is:
    +0.70

NWFC-7 has local IGRF declination of: 
-1.3528941918550572
The local declination calculated through magnetic and sun compass comparison is:
    -7.30
WARNING: local IGRF declination & calculated magnetic declination are more than 5 degree different

NWFC-8 has local IGRF declination of: 
-1.3528929625321098
The local declination calculated through magnetic and sun compass comparison is:
    -5.30


Site averages:
Average of local IGRF declination is: -1.352890950912652

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - NWFC-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - NWFC-1
Writing file - NWFC-2
Writing file - NWFC-3
Writing file - NWFC-4
Writing file - NWFC-5
Writing file - NWFC-6
Writing file - NWFC-7
Writing file - NWFC-8
Writing file - NWFC-.csv
Writing file - NWFC-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSG-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSG-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSG-1 has local IGRF declination of: 
-1.3289451229312021
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

PKSG-2 has local IGRF declination of: 
-1.3289462355020305
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-3 has local IGRF declination of: 
-1.328947348072802
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-4 has local IGRF declination of: 
-1.328948238129442
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-5 has local IGRF declination of: 
-1.3289487944148277
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-6 has local IGRF declination of: 
-1.3289501294997876
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-7 has local IGRF declination of: 
-1.3289499069855992
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-8 has local IGRF declination of: 
-1.3289507970422392
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.3289483215722413

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSG-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSG-1
Writing file - PKSG-2
Writing file - PKSG-3
Writing file - PKSG-4
Writing file - PKSG-5
Writing file - PKSG-6
Writing file - PKSG-7
Writing file - PKSG-8
Writing file - PKSG-.csv
Writing file - PKSG-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSG-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSG-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSG-1 has local IGRF declination of: 
-1.3289451229312021
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

PKSG-2 has local IGRF declination of: 
-1.3289462355020305
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-3 has local IGRF declination of: 
-1.328947348072802
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-4 has local IGRF declination of: 
-1.328948238129442
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-5 has local IGRF declination of: 
-1.3289487944148277
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-6 has local IGRF declination of: 
-1.3289501294997876
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-7 has local IGRF declination of: 
-1.3289499069855992
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-8 has local IGRF declination of: 
-1.3289507970422392
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.3289483215722413

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSG-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSG-1
Writing file - PKSG-2
Writing file - PKSG-3
Writing file - PKSG-4
Writing file - PKSG-5
Writing file - PKSG-6
Writing file - PKSG-7
Writing file - PKSG-8
Writing file - PKSG-.csv
Writing file - PKSG-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSG-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSG-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSG-1 has local IGRF declination of: 
-1.3289451229312021
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

PKSG-2 has local IGRF declination of: 
-1.3289462355020305
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-3 has local IGRF declination of: 
-1.328947348072802
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-4 has local IGRF declination of: 
-1.328948238129442
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-5 has local IGRF declination of: 
-1.3289487944148277
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-6 has local IGRF declination of: 
-1.3289501294997876
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-7 has local IGRF declination of: 
-1.3289499069855992
The local declination calculated through magnetic and sun compass comparison is:
insufficient data

PKSG-8 has local IGRF declination of: 
-1.3289507970422392
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.3289483215722413

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSG-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:252: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = "     0"
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSG-1
Writing file - PKSG-2
Writing file - PKSG-3
Writing file - PKSG-4
Writing file - PKSG-5
Writing file - PKSG-6
Writing file - PKSG-7
Writing file - PKSG-8
Writing file - PKSG-.csv
Writing file - PKSG-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py PKSH-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - PKSH-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:102: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['sun_core_strike'] = round(sundec(sundata), 1)
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
PKSH-1 has local IGRF declination of: 
-1.3277739718623138
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:147: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = calc_mag_dec
    +2.30

PKSH-2 has local IGRF declination of: 
-1.3277748619053114
The local declination calculated through magnetic and sun compass comparison is:
    +1.80

PKSH-3 has local IGRF declination of: 
-1.3277783108218841
The local declination calculated through magnetic and sun compass comparison is:
    -0.20


Site averages:
Average of local IGRF declination is: -1.3277757148631697

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - PKSH-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:220: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = float(df[sample]['sun_core_strike'])
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:221: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'sun compass orientation'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - PKSH-1
Writing file - PKSH-2
Writing file - PKSH-3
Writing file - PKSH-.csv
Writing file - PKSH-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py WBEA-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - WBEA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
WBEA-1 has local IGRF declination of: 
-1.354093127081569
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

WBEA-2 has local IGRF declination of: 
-1.3540945897736378
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.3540938584276034

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - WBEA-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - WBEA-1
Writing file - WBEA-2
Writing file - WBEA-.csv
Writing file - WBEA-.inp
(base) nicolasanderson@Mac SAM_Header-master % python mk_sam_file.py WBEA-.csv
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:356: SyntaxWarning: invalid escape sequence '\ '
  break types '\ r' and '\ n' so that python will for sure register all lines
Reading in file - WBEA-.csv
---------------------LOCAL MAGNETIC DECLINATION-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:120: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_IGRF'] = list(
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:126: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['IGRF_local_dec'] = df[sample]['calculated_IGRF'][0] - 360
WBEA-1 has local IGRF declination of: 
-1.354093127081569
The local declination calculated through magnetic and sun compass comparison is:
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:137: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['calculated_mag_dec'] = 'insufficient data'
insufficient data

WBEA-2 has local IGRF declination of: 
-1.3540945897736378
The local declination calculated through magnetic and sun compass comparison is:
insufficient data


Site averages:
Average of local IGRF declination is: -1.3540938584276034

---------------------OUTPUT-----------------------
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:171: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  hdf['site_info'][value] = str(round(float(hdf['site_info'][value]), 1))
Writing file - WBEA-.sam
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:216: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['core_strike'] = (float(df[sample]['magnetic_core_strike']) +
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:218: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['comment'] = 'mag compass orientation (IGRF corrected)'
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:253: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample]['strat_level'] = str((df[sample]['strat_level']))
/Users/nicolasanderson/Library/CloudStorage/OneDrive-CaliforniaInstituteofTechnology/Anderson/CIT/SAM_Header-master/mk_sam_file.py:283: FutureWarning: ChainedAssignmentError: behaviour will change in pandas 3.0!
You are setting values through chained assignment. Currently this works in certain cases, but when using Copy-on-Write (which will become the default behaviour in pandas 3.0) this will never work to update the original DataFrame or Series, because the intermediate object on which we are setting values will behave as a copy.
A typical example is when you are setting values in a column of a DataFrame, like:

df["col"][row_indexer] = value

Use `df.loc[row_indexer, "col"] = values` instead, to perform the assignment in a single step and ensure this keeps updating the original `df`.

See the caveats in the documentation: https://pandas.pydata.org/pandas-docs/stable/user_guide/indexing.html#returning-a-view-versus-a-copy

  df[sample][attribute] = str(round(float(df[sample][attribute]), 1))
Writing file - WBEA-1
Writing file - WBEA-2
Writing file - WBEA-.csv
Writing file - WBEA-.inp
(base) nicolasanderson@Mac SAM_Header-master % 
