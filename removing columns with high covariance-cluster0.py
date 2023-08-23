#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# # cluster0

# In[23]:


df = pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\cluster0 removing columns with low variance.csv')
df


# In[24]:


var=pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\cluster0 event var.csv')
var


# In[25]:


corr=pd.read_csv('C:\\Users\\Administrator\\thesis\\BPI Challenge 2016\\feature selection\\covariance cluster0.csv')
corr


# In[26]:


#استخراج آرایه ای از ایونت ها
#event=corr.columnsستون اول رو هم میده که نمیخوام
event=corr[corr.columns[0]]
event


# In[27]:


var_forcomp=pd.DataFrame(columns=['Event','variance'])
var_forcomp


# In[28]:


var_forcomp


# In[29]:


var_forcomp[var_forcomp.columns[0]]


# In[30]:


len (var_forcomp[var_forcomp.columns[0]])


# In[31]:


for i in range(1,len(event)): # فور که به تعداد ستون های دیتا فریم crr ران بشه
    arr=corr[corr.columns[i]] #یک آرایه ای از ستون iام ماتریس کرولیشن تشکیل میدیم
    a=np.percentile(arr, 25)  #چارک اول ستون
    b=np.percentile(arr, 75)  # چارک دوم ستون
    del_event= [event[j] for j in range(len(event)) if arr[j]<=a or arr[j]>=b] # آرایه ای از تمامی ایونت هایی در آرایه arr که بین چارک اول و سوم قرار ندارند
    for k in range (len(del_event)):# فور به تعداد ایونت های داخل آرایه del_event ران بشه 
        for m in range(len(event)): # فور به تعداد سطر های دیتافریم corr ران بشه
            if var[var.columns[0]][m]==del_event[k]: #میاد بررسی میکنه هر کدوم از سطر های دیتافریم corr برابر با کامپوننت های آرایه del_event بودن
                sereis=pd.Series(data=[var[var.columns[0]][m],var[var.columns[2]][m]], index=['Event','variance'])
                var_forcomp=var_forcomp.append(sereis,ignore_index=True) # اینجا دیتا فریم بالا رو با مقادیر پر میکنه
                del_event_=[] # یک آرایه خالی تشکیلی میدیم تا هر کدون از ایونت های موجود در آرایه del_event واریانس کمتری داشت بریزه این تو
    for l in range(len (var_forcomp[var_forcomp.columns[0]])): # فور به تعداد سطرهای دیتافریم واریانس های ایونت هایی که برای بررسی انتخا شدن ران میشه
        if var_forcomp[var_forcomp.columns[1]][l]<=var_forcomp[var_forcomp.columns[1]][i]:# بررسی میکنه واراینس هر ایونت آیا بیشتر از واریانس ستون 
            del_event_.append(var_forcomp[var_forcomp.columns[0]][l])
        else:
            del_event_.append(var_forcomp[var_forcomp.columns[0]][i]) 


# In[32]:


del_event_


# In[33]:


del_event_final=[]
for i in del_event_:
    if i not in del_event_final:
        del_event_final.append(i)
del_event_final


# In[34]:


len(del_event_final)


# In[35]:


for i in range(len(del_event_final)):
    df.drop(del_event_final[i], axis=1, inplace=True)
df


# In[36]:


df.to_csv('cluster0 feature selected.csv')


# In[268]:


#corr.columns[1]


# In[269]:


#var[var.columns[2]][0]


# In[270]:


#arr=corr[corr.columns[1]]
#a=np.percentile(arr, 25)
#b=np.percentile(arr, 75)
#del_event= [event[j] for j in range(len(event)) if arr[j]<=a or arr[j]>=b]
#for k in range (len(del_event)):
 #   for n in range(len(event)):
  #      if var[var.columns[0]][n]==del_event[k]:
   #         sereis=pd.Series(data=[var[var.columns[0]][n],var[var.columns[2]][n]], index=['Event','variance'])
    #        var_forcomp=var_forcomp.append(sereis,ignore_index=True)
#var_forcomp


# In[271]:


#A=['a','b']
#A.append('c')


# In[272]:


#A


# In[273]:


#A.append('d')


# In[274]:


#var[var.columns[0]][0]


# In[275]:


#del_event_=[]
#for i in range(len(del_event)):
   # if var[var.columns[2]][0]>var[var.columns[2]][i]:
    #    del_event_.append(var[var.columns[0]][i])
#del_event_


# In[276]:


#var.drop(index=var[var['Event']=='Question'].index, inplace=True)
#var


# In[277]:


#var.drop(['Mean'])


# In[278]:


#استخراج مقادیر هر ستون
#arr=corr[corr.columns[1]]
#arr


# In[279]:


#np.percentile(arr, 90)


# In[280]:


#range(1,len(event))


# In[281]:


#event[0]


# In[282]:


#a=np.percentile(arr, 25)
#b=np.percentile(arr, 75)
#del_event_vardf= [event[j] for j in range(len(event)) if arr[j]>a and arr[j]<b]
#del_event_vardf[1]


# In[283]:


#var['Event']==del_event_vardf[1]


# In[284]:


#var[var.columns[0]][0]


# In[285]:


#var[var.columns[0]][1]


# In[286]:


#var[var.columns[0]]


# In[287]:


#del_event_vardf


# In[288]:


#sereis=pd.Series(data=[var[var.columns[0]][1],var[var.columns[2]][1]], index=['Event','variance'])
#sereis


# In[289]:


#sereis=pd.Series(data=[var[var.columns[0]][1],var[var.columns[2]][1]], index=['Event','variance'])
#var_forcomp=var_forcomp.append(sereis,ignore_index=True)
#var_forcomp


# In[290]:


#sereis=pd.Series(data=[var[var.columns[0]][2],var[var.columns[2]][2]], index=['Event','variance'])
#var_forcomp=var_forcomp.append(sereis,ignore_index=True)
#var_forcomp


# In[291]:


#arr=corr[corr.columns[1]]
#a=np.percentile(arr, 25)
#b=np.percentile(arr, 75)
#del_event_vardf= [event[j] for j in range(len(event)) if arr[j]>a and arr[j]<b]
#for k in range (len(del_event_vardf)):
 #   for n in range(len(event)):
  #      if var[var.columns[0]][n]==del_event_vardf[k]:


# In[292]:


#arr=corr[corr.columns[1]]
#a=np.percentile(arr, 25)
#b=np.percentile(arr, 75)
#del_event_vardf= [event[j] for j in range(len(event)) if arr[j]>a and arr[j]<b]
#for k in range (len(del_event_vardf)):
 #   for n in range(len(event)):
  #      if var[var.columns[0]][n]==del_event_vardf[k]:
   #         var.drop(index=n, inplace=True)
    #        n=n-1
            
#var


# In[293]:


#arr=corr[corr.columns[1]]
#a=np.percentile(arr, 25)
#b=np.percentile(arr, 75)
#del_event_vardf= [event[j] for j in range(len(event)) if arr[j]>a and arr[j]<b]
#for k in range (len(del_event_vardf)):
#    var.drop(index=var[var['Event']==del_event_vardf[k]].index, inplace=True)
#var


# In[294]:


#var.drop(index=var[var['Event']=='Question'].index, inplace=True)
#var


# In[295]:


#arr=corr[corr.columns[1]]
#a=np.percentile(arr, 25)
#b=np.percentile(arr, 75)
#del_event_vardf= [event[j] for j in range(len(event)) if arr[j]>=a or arr[j]<=b]
#for k in range (len(del_event_vardf)):
 #   for m in range(len(event)):
  #      var_new=var.drop(index=var[var['Event']==del_event_vardf[k]].index, inplace=True)
#var
#del_event=[event[j] for j in range(len(event)) if arr[j]<=a or arr[j]>=b]
#del_event


# In[296]:


#len(del_event)


# In[ ]:




