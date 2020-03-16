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

conf.Lat.describe()
conf.Lat = conf.Lat.astype(float)
