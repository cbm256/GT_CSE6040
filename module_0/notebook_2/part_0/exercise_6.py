#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 21:07:43 2018

@author: hunter
"""

#Exercise 6 (filter_rules_by_conf_test: 2 points). Given tables of item-pair 
#counts and individual item counts, as well as a confidence threshold, return 
#the rules that meet the threshold. The returned rules should be in the form of 
#a dictionary whose key is the tuple,  (a,b)  corresponding to the rule  a⇒>b,
#and whose value is the confidence of the rule,  conf(a⇒>b).
#You may assume that if  (a,b) is in the table of item-pair counts, then both 
#a and b are in the table of individual item counts.


"""
sample input:
pair_counts = {('man', 'woman'): 5,
               ('bird', 'bee'): 3,
               ('red fish', 'blue fish'): 7}

item_counts = {'man': 7,
               'bird': 9,
               'red fish': 11}

threshold = .5
    
"""

def filter_rules_by_conf (pair_counts, item_counts, threshold):
    rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    #
    # YOUR CODE HERE
    #
    
    #strategy in the code: for each key pair_count, find how often each 
    #pair occurs.  Next, find how oftern the first item in pair_counts occurred,
    #then divide pair_count by the number of occurences of the first item, and 
    #compare this ratio to the threshold
    
    for i , j in pair_counts:
        #number of occurences of the pair i,j in pair_counts
        temp_pair_count = pair_counts[(i, j)]
        
        #number of occurences of the item i in item_counts
        temp_item_count = item_counts[i]
        
        #confidence level of i => j
        temp_conf = temp_pair_count / temp_item_count  
    
        #check if temp_conf meets the confidence threshold
        if temp_conf >= threshold :
            #if it does meet this level, add it to rules
            rules[(i, j)] = temp_conf
    
    return rules