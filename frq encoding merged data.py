#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


df = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\bpi2016-orginal data\\df_Merged.csv',parse_dates=['TIMESTAMP'])
df


# In[3]:


df.drop(['Unnamed: 0','ContactTimeEnd'], axis=1, inplace= True)
df


# In[4]:


df1= df.sort_values(['CustomerID','TIMESTAMP'],ascending=True)
df1


# In[5]:


df2=pd.DataFrame(df.groupby(['CustomerID','Event'])['Event'].count())
df2.rename({'Event':'count'}, axis=1, inplace=True)
df2


# In[6]:


df2.to_csv('group by bpi 2016.csv')


# In[7]:


df2 = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\encoding\\frq based\\group by bpi 2016.csv')
df2


# In[8]:


np_array=df2.to_numpy()
np_array


# In[9]:


ID = sorted(df[df2.columns[0]].unique())
ID


# In[10]:


len(ID)


# In[11]:


Event = sorted(df[df2.columns[1]].unique())
Event


# In[12]:


len(Event)


# In[13]:


df_Myans = pd.pivot_table(df2, values='count', index='CustomerID', columns='Event')
df_Myans


# In[14]:


df_Myans=df_Myans.fillna(0)
df_Myans


# In[15]:


df_Myans.to_csv('Frequency based encodingBPI2016-merged data.csv')


# In[ ]:




