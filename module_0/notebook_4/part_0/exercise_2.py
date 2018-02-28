#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 13:17:55 2018

@author: hunter
"""


#Exercise 2 (5 points). Write a function, fp_bin(v), that determines the 
#IEEE-754 tuple representation of any double-precision floating-point value, v. 
#That is, given the variable v such that type(v) is float, it should return a 
#tuple with three components, (s_sign, s_bin, v_exp) such that
#s_sign is a string representing the sign bit, encoded as either a '+' or '-' character;
#s_signif is the significand, which should be a string of 54 bits having the form, 
#x.xxx...x, where there are (at most) 53 x bits (0 or 1 values);
#v_exp is the value of the exponent and should be an integer.


#sample input:
#For example:
#    v = -1280.03125
#    assert v.hex() == '-0x1.4002000000000p+10'
#    assert fp_bin(v) == ('-', '1.0100000000000010000000000000000000000000000000000000', 10) 


#some subfunctions for parsing strings by character
def substring_after(the_string, delim_character):
    return the_string.partition(delim_character)[2]
    
def substring_before(the_string, delim_character):
    return the_string.partition(delim_character)[0]

def fp_bin(v):
    assert type(v) is float
#
# YOUR CODE HERE
#

    #find the hexadecimal representation of our number:
    hex_rep = v.hex()
        
#------------------------------------------------------------------------------
    #get a string version of the number (without the the '.')
    #get rid of the everything before the 'x' character hex_rep
    hex_number_string = substring_after(hex_rep,'x')

    #get rid of everything after the 'p' character from _
    hex_number_string = substring_before(hex_number_string, 'p')
    
    #remove the '.' from number_string (int() can't be used for a float with a defined base)
    hex_number_string = hex_number_string.replace('.', "")

#------------------------------------------------------------------------------
    #turn hex_number_string into a binary string (with a '.' in the second position)
    
    #get the string binary representation of hex_number_string 
    #[2:] at the end gets rid of 'ob' at the beginning which is normally returned
    binary_number_string = str(bin(int(hex_number_string, 16))[2:])
    
    #ensure the string will be 54 characters long by filling with '0' to the right
    #to represent more precision (we use 53 characters because the ','
    #added below will take up one more space)
    binary_number_string = binary_number_string.ljust(53, '0')
    
    #add the '.' into binary_number_string
    binary_number_string = binary_number_string[:1] + '.' + binary_number_string[1:]
    
    
#------------------------------------------------------------------------------
    
    #find the exponent (for scientific notation representation) from hex_rep
    #and convert it from string to int
    binary_exponent = int(substring_after(hex_rep,'p'))
    
    
        
    #check if the the hex_rep starts with a negative sign
    if hex_rep[0] == '-' :
        #assign the correct sign
        number_sign = '-'
    else :
        number_sign = '+'
        
#------------------------------------------------------------------------------
    #create tuple of correct output
    
    output_tuple = (number_sign, binary_number_string, binary_exponent)
    
    return(output_tuple)
    
