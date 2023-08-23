#!/usr/bin/env python
# coding: utf-8

# In[75]:


import pandas as pd
import numpy as np


# # cluster2

# In[76]:


df = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\DBSCAN clustering\\cluster2 without event with frequency0 and cluster lable.csv')
df


# In[77]:


#جایگذاری کردن آی دی به جای ایندکس
df=df.set_index('CustomerID')
df


# In[78]:


df1=pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\cluster2 event var.csv')
df1


# In[79]:


event=df.columns


# In[80]:


#df.drop(event[0], axis=1, inplace=True)
#df


# In[81]:


del_event= [event[i] for i in range(len(event)) if df1['variance'][i]<=0.25]


# In[82]:


for i in range(len(del_event)):
    df.drop(del_event[i], axis=1, inplace=True)
df


# In[83]:


df.to_csv('cluster2 removing columns with low variance.csv')


# # cluster0

# In[84]:


df = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\DBSCAN clustering\\cluster0 without event with frequency0 and cluster lable.csv')
df


# In[85]:


#جایگذاری کردن آی دی به جای ایندکس
df=df.set_index('CustomerID')
df


# In[86]:


df1=pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\cluster0 event var.csv')
df1


# In[87]:


event=df.columns


# In[88]:


del_event= [event[i] for i in range(len(event)) if df1['variance'][i]<=0.00011]


# In[89]:


for i in range(len(del_event)):
    df.drop(del_event[i], axis=1, inplace=True)
df


# In[90]:


df.to_csv('cluster0 removing columns with low variance.csv')


# # cluster1

# In[91]:


df = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\DBSCAN clustering\\cluster1 without event with frequency0 and cluster lable.csv')
df


# In[92]:


#جایگذاری کردن آی دی به جای ایندکس
df=df.set_index('CustomerID')
df


# In[93]:


df1=pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\cluster1 event var.csv')
df1


# In[94]:


event=df.columns


# In[95]:


del_event= [event[i] for i in range(len(event)) if df1['variance'][i]<=0.25]


# In[96]:


for i in range(len(del_event)):
    df.drop(del_event[i], axis=1, inplace=True)
df


# In[97]:


df.to_csv('cluster1 removing columns with low variance.csv')


# In[ ]:




