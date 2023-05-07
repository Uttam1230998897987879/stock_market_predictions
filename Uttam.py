#!/usr/bin/env python
# coding: utf-8

# # Stock Market Prediction 

# In[ ]:


### Microsoft dataset


# In[1]:


# dataset @ https://finance.yahoo.com/quote/MSFT/history?period1=1651810969&period2=1683346969&interval=1d&filter=history&frequency=1d&includeAdjustedClose=true


# In[3]:


import pandas as pd

df = pd.read_csv('MSFT.csv')

df


# In[4]:


df = df[['Date', 'Close']]

df


# In[5]:


df['Date']


# In[7]:


import datetime

def str_to_datetime(s):
  split = s.split('-')
  year, month, day = int(split[0]), int(split[1]), int(split[2])
  return datetime.datetime(year=year, month=month, day=day)

datetime_object = str_to_datetime('2022-05-06')
datetime_object


# In[8]:


df


# In[9]:


df['Date'] = df['Date'].apply(str_to_datetime)
df['Date']


# In[10]:


df.index = df.pop('Date')
df


# In[11]:


import matplotlib.pyplot as plt

plt.plot(df.index, df['Close'])


# In[ ]:





# In[ ]:





# In[ ]:




