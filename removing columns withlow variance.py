#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np


df = pd.read_csv('dataset.csv')
df
df=df.set_index('CustomerID')
df



df1=pd.read_csv('event var.csv')
df1


event=df.columns

del_event= [event[i] for i in range(len(event)) if df1['variance'][i]<=0.25]

for i in range(len(del_event)):
    df.drop(del_event[i], axis=1, inplace=True)
df



df.to_csv('removing columns with low variance.csv')




