#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 12:23:53 2020

@author: ap
"""

import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame as df

a = pd.read_csv('vwnd_00z-mly.csv',names = ["PLACE", "Year", "Month", "Pressure","wind speed","days taken"],delim_whitespace=True)
a.head()
a.tail()
a = a[(a['Year']<=2020) &(a['Year']>=2015)]
a = a[(a['Month']<=3)|(a['Month']==12)]
a = a.reset_index(drop=True)
a.describe()

######################################################################################################
#CONVERT THE DATAFRAMES INTO ARRAY AGAIN BEFORE USING HERE OR WILL GIVE ERROR
######################################################################################################
ID = []
LATITUDE= []
LONGITUDE= []
ELEVATION= []
NAME= []
FSTYEAR  = []
LSTYEAR  = []
NOBS = []
DATA = []
def input():
    i_file = open("igra2-station-list.txt","r")
    #o_file = open("out.csv","w")
    #o_file.write("ID,LATITUDE,LONGITUDE,ELEVATION,NAME,FSTYEAR,LSTYEAR,NOBS\n")
    for line in i_file.readlines():
        ID.append(line[0:11])
        LATITUDE.append(float(line[12:20]))
        LONGITUDE.append(float(line[21:30]))
        ELEVATION.append(float(line[31:37]))
        #STATE=line[38:39]
        NAME.append(line[41:72])  
        FSTYEAR.append(int(line[72:77])) 
        LSTYEAR.append(int(line[77:82]))   
        NOBS.append((line[82:88]))  
        #o_file.write("{},{},{},{},{},{},{},{}\n".format(ID,LATITUDE,LONGITUDE,ELEVATION,NAME,FSTYEAR,LSTYEAR,NOBS))
        
input()    
   
def pos(id_s):
    for i in range(len(ID)):

        if(ID[i]== id_s):
            return i;
    return -1        
#print(pos('AEM00041217'))
long_add = []
lat_add = []
elev_add = []        
for i in a["PLACE"]:
    p = pos(i)
    long_add.append(LONGITUDE[p])
    lat_add.append(LATITUDE[p])
    elev_add.append(ELEVATION[p])
   
a["LONGITUDE"]= long_add
a["LATITUDE"]= lat_add
a["ELEVATION"]= elev_add           


######################################################################################################
#CONVERT THE DATAFRAMES INTO ARRAY AGAIN BEFORE USING HERE OR WILL GIVE ERROR
######################################################################################################
conf_2019 = pd.read_csv('time_series-2019-ncov-Confirmed.csv')
conf_data = pd.DataFrame()
conf_data["LONGITUDE"] = conf_2019['Long']
conf_data["LATITUDE"] = conf_2019['Lat']
conf_data["COUNT"] = conf_2019['3/15/20']
elev_data = []
wind_data = []
pressure_data=[]

def elev(long,lat):
    c = 1;
    elev_sum = 0;
    wind_sum = 0;
    pressure_sum = 0;
    for i in range(len(a['PLACE'])):
        if((abs(a["LONGITUDE"][i]-long)<=5)and(abs(a["LATITUDE"][i]-lat)<=5)):
            c = c + 1
            elev_sum = elev_sum + a["ELEVATION"][i]
            wind_sum = wind_sum + a["wind speed"][i]
            pressure_sum = pressure_sum + a["Pressure"][i]
    elev_data.append(elev_sum/c)
    wind_data.append(wind_sum/c)
    pressure_data.append(pressure_sum/c)
    
for i in range (len(conf_data['COUNT'])):
    elev(conf_data["LONGITUDE"][i],conf_data["LATITUDE"][i])
 
conf_data["pressure"]= pressure_data
conf_data["wind speed"]= wind_data
conf_data["ELEVATION"]= elev_data      
conf_data.to_csv('conf_data.csv', encoding='utf-8', index=True)   
conf_data = conf_data[(conf_data.pressure != 0)]    
conf_data = conf_data.reset_index(drop=True)    

plt.scatter(conf_data["ELE"],conf_data["COUNT"]) 
plt.ylim(-300,300)  
#plt.yscale('log') 
plt.show()           
            
            