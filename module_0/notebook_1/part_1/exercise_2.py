#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 21:10:35 2018

@author: hunter
"""

#Exercise 2 (compress_vector_test: 2 points). Suppose you are given a vector, x, 
#containing real values that are mostly zero. For instance:
#    x = [0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]

#Complete the function, compress_vector(x), so that returns a dictionary d with 
#two keys, d['inds'] and d['vals'], which are lists that indicate the position 
#and value of all the non-zero entries of x. 

#sample inpute for parameter x ->  x = [0.0, 0.87, 0.0, 0.0, 0.0, 0.32, 0.46, 0.0, 0.0, 0.10, 0.0, 0.0]

def compress_vector(x):
    #assert type(x) is list
    #d = {'inds': [], 'vals': []}
    #
    # YOUR CODE HERE
    #
    
    #create empty lists
    inds_list = []
    vals_list = []


    #determine the number of elements in the list
    num_vals = len(x)
    
    for i in range(0 , num_vals):
        if x[i] != 0 :
            inds_list.append(i)
            vals_list.append(x[i])

    #print(inds_list)            
    #append the lists to the dictionary
    value_dic = {"inds" : inds_list, "vals" : vals_list}
    return(value_dic)
