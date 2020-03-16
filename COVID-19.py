#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 12:49:06 2020

@author: ap
"""
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame as df

conf_2019 = pd.read_csv('time_series-2019-ncov-Confirmed.csv')
dead_2019 = pd.read_csv('time_series-2019-ncov-Death.csv')
rec_2019 = pd.read_csv('time_series-2019-ncov-Recovered.csv')

conf = pd.read_csv('time_series-ncov-Confirmed.csv')[1:]
dead = pd.read_csv('time_series-ncov-Deaths.csv')[1:]
rec = pd.read_csv('time_series-ncov-Recovered.csv')[1:]


############################################################################################################################
#ANALYSING CONFIRMED CASES
############################################################################################################################
conf.Value = conf.Value.astype(float)
conf.Long = conf.Long.astype(float)
conf.Lat = conf.Lat.astype(float)
conf_mod = conf[(conf['Value']>1)]
#********************************************
points = plt.scatter(conf_mod.Long,conf_mod.Lat, c=conf_mod.Value, lw=0)
plt.colorbar(points)
plt.show()
#********************************************
    #-----------------------------
    #LATITUDE
    #-----------------------------
conf.Lat.describe()
sns.distplot(conf.Lat)
conf.Lat.value_counts()
pd.crosstab(conf.Lat, columns = 'count' , normalize = True)
sns.countplot(conf.Lat)
sns.boxplot( x = 'Lat' , y = 'Value', data = conf)
plt.hist(conf.Lat ,conf.Value, bin = 10)
# Most confirmed cases between Latitude 20 to 60
plt.scatter(conf.Long,conf.Lat)
    #-----------------------------
    #VALUES
    #-----------------------------
conf.Lat.describe()
sns.distplot(conf.Lat)
conf.Lat.value_counts()
pd.crosstab(conf.Lat, columns = 'count' , normalize = True)
sns.countplot(conf.Lat)
sns.boxplot( x = 'Lat' , y = 'Value', data = conf)
plt.hist(conf.Lat ,conf.Value, bin = 10)