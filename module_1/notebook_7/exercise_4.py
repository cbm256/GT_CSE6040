#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 21:53:47 2018

@author: hunter
"""

#Exercise 4 (1 point). Write a function, tibbles_are_equivalent(A, B) to 
#determine if two tibbles, A and B, are equivalent. "Equivalent" means 
#that A and B have identical variables and observations, up to permutations. 
#If A and B are equivalent, then the function should return True. Otherwise, 
#it should return False.

#The last condition, "up to permutations," means that the variables and 
#observations might not appear in the table in the same order. For example, the 
#following two tibbles are equivalent:



def tibbles_are_equivalent(A, B):
    """Given two tidy tables ('tibbles'), returns True iff they are
    equivalent.
    """
    #
    # YOUR CODE HERE
    #
    
    
    
    #first make copies of the tibbles
    A_copy = A.copy()
    B_copy = B.copy()
    
    #next, sort both data frames in canonical order (except for row labels)
    A_canon = canonicalize_tibble(A_copy)
    B_canon = canonicalize_tibble(B_copy)
    
    #check if they are the same using the all function
    if A_canon.equals(B_canon) == True:
        return(True)
    else:
        return(False)