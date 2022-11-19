# -*- coding: utf-8 -*-
"""
Created on Sat Nov 19 00:17:00 2022

@author: khaled-alahamd


"""

import pandas as pd
import numpy as np
sheet="Sheet1"
file_excel="assignment 1.xlsx"
df = pd.read_excel(file_excel,sheet_name=sheet)

x=df.iloc[:,2:9]
y=df.iloc[:,11]
    
df["Minuts"]=df.iloc[:,2:9].sum(axis=1)
print(df["Minuts"])

arg=[]
i=0
for col in x.values:
    for row in col:
        if row==0:
            i=i+1
    arg.append(i)
    i=0
df['absentDays']=arg
print(df['absentDays'])
    