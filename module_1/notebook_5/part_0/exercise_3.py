#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 19:41:16 2018

@author: hunter
"""

#Exercise 3 (3 points). Implement an enhanced phone number parser that can 
#handle any of these patterns.
#(404) 555-1212  case 1
#(404) 5551212   case 2
#404-555-1212    case 3
#404-5551212     case 4
#404555-1212     case 5
#4045551212      case 6


#import regular expression
import re

def parse_phone2 (s):
    #
    # YOUR CODE HERE
    #
    
    phone_pattern_1 = re.compile ("""
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
        
    phone_pattern_2 = re.compile ("""
        ^                               # beginning of string
        \(                              # first parentheses character 
        (?P<area_code>[\d {3}]+)        # area code
        \)                              # followed by ) 
        (?P<last_seven>[\d {7}]+)       # last seven
        $                               # end of string
        
        """
        ,
        re.VERBOSE)
        
        
    phone_pattern_3 = re.compile ("""
        ^                               # beginning of string
        (?P<area_code>[\d {3}]+)        # area code
        \-                              # followed by -
        (?P<first_three>[\d {3}]+)      # first_three
        \-                              # followed by hyphe  -
        (?P<last_four>[\d {4}]+)        # last_four
        $                               # end of string
        
        """
        ,
        re.VERBOSE)
    
        
    phone_pattern_4_5 = re.compile ("""
        ^                               # beginning of string
        (?P<first_part>[\d]+)           # first part
        \-                              # followed by -
        (?P<last_part>[\d]+)         # last part
        $
        
        """
        ,
        re.VERBOSE)

    
    phone_pattern_6 = re.compile ("""
        ^                               # beginning of string
        (?P<all_ten>[\d {9}]+)          # all_ten
        $
        
        """
        ,
        re.VERBOSE)




    #remove leading and whitespace trailing characters
    s = s.strip()
    
    #case 1
    try:
        area_code = (phone_pattern_1.match (s).group ('area_code'))
        first_three = (phone_pattern_1.match (s).group ('first_three')) 
        last_four = (phone_pattern_1.match (s).group ('last_four'))
        
        
        #remove possible leading characters before first_three (space between 
        #the area code and the first three numbers) but not trailing spaces
        first_three = first_three.lstrip()
        
        #check that all cases are the correct lenght (ie check for white space)
        if len(area_code) != 3 or len(first_three) != 3 or len(last_four) !=4:
            raise ValueError('wrong format')
        else:
            return(area_code, first_three, last_four)
    except AttributeError:
        pass
    
    
    #case 2
    try:
        area_code = (phone_pattern_2.match (s).group ('area_code'))
        last_seven = (phone_pattern_2.match (s).group ('last_seven')) 
        
        #remove possible leading characters before first_three (space between 
        #the area code and the first three numbers) but not trailing spaces
        last_seven = last_seven.lstrip()

                #check that all cases are the correct lenght (ie check for white space)
        if len(area_code) != 3 or len(last_seven) != 7:
            raise ValueError('wrong format')
        else:
            first_three = last_seven[:3]
            last_four = last_seven[3:]
            return(area_code, first_three, last_four)
    except AttributeError:
        pass
     
    
    #case 3        
    try:
        area_code = (phone_pattern_3.match (s).group ('area_code'))
        first_three = (phone_pattern_3.match (s).group ('first_three')) 
        last_four = (phone_pattern_3.match (s).group ('last_four'))
        
        #check that all cases are the correct lenght (ie check for white space)
        if len(area_code) != 3 or len(first_three) != 3 or len(last_four) !=4:
            raise ValueError('wrong format')
        else:
            return(area_code, first_three, last_four)
    except AttributeError:
        pass      
    
    
    #case 4 and 5       
    try:
        first_part = (phone_pattern_4_5.match (s).group ('first_part'))
        last_part = (phone_pattern_4_5.match (s).group ('last_part')) 
        

        #check that all cases are the correct lenght (ie check for white space)
        if len(first_part) == 3 and len(last_part) == 7:
            area_code = first_part
            first_three = last_part[:3]
            last_four = last_part[3:]
            return(area_code, first_three, last_four)
        elif len(first_part) == 6 and len(last_part) == 4:
            area_code = first_part[:3]
            first_three = first_part[3:]
            last_four = last_part  
            return(area_code, first_three, last_four)
        else:
            raise ValueError('wrong format')

    except AttributeError:
        pass

    #case 5        
    try:
        all_ten = (phone_pattern_6.match (s).group ('all_ten'))

        #check for correct length
        if len(all_ten) != 10: 
            raise ValueError('wrong format')
        else:
            area_code = all_ten[:3]
            first_three = all_ten[3:6]
            last_four = all_ten[6:]
            return(area_code, first_three, last_four)
    except AttributeError:
        raise ValueError('wrong format')
        
        
        
        
        
        