
# coding: utf-8

# In[ ]:


import pandas as pd
import pandas_datareader.data as web

data1 = pd.read_csv('C:/Users/DELL/Desktop/intern/INFY 2015-2016.csv')

open = f.Open.resample('W-MON', how='last')
close = f.Close.resample('W-FRI', how='last').resample('W-MON', how='last')
high = f.High.resample('W-MON', how='max')
low = f.Low.resample('W-MON', how='min')
vol = f.Volume.resample('W-MON', how='sum')
weekly_data = pd.concat([open, close, high, low, vol], axis=1)

pd.concat([open, close, high, low, vol], axis=1)

