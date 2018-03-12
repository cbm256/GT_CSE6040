#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:46:24 2018

@author: hunter
"""


table3 = pd.read_csv('table3.csv')


#Exercise 6 (3 points). Write a function that takes a data frame (df) and 
#separates an existing column (key) into new variables (given by the list of new variable names, into).

#How will the separation happen? The caller should provide a function, splitter(x), 
#that given a value returns a list containing the components. Observe that the 
#partial solution below defines a default splitter, which uses the regular 
#expression, (\d+\.?\d+), to find all integer or floating-point values in a string input x.


#sample input:
table3 = pd.read_csv('table3.csv')
print('=== table3 ===')
display(table3)

#tibble3 = separate(table3, key = 'rate', into = ['cases','population'])



import re

def default_splitter(text):
    """Searches the given spring for all integer and floating-point
    values, returning them as a list _of strings_.
    
    E.g., the call
    
      default_splitter('Give me $10.52 in exchange for 91 kitten stickers.')
      
    will return ['10.52', '91'].
    """
    fields = re.findall('(\d+\.?\d+)', text)
    return fields

def separate(df, key, into, splitter=default_splitter):
    """Given a data frame, separates one of its columns, the key,
    into new variables.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns
    
    # Hint: http://stackoverflow.com/questions/16236684/apply-pandas-function-to-column-to-create-multiple-new-columns

    #
    # YOUR CODE HERE
    #
    
    #this function takes a string input and returns values in a panda series
    def apply_splitter(text):
        fields = splitter(text)
        return(pd.Series({into[i]:f for i, f in enumerate(fields)}))
    
    #variables that don't change
    fixed_vars = df.columns.difference([key])
    #copy of data frame at fixed variables
    tibble = df[fixed_vars].copy()
    #use apply_splitter to apply splitter to the key column
    tibble_extra = df[key].apply(apply_splitter)
    
    
    return(pd.concat([tibble, tibble_extra], axis = 1))

