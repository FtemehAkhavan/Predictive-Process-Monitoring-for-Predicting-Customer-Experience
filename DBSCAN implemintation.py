#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import DBSCAN
from matplotlib import pyplot as plt
import seaborn as sns
sns.set()
from numpy import where
from numpy import unique
from sklearn.datasets import make_classification
from sklearn.metrics import silhouette_samples, silhouette_score
from sklearn. cluster import KMeans
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


df = pd.read_csv('D:\\M.Sc\\thesis\\VM backup\\14010421\\code\\BPI Challenge 2016\\encoding\\frq based\\Frequency based encodingBPI2016-merged data.csv')
df


# In[89]:


ID = sorted(df[df.columns[0]].unique())
ID


# In[90]:


#جایگذاری کردن آی دی به جای ایندکس
df=df.set_index('CustomerID')
df


# In[91]:


sum_of_columns=df.sum(axis=0)
sum_of_cols=pd.DataFrame(sum_of_columns,columns=['frequency'])
sum_of_cols


# In[92]:


sum_of_cols=sum_of_cols.sort_values(by='frequency',axis=0)
sum_of_cols


# In[93]:


x=df.values
x


# In[ ]:


db= DBSCAN(eps=247,min_samples=4).fit(x)
core_sampels_mask=np.zeros_like(db.labels_,dtype=bool)
core_sampels_mask[db.core_sample_indices_]=True
labels=db.labels_
dbscan_clstrs = unique(labels)
#print(set(labels))
n_clusters_=len(dbscan_clstrs)
n_noise_=list(labels).count(-1)
print('number of clusters: %d' % n_clusters_)
print('number of noise points: %d' % n_noise_)


# In[ ]:


index_cluster=pd.DataFrame(columns=['index','cluster'])
index_cluster


# In[ ]:


len(labels)


# In[7]:


#خروجی اکسل از کلاسترها
for j in range (len(dbscan_clstrs)):
    for i in range (len(labels)):
        if labels[i] == dbscan_clstrs[j]:
            index_cluster=index_cluster.append({'index':ID[i],'cluster':dbscan_clstrs[j]},ignore_index=True)
        #    a=[i,dbscan_clstrs[j]]
         #   index_cluster.append(a)
            
  #  index = where(dbscan_res == dbscan_clstr)
   # a=[index,dbscan_clstr]
 #   index_cluster.append(a)
index_cluster


# In[8]:


index_cluster.to_csv('index_cluster.csv')


# In[32]:


get_ipython().run_line_magic('matplotlib', 'inline')
plt.rcParams['figure.figsize']=(10,6)
plt.rcParams['figure.dpi']=150


# In[35]:


dbscan_clstrs


# In[85]:


#نمودار سه بعدی کلاستر ها
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
xs = df.values[:,13]
ys = df.values[:,42]
zs = df.values[:,39]
ax.scatter(xs, ys, zs, c=labels, cmap= "Spectral")#plt.cm.get_cmap("cool",4))
#Spectral
cbar=plt.colorbar(ax.scatter(xs, ys, zs, c=labels, cmap="Spectral"), extend="both", pad=0.08)#, shrink=0.5)
cbar.set_ticks([-1,0,1,2])
#ax.legend(labels, loc= 'upper right')
ax.set_xlabel('The first most frequent page')
ax.set_ylabel('The second most frequent page')
ax.set_zlabel('The third most frequent page')
ax.view_init(45,135)
plt.show()


# In[ ]:


#اضافه کردن ستون کلاستر به ماتریس کدگذاری شده برمبنای تکرار

