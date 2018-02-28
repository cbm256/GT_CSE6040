#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 14:28:50 2018

@author: hunter
"""

#Exercise 1 (3 points). Suppose a string of digits s in base base contains up to 
#one fractional point. Complete the function, eval_strfrac(s, base), so that it 
#returns its corresponding floating-point value. Your function should always 
#return a value of type float, even if the input happens to correspond to an exact integer.
#Examples:
#    eval_strfrac('3.14', base=10) ~= 3.14
#    eval_strfrac('100.101', base=2) == 4.625
#    eval_strfrac('f.a', base=16) == 15.625


def is_valid_strfrac(s, base=2):
    return all([is_valid_strdigit(c, base) for c in s if c != '.']) \
        and (len([c for c in s if c == '.']) <= 1)
    
def eval_strfrac(s, base=2):
    #assert is_valid_strfrac(s, base), "'{}' contains invalid digits for a base-{} number.".format(s, base)
    
    #
    # YOUR CODE HERE
    #
    
    #first, we will split the string into two parts, the part before and the 
    #part after the decimal place.
    split_string = s.split('.')
    
    if len(split_string) == 1 : 
        pre_decimal = split_string[0]
        post_decimal = '0'
    else :
        pre_decimal = split_string[0]
        post_decimal = split_string[1]
    
    
    #if we are using a base > 10 system, we will need to convert the non-numerical
    #digits to numbers (this is only applied to the decimal portion,
    #whole number portion is taken care of in pythons built in 'int' function)
    possible_digits = '0123456789abcdefghijklmnopqrstuvwxyz'
    
    #preallocate some numbers
    place_counter = -1
    post_decimal_number = 0
    
    
    #convert the decimal portion to base 10 
    for i in post_decimal:
        #we convert character later digits (for bases > 10) to 2 digit base 10
        #numbers by finding there indices in the possible_digits string
        temp_digit = possible_digits.find(i)
     #  print(temp_digit)
        post_decimal_number = int(temp_digit) * (base ** place_counter) + post_decimal_number
        #update place_counter
        place_counter = place_counter - 1
    
    print(pre_decimal)
    #convert whole number portion to base 10
    pre_digit_number = int(pre_decimal, base)
        
    #add the whole number and decimal portion together
    base_10_number = pre_digit_number + post_decimal_number
    
    return(base_10_number)
    

