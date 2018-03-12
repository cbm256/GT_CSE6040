#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:12:46 2018

@author: hunter
"""

#Exercise 9 (5 points). Starting from your who2 data frame, create a new tibble, 
#who3, for which each 'key' value is split into three new variables:
#* 'type', to hold the TB type, having possible values of rel, ep, sn, and sp;
#* 'gender', to hold the gender as a string having possible values of female and male; and
#* 'age_group', to hold the age group as a string having possible values of 0-14, 15-24, 25-34, 35-44, 45-54, 55-64, and 65+.
#The input data file is large enough that your solution might take a minute to run. 
#But if it appears to be taking much more than that, you may want to revisit your approach.


#
# YOUR CODE HERE
#
import re

def whosplitter(text):
    m = re.match("^new_?(rel|ep|sn|sp)_(f|m)(\\d{2,4})$", text)
    if m is None or len(m.groups()) != 3:
        return(['','',''])
    
    fields = list(m.groups())
    if fields[1] == 'f':
        fields[1] = 'female'
    elif fields[1] == 'm':
        fields[1] = 'male'
        
    if fields[2] == '014':
        fields[2] = '0-14'
    elif fields[2] == '65':
        fields[2] = '65+'
    elif len(fields[2]) == 4 and fields[2].isdigit():
        fields[2] = fields[2][0:2] + '-' + fields[2][2:4]
    
    return(fields)
    
who3 = separate(df = who2, key = 'case_type', into = ['type','gender','age_group'], splitter=whosplitter)

    

      
        