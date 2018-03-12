#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:00:26 2018

@author: hunter
"""

#Exercise 7 (2 points). Implement the inverse of separate, which is unite. 
#This function should take a data frame (df), the set of columns to combine (cols), 
#the name of the new column (new_var), and a function that takes the subset of 
#the cols variables from a single observation. It should return a new value for that observation.


#sample input:
#table3_again = unite(tibble3, ['cases', 'population'], 'rate',
#                     combine=lambda x: str_join_elements(x, "/"))


def str_join_elements(x, sep="/"):
    assert type(sep) is str
    return sep.join([str(xi) for xi in x])

    

def unite(df, cols, new_var, combine=str_join_elements):
    # Hint: http://stackoverflow.com/questions/13331698/how-to-apply-a-function-to-two-columns-of-pandas-dataframe
    #
    # YOUR CODE HERE
    #
    
    #rate = df.apply(str_join_elements, axis = 1)
    
    df['rate'] = df[['cases','population']].apply(str_join_elements, axis=1)
    
    df = df.drop(['cases', 'population'], axis=1)
    
    #display(df)
    
    return(df)


