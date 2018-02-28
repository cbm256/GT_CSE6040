#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 21 20:14:54 2018

@author: hunter
"""

#Exercise 3 (make_itemsets_test: 2 points). Implement a function, 
#make_itemsets, that given a list of strings converts the characters of each 
#string into an itemset, returning the list of itemsets.

#sample input for parameter words -> normalized list of strings from the 
# output of exercise_2


def make_itemsets(words):
    #
    # YOUR CODE HERE
    #
    
    #our input 'words' is a list of strings (words)
    
    #find the length of words
    num_words = len(words)
    
    #create a copy of words that will become the list of sets
    word_list_set = words[:]
    
    #iterate through each string (word) in the list called words 
    for i in range(0 , num_words):
        #set turns a string into a set of unique letters
        word_list_set[i] = set(words[i])
        
    return(word_list_set)
        
        
        
        
        
        
    