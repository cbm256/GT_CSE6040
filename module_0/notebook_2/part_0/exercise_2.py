#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 19:00:00 2018

@author: hunter
"""

#Exercise 2 (get_normalized_words_test: 1 point). Implement the following 
#function, get_normalized_words(s): given a string (str object) s, returns a 
#list of its words, normalized per the definition of normalize_string().


#sample input for parameter s -> output of exercise_1 (normalized latin text)

def get_normalized_words(s):
    assert type (s) is str
    #
    # YOUR CODE HERE
    #
    
    #split the words and create the list
    #word_list = re.sub("[^\w]", " ",  s).split()
    
    #split the string into a list of strings
    word_list = s.split()
    
    return(word_list)