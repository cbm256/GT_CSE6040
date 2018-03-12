#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:32:47 2018

@author: hunter
"""


import pandas as pd  # The suggested idiom
from io import StringIO

from IPython.display import display # For pretty-printing data frames

#Exercise 3 (3 points). Write a function, canonicalize_tibble(X), that, given 
#a tibble X, returns a new copy Y of X in canonical order. We say Y is in 
#canonical order if it has the following properties.
#The variables appear in sorted order by name, ascending from left to right.
#The rows appear in lexicographically sorted order by variable, ascending from top to bottom.
#The row labels (Y.index) go from 0 to n-1, where n is the number of observations.
#For instance, here is a non-canonical tibble .


#sample input:
## Test input
canonical_in_csv = """,c,a,b
2,hat,x,1
0,rat,y,4
3,cat,x,2
1,bat,x,2"""

def canonicalize_tibble(X):
    
    # Enforce Property 1:
    var_names = sorted(X.columns)
    Y = X[var_names].copy()

    
    #Enforce property 2:
    Y.sort_values(by = var_names, inplace = True)
    
        
    #enforce property 3:
    Y.set_index([list(range(0, len(Y)))], inplace = True)

    
    return(Y)


