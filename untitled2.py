# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 01:08:13 2020

@author: arjin aydemir
"""

import pandas as pd
import numpy as np
import matplotlib as plt
data = pd.read_csv('covid_19_data.csv',sep=";")
data=data.apply(lambda x:x.str.replace(".","."))


data['Confirmed'].median()
plot.show()
