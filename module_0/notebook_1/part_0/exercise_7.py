#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 18:20:02 2018

@author: hunter
"""

#3Exercise 7 (count_word_lengths_test: 2 points). Write a function 
#count_word_lengths(s) that, given a string consisting of words separated by 
#spaces, returns a list containing the length of each word. Words will consist 
#of lowercase alphabetic characters, and they may be separated by multiple 
#consecutive spaces. If a string is empty or has no spaces, the function should 
#return an empty list.

#sample input for parameter s -> s = 'the quick  brown   fox jumped over     the lazy  dog'


def count_word_lengths(s):
    assert all([x.isalpha() or x == ' ' for x in s])
    assert type(s) is str
    #
    # YOUR CODE HERE
    #
    
    #the split function returns a list of words of a string, separated by
    #white space
    split_words = s.split() 
    #the map function applies a function to every item of an iterable and 
    # a list of the values is returned
    word_lengths = list(map(len, split_words))
    
    return(word_lengths)
    
    
    
    