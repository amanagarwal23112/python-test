
# coding: utf-8

# In[ ]:


import pandas as pd
import numpy as np

data1 = pd.read_csv('C:/Users/DELL/Desktop/intern/INFY 2015-2016.csv')
print(data1)

data1['prcnt_vol']=data1.Volume.pct_change() * 100
data1['volume_shocks']=np.where(data1['prcnt_vol']>10,1,0)

