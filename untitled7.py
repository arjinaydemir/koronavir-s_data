# -*- coding: utf-8 -*-
"""
Created on Fri May 15 04:49:54 2020

@author: arjin aydemir
"""

import pandas as pd
import matplotlib.pyplot as plt
df=pd.read_csv("covid_19_data.csv")


türkiye=df[df["Country/Region"]=="Turkey"]

İtalya=df[df["Country/Region"]=="Italy"]

Ispanya=df[df["Country/Region"]=="Spain"]


plt.hist(İtalya.Deaths,bins=10)
plt.xlabel("ölüm sayıları")
plt.ylabel("değer araları")
plt.title("Italya koronavirus analizi")
plt.show()

plt.hist(Ispanya.Deaths,bins=10)
plt.xlabel("ölüm sayıları")
plt.ylabel("değer araları")
plt.title("İspanya koronavirus analizi")
plt.show()
