#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:10:58 2018

@author: hunter
"""

#Exercise 4 (floor_fraction_test: 1 point). Suppose you are given two variables, 
#a and b, whose values are the real numbers,  a≥0 (non-negative) and  b>0
#(positive). Complete the function, floor_fraction(a, b) so that it 
#returns ⌊a/b⌋, that is, the floor of  a/b. The type of the returned value must be int (an integer).

#sample input for a, and b -> a = 15.5 , b = 4

def is_number(x):
    """Returns `True` if `x` is a number-like type, e.g., `int`, `float`, `Decimal()`, ..."""
    from numbers import Number
    return isinstance(x, Number)
 
    
# Suppose you are given two variables, a and b, whose values are the real numbers,  a≥0
#(non-negative) and  b>0
#(positive). Complete the function, floor_fraction(a, b) so that it returns  ⌊ab⌋
#that is, the floor of  ab. The type of the returned value must be int (an integer).
    
def floor_fraction(a, b):
    assert is_number(a) and a >= 0
    assert is_number(b) and b > 0
    #
    # YOUR CODE HERE
    #
    
    # // is defined as floor quotient.  Then we make it a type int
    floor_quotient = int(a // b)
    
    #return floor_quotient
    return(floor_quotient)