#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 22:33:30 2018

@author: hunter
"""


#----------------------------------Casting-------------------------------------
#The second most common issue is that an observation might be split across 
#multiple rows. Table 2 is an example. To tidy up, you want to merge rows:

#Because this operation is the moral opposite of melting, and "rebuilds" 
#observations from parts, it is sometimes called casting.

#The signature of a cast is similar to that of melt. However, you only need to 
#know the key, which is column of the input table containing new variable names, 
#and the value, which is the column containing corresponding values.

#Exercise 6 (4 points). Implement a function to cast a data frame into a tibble, 
#given a key column containing new variable names and a value column containing the corresponding cells.
#We've given you a partial solution that
#verifies that the given key and value columns are actual columns of the input data frame;
#computes the list of columns, fixed_vars, that should remain unchanged; and
#initializes and empty tibble.
#Observe that we are asking your cast() to accept an optional parameter, join_how, 
#that may take the values 'outer' or 'inner' (with 'outer' as the default). 
#Why do you need such a parameter?


#sample input:
table2 = pd.read_csv('table2.csv')
print('=== table2 ===')
display(table2)

#tibble2 = cast(table2, 'type', 'count')



def cast(df, key, value, join_how='outer'):
    """Casts the input data frame into a tibble,
    given the key column and value column.
    """
    assert type(df) is pd.DataFrame
    assert key in df.columns and value in df.columns
    assert join_how in ['outer', 'inner']
    
    #column names that will stay the same
    fixed_vars = df.columns.difference([key, value])
    tibble = pd.DataFrame(columns=fixed_vars) # empty frame
    
    #
    # YOUR CODE HERE
    #
    
    new_vars = df[key].unique()
    for i in new_vars:
        df_i = df[df[key] == i]
        del df_i[key]
        df_i = df_i.rename(columns = {value:i})
        tibble = tibble.merge(df_i, on = list(fixed_vars), how = join_how)
        
    
    return(tibble)


