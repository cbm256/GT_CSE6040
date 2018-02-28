#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 11 10:35:47 2018

@author: hunter
"""



#Exercise 3  Complete the function decompress_vector(d) that takes a compressed vector d, 
#which is a dictionary with keys for the indices (inds) and values (vals), and 
#returns the corresponding full vector. For any repeated index, the values 
#should be summed.  The function should accept an optional parameter, n, that 
#specifies the length of the full vector. You may assume this length is 
#at least max(d['inds'])+1.

#if an indice is missing, populate it with 0.  If n exceeds max(d["inds"]), 
#populate additional indices with 0.


#sample input for parameter d ->
#   d = {}
#   d['inds'] = [0, 3, 7, 3, 4, 3]
#   d['vals'] = [1.0, 2.0, 3.0, 4.0, 5.0, 6.0]


def decompress_vector(d, n=None):
    # Checks the input
    assert type(d) is dict and 'inds' in d and 'vals' in d, "Not a dictionary or missing keys"
    assert type(d['inds']) is list and type(d['vals']) is list, "Not a list"
    assert len(d['inds']) == len(d['vals']), "Length mismatch"
    
    # Determine length of the full vector
    i_max = max(d['inds']) if d['inds'] else -1
    if n is None:
        n = i_max+1
    else:
        assert n > i_max, "Bad value for full vector length"
        
    #
    # YOUR CODE HERE
    #
    
    #make individual lists from the the dictionary of lists
    inds_list = d['inds']
    vals_list = d['vals']
    
    #create a vector length n populated with 0's (takes care of 0's at the end)
    decompressed_vector = [0] * n
    
    #find the length of inds_list
    inds_len = len(inds_list)
    
    #loop through vals_list
    for i in range(0 , inds_len):
        #find the current indecy number
        temp_inds_val = inds_list[i]
        #add the corresponding value to the corresponding indecy of decompressed_vector
        decompressed_vector[temp_inds_val] = vals_list[i] + decompressed_vector[temp_inds_val]
    
    return(decompressed_vector)
    
    
    
    