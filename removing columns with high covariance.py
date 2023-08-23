#!/usr/bin/env python
# coding: utf-8


import pandas as pd
import numpy as np


df = pd.read_csv('dataset.csv')
df


var=pd.read_csv('event var.csv')
var


corr=pd.read_csv('event covariance.csv')
corr



event=corr[corr.columns[0]]
event



var_forcomp=pd.DataFrame(columns=['Event','variance'])
var_forcomp



var_forcomp



var_forcomp[var_forcomp.columns[0]]



len (var_forcomp[var_forcomp.columns[0]])


for i in range(1,len(event)): 
    arr=corr[corr.columns[i]]
    a=np.percentile(arr, 25)  
    b=np.percentile(arr, 75)  
    del_event= [event[j] for j in range(len(event)) if arr[j]<=a or arr[j]>=b]  
    for k in range (len(del_event)):  
        for m in range(len(event)): 
            if var[var.columns[0]][m]==del_event[k]: 
                sereis=pd.Series(data=[var[var.columns[0]][m],var[var.columns[2]][m]], index=['Event','variance'])
                var_forcomp=var_forcomp.append(sereis,ignore_index=True) 
                del_event_=[] 
    for l in range(len (var_forcomp[var_forcomp.columns[0]])): 
        if var_forcomp[var_forcomp.columns[1]][l]<=var_forcomp[var_forcomp.columns[1]][i]:
            del_event_.append(var_forcomp[var_forcomp.columns[0]][l])
        else:
            del_event_.append(var_forcomp[var_forcomp.columns[0]][i]) 


del_event_


del_event_final=[]
for i in del_event_:
    if i not in del_event_final:
        del_event_final.append(i)
del_event_final


len(del_event_final)


for i in range(len(del_event_final)):
    df.drop(del_event_final[i], axis=1, inplace=True)
df


df.to_csv('feature selected.csv')



