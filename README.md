# Gettings started
Please use Python>=3.5.

To start the challenge interactively(recommended):
```
pip install -r requirements.txt
jupyter notebook
```
and open the challenge notebook.

If you prefer to just work on a script:
```
pip install pandas
python challenge.py
```

## Evaluation
Your solution will be evaluated against the following criteria:

* pandas/numpy knowledge
* complexity (the lower the better)
* efficiency (use of GIL releasing / cythonized functions, memory use, etc.)
* ease of parallelization
* readability (PEP8 Standard)
* documentation

### Automatic criteria
Due to high submission count with great differences in solution quality
we evaluate all challenges first automatically.

* 30 points for correctness
* 30 points for speed rel to 60 sec.
* 20 points for memory rel to 1GB
* 10 points for doc
* 10 points for flake8 compliance

Please don't generate testdata in your submission. Your solution will be evaluated
automatically and checked for correctness using an automated testuite on real data.


## Submission

### Challenge
The `SUM_INTERVAL` variable contains relative time intervals in days.
So the first means 7 days back until today (asof time writing this 2016-02-01).

The generated files contain 1000 distinct users which made visits over the timespan of one month.
Each visit has a value for `feature a`, as awell as `feature_b` assigned to it.

**For each user calculate the sum of it's respective features for each time interval.
The final output should be a dataframe or numpy matrix containing one row per user,
an id column an the feature columns (N_users, 1 + N_intervals*N_features)**

### Note
The feature columns are expected to be in descending order (in terms of days included, so
30 days feature A as the first column and 30 days feature B is second and so on). 
The resulting matrix should be ordered by the user ids.

When the relative interval `(-7, 0)` is given with the date `2017-02-01` the semantics 
are to include features values within following time interval: 
`[2016-01-25 00:00:00; 2016-02-01 00:00:00)`

*You are encouraged to use the pandas library for this task but it is not required.*

### File Format

Please zip your solution including all files (do not include the generated data directory!)
and send to us with the following naming schema:
```
cc_<name>_<last_name>.zip
```
Send each code challenge as a separate zip file!

Solutions that don't follow this convention can not be evaluated.
