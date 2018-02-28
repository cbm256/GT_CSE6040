#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:29:37 2018

@author: hunter
"""

#Exercise 3 (strcat_list_test: 2 points). Complete the following function, 
#strcat_list(L), which generalizes the previous function: given a list of 
#strings, L[:], returns the concatenation of the strings in reverse order. 
#For example:  strcat_list(['abc', 'def', 'ghi']) == 'ghidefabc'

#sample input for L -> L = ['abc', 'def', 'ghi']


#reverse the order of a list of strings, then concatenate all items of the list
def strcat_list(L):
    assert type(L) is list
    #
    # YOUR CODE HERE
    #
    
    #reverse the order of the list
    reverse_list = L[::-1]
    #concatenate the strings
    reverse_concat = ''.join(reverse_list)
    #return the output
    return(reverse_concat)

