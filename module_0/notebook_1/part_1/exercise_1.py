#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:21:30 2018

@author: hunter
"""

#Exercise 1 (remove_all_test: 2 points). Complete the function remove_all(L, x) 
#so that, given a list L and a target value x, it returns a copy of the list 
#that excludes all occurrences of x but preserves the order of the remaining 
#elements. For instance:
#       remove_all([1, 2, 3, 2, 4, 8, 2], 2) == [1, 3, 4, 8]

#sample input for parameter L -> L = [1, 2, 3, 2, 4, 8, 2]
#sample input for parameter x -> x = 2

def remove_all(L, x):
    assert type(L) is list and x is not None
    #
    # YOUR CODE HERE
    #
    
    the_list = L[:]
    
    #while there is at least 1 occurence of x, continue to remove it from L
    while the_list.count(x) > 0:
        the_list.remove(x)
    
    return(the_list)