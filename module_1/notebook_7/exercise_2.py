#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:01:38 2018

@author: hunter
"""

#------------------------------NOT MY CODE!!-----------------------------------

A_csv = """country,year,cases
Afghanistan,1999,745
Brazil,1999,37737
China,1999,212258
Afghanistan,2000,2666
Brazil,2000,80488
China,2000,213766"""

with StringIO(A_csv) as fp:
    A = pd.read_csv(fp)
print("=== A ===")
display(A)


B_csv = """country,year,population
Afghanistan,1999,19987071
Brazil,1999,172006362
China,1999,1272915272
Afghanistan,2000,20595360
Brazil,2000,174504898
China,2000,1280428583"""


with StringIO(B_csv) as fp:
    B = pd.read_csv(fp)
print("\n=== B ===")
display(B)


C = A.merge(B, on=['country', 'year'])
print("\n=== C = merge(A, B) ===")
display(C)


#------------------- G is the input for calc_prevalence!!----------------------

G = C.copy()
G['year'] = G['year'].apply(lambda x: "'{:02d}".format(x % 100))
display(G)


#------------------------QUESTION STARTS HERE----------------------------------

#Exercise 2 (2 points). Suppose you wish to compute the prevalence, which is the 
#ratio of cases to the population.
#The simplest way to do it is as follows:
#    G['prevalence'] = G['cases'] / G['population']
#However, for this exercise, try to figure out how to use apply() to do it instead. 
#To figure that out, you'll need to consult the documentation for apply() 
#or go online to find some hints.
#Implement your solution in a function, calc_prevalence(G), which given G returns 
#a new copy H that has a column named 'prevalence' holding the correctly 
#computed prevalence values.
#Note 0. The emphasis on "new copy" is there to remind you that your function 
#        should not modify the input dataframe, G.
#Note 1. Although there is the easy solution above, the purpose of this exercise 
#        is to force you to learn more about how apply() works, so that you 
#        can "apply" it in more settings in the future.


#-------------------------MY CODE STARTS HERE----------------------------------
def calc_prevalence(G):
    assert 'cases' in G.columns and 'population' in G.columns
    #
    # YOUR CODE HERE
    #
    
    H = G.copy()
    
    def prevalence(x, y):
        return x / y
    
    H['prevalence'] = H.apply(lambda x: prevalence(x['cases'], x['population']), axis=1)
    
    return(H)

