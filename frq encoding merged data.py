#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import numpy as np


df = pd.read_csv('dataset.csv',parse_dates=['TIMESTAMP'])
df

df.drop(['Unnamed: 0','ContactTimeEnd'], axis=1, inplace= True)
df


df1= df.sort_values(['CustomerID','TIMESTAMP'],ascending=True)
df1



df2=pd.DataFrame(df.groupby(['CustomerID','Event'])['Event'].count())
df2.rename({'Event':'count'}, axis=1, inplace=True)
df2


df2.to_csv('group by dataset.csv')




df2 = pd.read_csv('group by dataset.csv')
df2

np_array=df2.to_numpy()
np_array


ID = sorted(df[df2.columns[0]].unique())
ID


len(ID)


Event = sorted(df[df2.columns[1]].unique())
Event



len(Event)



df_Myans = pd.pivot_table(df2, values='count', index='CustomerID', columns='Event')
df_Myans



df_Myans=df_Myans.fillna(0)
df_Myans



df_Myans.to_csv('Frequency based encoding dataset.csv')



