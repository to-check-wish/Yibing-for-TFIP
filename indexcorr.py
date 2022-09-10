#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
import seaborn as sns
import matplotlib.pyplot as plt
 

data_train_set = pd.read_csv("/Volumes/U_WHU_2T/indextotal/indexmerge.csv")
data_train_set.head()
d = data_train_set.corr()

plt.subplots(figsize = (12,12))
sns.heatmap(d,annot = True,vmax = 1,square = True,cmap = "Reds")
plt.show()

