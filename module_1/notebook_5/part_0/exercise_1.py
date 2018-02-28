#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 14:31:09 2018

@author: hunter
"""

#for this exercise, let's use the following simplified rules for email addresses:
#We will restrict our attention to ASCII addresses and ignore Unicode. 
#-An email address has two parts, the username and the domain name. 
#    These are separated by an @ character.
#-A username must begin with an alphabetic character. It may be followed by any 
#    number of additional alphanumeric characters or any of the following special 
#    characters: . (period), - (hyphen), _ (underscore), or + (plus).
#-A domain name must end with an alphabetic character. It may consist of any of 
#   the following characters: alphanumeric characters, . (period), - (hyphen), or _ (underscore).
#-Alphabetic characters may be uppercase or lowercase.
#-No whitespace characters are allowed.


#Exercise 1 (2 points). Write a function parse_email that, given an email 
#address s, returns a tuple, (user-id, domain) corresponding to the user name 
#and domain name. For instance, given richie@cc.gatech.edu it should 
#return (richie, cc.gatech.edu).
#Your function should parse the email only if it exactly matches the email 
#specification. For example, if there are leading or trailing spaces, the 
#function should not match those. See the test cases for examples.
#If the input is not a valid email address, the function should raise a ValueError.

#import regular expression
import re

def parse_email(s):
    """Parses a string as an email address, returning an (id, domain) pair."""
    #
    # YOUR CODE HERE
    #
    
    email_pattern = re.compile ("""
    ^                                       # beginning of string
    (?P<user_name>[\w \- \. \+ \_ ]+)       # user name
    @                                       # followed bvy @ 
    (?P<domain_name>[\w \- \. \_ ]+)        # domain name
    $                                       # end of string
    
    """
    ,
    re.VERBOSE)
  
    #try and except ValueError (wrong input format)
    try:
        user_name = (email_pattern.match (s).group ('user_name'))
        domain_name = (email_pattern.match (s).group ('domain_name')) 
        
        #check if there are any spaces
        if ' ' in user_name or ' ' in domain_name:
            raise ValueError
        #make sure user_name begins with alphabetic character and domain_name
        #ends with alphabetic character
        first_char = user_name[0]
        last_char = domain_name[-1]
        if first_char.isalpha() != True or last_char.isalpha() != True:
            raise ValueError('wrong format')
            
        return(user_name, domain_name)
            
            
            
    except AttributeError:
        raise ValueError('wrong format')
    
   

    
    