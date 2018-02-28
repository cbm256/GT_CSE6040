#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:19:34 2018

@author: hunter
"""

#Exercise 5 (ceiling_fraction_test: 1 point). Complete the function, 
#ceiling_fraction(a, b), which for any numeric inputs, a and b, corresponding 
#to real numbers,  a≥0 and  b>0, returns  ⌈a/b⌉, that is, the ceiling of a/b. 
#The type of the returned value must be int.

#sample input for a, and b -> a = 15.5 , b = 4


def ceiling_fraction(a, b):
#    assert is_number(a) and a >= 0
#    assert is_number(b) and b > 0
    #
    # YOUR CODE HERE
    #
    
    #we find the floor fraction of the opposite (always negative)
    #of the fraction, then find its opposite (always positive),
    #then make it an int
    ceiling_quotient = int(-(-a//b))
    
    #return the answer
    return(ceiling_quotient)