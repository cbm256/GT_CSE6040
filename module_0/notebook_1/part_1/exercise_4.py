#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 13:02:02 2018

@author: hunter
"""

#Exercise 4  Suppose you are given two compressed vectors, d1 and d2, each represented as 
#described in exercises 2 and 3 and possibly with repeated indices. Complete the function
#find_common_inds(d1, d2) so that it returns a list of the indices they have in common.

#sample input for parameters d1 and d2
#d1 == {'inds': [9, 9, 1, 9, 8, 1], 'vals': [0.28, 0.84, 0.71, 0.03, 0.04, 0.75]}
#d2 == {'inds': [0, 9, 9, 1, 3, 3, 9], 'vals': [0.26, 0.06, 0.46, 0.58, 0.42, 0.21, 0.53, 0.76]}

def find_common_inds(d1, d2):
    assert type(d1) is dict and 'inds' in d1 and 'vals' in d1
    assert type(d2) is dict and 'inds' in d2 and 'vals' in d2
    #
    # YOUR CODE HERE
    #
    
    #create lists of indices d1 and d2
    d1_ind_list = d1['inds']
    d2_ind_list = d2['inds']
    common_indices = list(set(d1_ind_list).intersection(d2_ind_list))
    
    return(common_indices)