#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:57:11 2018

@author: hunter
"""

#Basic tidying transformations: Melting and casting
#Given a data set and a target set of variables, there are at least two common 
#issues that require tidying.


#-------------------------------Melting----------------------------------------
#First, values often appear as columns. Table 4a is an example. To tidy up, you 
#want to turn columns into rows:

#Exercise 5 (4 points). Implement the melt operation as a function,
    
#def melt(df, col_vals, key, value):
        
#It should take the following arguments:
#df: the input data frame, e.g., table4 in the example above;
#col_vals: a list of the column names that will serve as values;
#key: name of the new variable, e.g., year in the example above;
#value: name of the column to hold the values.
#You may need to refer to the Pandas documentation to figure out how to create 
#and manipulate tables. The bits related to indexing and merging may be especially helpful.


#sample input:
table4a = pd.read_csv('table4a.csv')
print("\n=== table4a ===")
display(table4a)

#melt_4a = melt(table4a, col_vals=['1999','2000'], key = 'year', value = 'cases')



def melt(df, col_vals, key, value):
    assert type(df) is pd.DataFrame
    #
    # YOUR CODE HERE
    #
    
    #col_vals will be melted
    
    #get the names of the columns that we want to keep
    #returns the columns in the dataframe that are NOT in col_vals:
    keep_vars = df.columns.difference(col_vals)
    
    #next, create an empty datafram
    melted_sections = []
    
    
    #loop through col_vals
    for i in col_vals:
        melted_i = df[keep_vars].copy()
        melted_i[key] = i
        melted_i[value] = df[i]
        melted_sections.append(melted_i)
    
    melted = pd.concat(melted_sections)
    return(melted)
        
        


