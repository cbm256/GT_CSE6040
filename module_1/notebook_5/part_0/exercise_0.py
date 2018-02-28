#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb  2 18:08:29 2018

@author: hunter
"""

#Exercise 0 (1 point). Create a new function that checks whether a given input 
#string is a properly formatted social security number, i.e., has the pattern, 
#XXX-XX-XXXX, including the separator dashes, where each X is a digit. It should 
#return True if so or False otherwise.

#sample input s = '123-45-6789', s = 'abc-12-3456', s = '123 - 23 - 4356'


def is_ssn(s):
    #
    # YOUR CODE HERE
    #
    
    #first, check if ssn is the correct length
    if len(s) != 11:
        return(False)
    
    
    #find the 3 number sections
    part_1 = s[0:3]
    part_2 = s[4:6] 
    part_3 = s[7:11]  
    
    #find the two dashes
    dash_1 = s[3]
    dash_2 = s[6]
    
    
    #check that part_1, part_2, and part_3 are numeric
    if part_1.isnumeric() != True or part_2.isnumeric() != True or part_3.isnumeric() != True:
        print(part_1,part_2,part_3)
        return(False)
    
    #check that dash_1 and dash_2 == '1'
    if dash_1 != '-' or dash_2 != '-' :
        return(False)
    else:
        return(True)

    
    
    
