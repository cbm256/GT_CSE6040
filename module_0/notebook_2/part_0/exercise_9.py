#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:23:29 2018

@author: hunter
"""

#Exercise 9 (intersect_keys_test: 2 points). Write a function that, given two 
#dictionaries, finds the intersection of their keys.

#sample input: d1 and d2 are both dictionaries (likely with some common keys)

from collections import defaultdict

def intersect_keys(d1, d2):
    assert type(d1) is dict or type(d1) is defaultdict
    assert type(d2) is dict or type(d2) is defaultdict
    #
    # YOUR CODE HERE
    #

    #create sets of the keys from d1 and d2
    keys_1 = set(d1.keys())
    keys_2 = set(d2.keys())
    # & operator means set intersection
    keys_intersection = keys_1 & keys_2
    
    return(keys_intersection)