#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 20:43:57 2018

@author: hunter
"""

#Exercise 4 (2 points). Suppose you are given two binary floating-point values, 
#u and v, in the tuple form given above. That is, u == (u_sign, u_signif, u_exp) 
#and v == (v_sign, v_signif, v_exp), where the base for both u and v is two (2). 
#Complete the function add_fp_bin(u, v, signif_bits), so that it returns the 
#sum of these two values with the resulting significand truncated to signif_bits digits.

#Note 0: Assume that signif_bits includes the leading 1. For instance, suppose 
#signif_bits == 4. Then the significand will have the form, 1.xxx.

#Note 1: You may assume that u_signif and v_signif use signif_bits bits 
#(including the leading 1). Furthermore, you may assume each uses far fewer 
#bits than the underlying native floating-point type (float) does, so that 
#you can use native floating-point to compute intermediate values.

#Hint: The test cell above defines a function, fp_bin(v), which you can use to 
#convert a Python native floating-point value (i.e., type(v) is float) into a 
#binary tuple representation.



#we will perform this exercise using the functions defined inexercise_1, 
#exercise_2, and exercise_3

#sample input and output


#u = ('+', '1.010010', 0)
#v = ('-', '1.000000', -2)
#add_fp_bin(u,v,7) = ('+', '1.000010', 0)

#u = ('+', '1.00000', 0)
#v = ('+', '1.00000', -5)
#add_fp_bin(u,v,6) = ('+', '1.00001', 0)

#u = ('+', '1.00000', 0)
#v = ('-', '1.00000', -6)
#add_fp_bin(u,v,6) = ('+', '1.11111', -1)





def add_fp_bin(u, v, signif_bits):
    u_sign, u_signif, u_exp = u
    v_sign, v_signif, v_exp = v
    
    # You may assume normalized inputs at the given precision, `signif_bits`.
    #assert u_signif[:2] == '1.' and len(u_signif) == (signif_bits+1)
    #assert v_signif[:2] == '1.' and len(v_signif) == (signif_bits+1)
    
    #
    # YOUR CODE HERE
    #

    #first use eval_fp defined in exercise_ (and which calls the function
    #eval_strfrac() from exercise_1) to convert the binary tuples into floats
    float_1 = eval_fp(u_sign, u_signif, u_exp)
    float_2 = eval_fp(v_sign, v_signif, v_exp)

    #then, we find the sum of these floats
    the_sum = float_1 + float_2
    
    #return(the_sum)
    
    #next we find the binary tuple output by fp_bin() defined in exercise_2
    #when we use the_sum as an input parameter
    binary_tuple = fp_bin(the_sum)
    
    
    #collect the elements from binary_tuple
    the_sign = binary_tuple[0]
    the_signif = binary_tuple[1]
    the_exponent = binary_tuple[2]
    
    #update significand for correct number of signifcant places
    the_signif = the_signif[0:signif_bits+1]
    
    #update the new tuple
    updated_binary_tuple = (the_sign, the_signif, the_exponent)
    
    return(updated_binary_tuple)
    
    
    




