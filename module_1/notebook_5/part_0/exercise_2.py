#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 17:22:35 2018

@author: hunter
"""

#Exercise 2 (2 points). Write a function to parse US phone numbers written in 
#the canonical "(404) 555-1212" format, i.e., a three-digit area code enclosed 
#in parentheses followed by a seven-digit local number in three-hyphen-four digit 
#format. It should also ignore all leading and trailing spaces, as well as any 
#spaces that appear between the area code and local numbers. However, it should 
#not accept any spaces in the area code (e.g., in '(404)') nor should it in 
#the seven-digit local number.  It should return a triple of strings, 
#(area_code, first_three, last_four).
#If the input is not a valid phone number, it should raise a ValueError.


#import regular expression
import re

def parse_phone1 (s):
    #
    # YOUR CODE HERE
    #
    
    #remove leading and whitespace trailing characters
    s = s.strip()
     
    try:
        phone_pattern = re.compile ("""
        ^                               # beginning of string
        \(                              # first parentheses character 
        (?P<area_code>[\d {3}]+)        # area code
        \)                              # followed by ) 
        (?P<first_three>[\d {3}]+)      # first_three
        \-                              # followed by hyphe  -
        (?P<last_four>[\d {4}]+)        # last_four
        $                               # end of string
        
        """
        ,
        re.VERBOSE)
        
        area_code = (phone_pattern.match (s).group ('area_code'))
        first_three = (phone_pattern.match (s).group ('first_three')) 
        last_four = (phone_pattern.match (s).group ('last_four'))
        
        
        #remove possible leading characters before first_three (space between 
        #the area code and the first three numbers) but not trailing spaces
        first_three = first_three.lstrip()
        
        #check that all cases are the correct lenght (ie check for white space)
        if len(area_code) != 3 or len(first_three) != 3 or len(last_four) !=4:
            raise ValueError('wrong format')
        else:
            return(area_code, first_three, last_four)
        return(area_code)
        
    except AttributeError:
        raise ValueError('wrong format')
    
    
    