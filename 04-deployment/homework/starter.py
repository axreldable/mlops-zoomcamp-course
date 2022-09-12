#!/usr/bin/env python
# coding: utf-8

# In[1]:
import argparse
import pickle

import pandas as pd


# get_ipython().system('pip freeze | grep scikit-learn')
# In[2]:


# In[9]:


# In[10]:


# In[11]:


def read_data(filename):
    categorical = ['PUlocationID', 'DOlocationID']

    df = pd.read_parquet(filename)

    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')

    return df


# In[12]:


# In[13]:


# In[14]:


# In[21]:


# In[22]:


# In[23]:


# get_ipython().system('ls -lh output/')


# In[24]:


def run(year, month):
    input_file = f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet'
    input_file = f'./data/fhv_tripdata_{year:04d}-{month:02d}.parquet'
    output_file = f'output/fhv_tripdata_{year:04d}-{month:02d}.parquet'
    print(input_file)

    with open('model.bin', 'rb') as f_in:
        dv, lr = pickle.load(f_in)

    df = read_data(input_file)
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')

    categorical = ['PUlocationID', 'DOlocationID']
    dicts = df[categorical].to_dict(orient='records')
    X_val = dv.transform(dicts)
    y_pred = lr.predict(X_val)

    y_pred.mean()

    df_result = pd.DataFrame()
    df_result['ride_id'] = df['ride_id']
    df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
    df_result['predicted_duration'] = y_pred
    df_result

    df_result.to_parquet(
        output_file,
        engine='pyarrow',
        compression=None,
        index=False
    )

    print(df_result['predicted_duration'].mean())


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--year",
        type=int,
        default=2021,
        help="year"
    )
    parser.add_argument(
        "--month",
        type=int,
        default=2,
        help="year"
    )
    args = parser.parse_args()

    run(args.year, args.month)
