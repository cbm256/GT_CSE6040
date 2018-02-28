#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 17:36:52 2018

@author: hunter
"""

#Exercise 3 (3 points). Suppose you are given a floating-point value in a base 
#given by base and in the form of the tuple, (sign, significand, exponent), where
#sign is either the character '+' if the value is positive and '-' otherwise;
#significand is a string representation in base-base;
#exponent is an integer representing the exponent value.
#Complete the function,
#def eval_fp(sign, significand, exponent, base):
#so that it converts the tuple into a numerical value (of type float) and returns it.


#sample input:
#eval_fp('+', '1.25000', -1, base=10) = 0.125

#------------------------------------------------------------------------------
#exercise_1 function eval_strfrac() is used as a subfunction in eval_fp
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
    
    #convert whole number portion to base 10
    pre_digit_number = int(pre_decimal, base)
        
    #add the whole number and decimal portion together
    base_10_number = pre_digit_number + post_decimal_number
    
    return(base_10_number)

#------------------------------------------------------------------------------


def eval_fp(sign, significand, exponent, base=2):
    assert sign in ['+', '-'], "Sign bit must be '+' or '-', not '{}'.".format(sign)
    #assert is_valid_strfrac(significand, base), "Invalid significand for base-{}: '{}'".format(base, significand)
    assert type(exponent) is int

    #
    # YOUR CODE HERE
    #

    #turn significand and exponent from strings into floats
    #significand = float(significand)
    exponent = int(exponent)
    
    
#------------------------------------------------------------------------------
    #convert out of scientific notation
    
    #first, remove the '.' from significand
    significand = significand.replace('.', "")
    #case of positive exponent:
    if exponent >= 0:         
        #convert significand out of scientific notation by moving the '.'
        #to the correct position (correct position = exponent + 1)
        the_number = significand[:exponent+1] + '.' + significand[exponent+1:]
    else:
        #find the number of '0's that should be appended to ghe beginning 
        #of the number
        abs_exponent = abs(exponent)
        num_zeros = abs_exponent - 1
        
        the_number = significand
        
        #case that we need to add zeros, we add zeros to the begining
        if num_zeros > 0 :
            for i in range(0, num_zeros):
                the_number = '0' + the_number
        
        #add '.' to the beginning
        the_number = '.' + the_number
        #return(the_number)
        #the_number = float(significand)*10**exponent
        #the_number = "%.50f" % the_number 

        
    #assign a leading 0 to the decimal string, if it begins with a '.'
    if the_number[0] == '.':
        the_number = '0' + the_number
    
    output_float = eval_strfrac(the_number, base=base)
    
    #make significand negative if sign is negative
    if sign == '-' :
        output_float = output_float * -1
    
    return(output_float)
    



