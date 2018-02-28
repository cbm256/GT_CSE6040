#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 20:15:00 2018

@author: hunter
"""

#Exercise 0 (minmax_test: 1 point). Complete the function minmax(L), which takes 
#a list L and returns a pair---that is, 2-element Python tuple, 
#or "2-tuple"---whose first element is the minimum value in the list and whose 
#second element is the maximum. For instance:

#sample input for L -> L = [8, 7, 2, 5, 1]

def minmax(L):
    assert hasattr(L, "__iter__")
    #
    # YOUR CODE HERE
    #
    
    #find the min element
    min_element = min(L)
    #find the max element
    max_element = max(L)
    
    #create the tuple containing the min and max element
    min_and_max = (min_element, max_element)
    
    #return the answer
    return(min_and_max)