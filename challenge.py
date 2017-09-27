
# coding: utf-8
import pandas as pd
import numpy as np
import uuid

SUM_INTERVALS = [(-7,0), (-14,0), (-30,0)]

# Challenge:
# The `SUM_INTERVAL` variable contains relative time intervals in days. So the first means 7 days back until today.
# the dictionary `data` contains 10 distinct users which made visists over the timespan of one month. Each visit has a value for `feature a`, as awell as `feature_b` assigned to it. **For each user calculate the sum of it's respective features for each time interval. The final output should be a numpy matrix containing one row per user, an id column an the feature columns (N_users, 1 + N_intervals*N_features)**
#
# *It is encouraged to use the pandas library for this task but it is not required.*

def bin_sum_features(data, today=pd.Timestamp('2016-02-01')):
    pass

if __name__=='__main__':
    # Generate some random data
    uids=np.array([str(uuid.uuid4()) for _ in range(10)])
    times = pd.date_range('2016-01-01','2016-02-01', freq='s')
    data = dict(
        id=np.random.choice(uids, 100),
        timestamp=np.random.choice(times, 100),
        feature_a=np.random.randint(0,100, 100),
        feature_b=np.random.random(100),
    )

    res = bin_sum_features(data)
    assert isinstance(res, np.ndarray) or \
        isinstance(res, np.matrixlib.defmatrix.matrix)
    assert res.shape == (10,7)
