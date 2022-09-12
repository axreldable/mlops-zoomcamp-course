#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip freeze | grep scikit-learn')


# In[2]:


import pickle
import pandas as pd


# In[9]:


year = 2021
month = 2

input_file = f'https://nyc-tlc.s3.amazonaws.com/trip+data/fhv_tripdata_{year:04d}-{month:02d}.parquet'
input_file = f'./data/fhv_tripdata_{year:04d}-{month:02d}.parquet'
output_file = f'output/fhv_tripdata_{year:04d}-{month:02d}.parquet'
print(input_file)


# In[10]:


with open('model.bin', 'rb') as f_in:
    dv, lr = pickle.load(f_in)


# In[11]:


categorical = ['PUlocationID', 'DOlocationID']

def read_data(filename):
    df = pd.read_parquet(filename)
    
    df['duration'] = df.dropOff_datetime - df.pickup_datetime
    df['duration'] = df.duration.dt.total_seconds() / 60

    df = df[(df.duration >= 1) & (df.duration <= 60)].copy()

    df[categorical] = df[categorical].fillna(-1).astype('int').astype('str')
    
    return df


# In[12]:


df = read_data(input_file)
df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')


# In[13]:


dicts = df[categorical].to_dict(orient='records')
X_val = dv.transform(dicts)
y_pred = lr.predict(X_val)


# In[14]:


y_pred.mean()


# In[21]:


df_result = pd.DataFrame()
df_result['ride_id'] = df['ride_id']
df['ride_id'] = f'{year:04d}/{month:02d}_' + df.index.astype('str')
df_result['predicted_duration'] = y_pred
df_result


# In[22]:


df_result.to_parquet(
    output_file,
    engine='pyarrow',
    compression=None,
    index=False
)


# In[23]:


get_ipython().system('ls -lh output/')


# In[24]:


df_result['predicted_duration'].mean()

