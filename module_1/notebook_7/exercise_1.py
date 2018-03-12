#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 20:56:58 2018

@author: hunter
"""

#------------------------------NOT MY CODE!!-----------------------------------

# Some modules you'll need in this part
import pandas as pd
from io import StringIO
from IPython.display import display

# Ignore this line. It will be used later.
SAVE_APPLY = getattr(pd.DataFrame, 'apply')


#reading in the famous iris data set
irises = pd.read_csv('iris.csv')
print("=== Iris data set: {} rows x {} columns. ===".format(irises.shape[0], irises.shape[1]))
display (irises.head())

#Exercise 1 (ungraded). Run the following commands to understand what each one does. 
#If it's not obvious, try reading the Pandas documentation or going online to get more information.

irises.describe()
irises['sepal length'].head()
irises[["sepal length", "petal width"]].head()
irises.iloc[5:10]
irises[irises["sepal length"] > 5.0]
irises["sepal length"].max()
irises['species'].unique()
irises.sort_values(by="sepal length", ascending=False).head(1)
irises.sort_values(by="sepal length", ascending=False).iloc[5:10]
irises.sort_values(by="sepal length", ascending=False).loc[5:10]
irises['x'] = 3.14
irises.rename(columns={'species': 'type'})
del irises['x']