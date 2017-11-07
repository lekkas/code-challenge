# coding: utf-8
"""Challenge

The `SUM_INTERVAL` variable contains relative time
intervals in days. So the first means 7 days back until today.

The generated files contain 1000 distinct users which made
visits over the timespan of one month. Each visit has a
value for `feature a`, as awell as `feature_b` assigned to it.

For each user calculate the sum of it's respective features
for each time interval. The final output should be a numpy
matrix containing one row per user, an id column an the feature
columns (N_users, 1 + N_intervals*N_features)

You are encouraged to use the pandas library for this task
but it is not required.
"""
import os
import pandas as pd
import numpy as np
import uuid
from tqdm import tqdm

SUM_INTERVALS = [(-7, 0), (-14, 0), (-30, 0)]


def bin_sum_features(csv_glob="data/shard-*.csv.gz",
                     today=pd.Timestamp('2016-02-01')):
    pass


def generate_data():
    # Generate some random data
    uids = np.array([str(uuid.uuid4()) for _ in range(1000)])
    times = pd.date_range('2016-01-01', '2016-02-01', freq='d')
    data = dict(
        id=np.random.choice(uids, 100000),
        timestamp=np.random.choice(times, 100000),
        feature_a=np.random.randint(0, 100, 100000),
        feature_b=np.random.random(100000),
    )

    df = pd.DataFrame(data)\
        .set_index('timestamp')\
        .sort_index()

    os.makedirs('data', exist_ok=True)

    for ts in tqdm(times):
        path = "data/shard-{:%Y-%m-%d}.csv.gz".format(ts)
        df.loc['{:%Y-%m-%d}'.format(ts)]\
            .reset_index()\
            .sample(frac=1)\
            .to_csv(path, index=False, compression='gzip')


if __name__ == '__main__':
    # uncomment for your testing but leave commented in submission
    # generate_data()
    res = bin_sum_features("data/shard-*.csv.gz",
                           pd.Timestamp('2016-02-01'))
