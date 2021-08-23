#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 22 21:17:48 2021

@author: yunji
"""

import matplotlib.pyplot as plt
from matplotlib import rc
import seaborn as sns
import pandas as pd


df_infection = pd.read_csv("/Users/yunji/infection.csv")
df_death=pd.read_csv("/Users/yunji/death.csv")


df = pd.concat([df_infection[['date','cumCasesBySpecimenDate']],df_death['cumDeaths28DaysByDeathDate']],axis=1)


df = df.iloc[::-1].reset_index(drop=True)


fig, ax = plt.subplots(1,1,figsize=(8,8))
g = df[['date','cumCasesBySpecimenDate']].plot.line(ax=ax,color='red')
ax.set_xticklabels([])
ax = ax.twinx()
df[['date','cumDeaths28DaysByDeathDate']].plot.line(ax=ax,color='blue')
ax.set_title('cumCasesBySpecimenDate vs cumDeaths28DaysByDeathDate')
plt.show()