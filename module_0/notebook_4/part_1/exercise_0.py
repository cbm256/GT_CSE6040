#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  1 15:06:41 2018

@author: hunter
"""
#Exercise 0 (2 points). In the code cell below, we've defined a list,
#    N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]
#Take each entry N[i] to be a problem size.
#Let t[:len(N)] be a list, which will hold computed sums.
#For each N[i], run an experiment where you sum a list of values x[:N[i]] using 
#alg_sum(). You should initialize x[:] so that all elements have the value 0.1. 
#Store the computed sum in t[i].


#alg_sum sample input: x = [0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01, 0.01]


def alg_sum(x): # x == x[:n]
    s = 0.
    for x_i in x: # x_0, x_1, \ldots, x_{n-1}
        s += x_i
    return s



N = [10, 100, 1000, 10000, 100000, 1000000, 10000000]

# Initialize an array t of size len(N) to all zeroes.
t = [0.0] * len(N)  

# Your code should do the experiment described above for
# each problem size N[i], and store the computed sum in t[i].

#
# YOUR CODE HERE
#

#alg_sum will be called iteratively
counter = 0
for i in N:
    #initialize the list of N[i] 0.1's 
    temp_x = [0.1] * i

    #call alg_sum iteratively
    t[counter] = alg_sum(temp_x)
    
    counter = counter + 1
    

print(t)


