# -*- coding: utf-8 -*-
"""
Created on Fri May 15 04:44:48 2020

@author: arjin aydemir
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")

df.plot()
plt.show()
df=df.drop("SNo",axis=1)

df.plot()
df.show()