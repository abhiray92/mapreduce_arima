#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
import numpy as np
from sklearn.experimental import enable_iterative_imputer
from sklearn.impute import KNNImputer
import sys
import os

# In[5]:


data = pd.read_csv('household_power_consumption.00010.00002.csv', usecols=["Date", "Time", "Global_Active_Energy" ])
print(data.isna().sum())


# In[ ]:


def df_imputer(df_import):
    imputer = KNNImputer(n_neighbors=5)
    df_import2 = pd.DataFrame(imputer.fit_transform(df_import))
    df_import2.columns = df_import.columns
    return df_import2
print("Function df_imputer created")


# In[ ]:


data[['Global_Active_Energy']] = df_imputer(data[['Global_Active_Energy']])

print(data.isna().sum())
# In[ ]:


data.to_csv('household_power_consumption.00010.00002.csv', index=False)

