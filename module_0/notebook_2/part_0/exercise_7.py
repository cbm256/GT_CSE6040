#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 22:50:24 2018

@author: hunter
"""

#Exercise 7 (find_assoc_rules_test: 3 points). Using the building blocks you 
#implemented above, complete a function find_assoc_rules so that it implements 
#the basic association rule mining algorithm and returns a dictionary of rules.

#In particular, your implementation may assume the following:
#1. As indicated in its signature, below, the function takes two inputs: 
#   receipts and threshold.
#2. The input, receipts, is a collection of itemsets: for every receipt r in 
#   receipts, r may be treated as a collection of unique items.
#3. The input threshold is the minimum desired confidence value. That is, the 
#   function should only return rules whose confidence is at least threshold.
#The returned dictionary, rules, should be keyed by tuples  (a,b)
#corresponding to the rule  a⇒b; each value should the the confidence conf(a⇒b)
#of the rule.



"""
sample input: 
receipts = [set('abbc'), set('ac'),set('a')]
threshold = .6
"""


from collections import defaultdict
from itertools import permutations

def find_assoc_rules(receipts, threshold):
    #
    # YOUR CODE HERE
    #
    
#-------------------functions called within find_assoc_rules-------------------
    #pair_counts is a defaultdict and itemset is a set of strings
    #this function updates how often pair of letters occurs
    def update_pair_counts (pair_counts, itemset):
        #loop through each element i in itemset
        for i , j in permutations(itemset, 2):
        #print(i,j)
            pair_counts[(i,j)] += 1
        return(pair_counts)
        
    
    #item_counts is a defaultdict and itemset is a set of strings
    #this function updates how often each letter occurs
    def update_item_counts(item_counts, itemset):
        #loop through each element i itemset
        for i in itemset:
            item_counts[i] += 1
        return(item_counts)
      
    #see exercise_6 for explanation    
    def filter_rules_by_conf (pair_counts, item_counts, threshold):
        rules = {} # (item_a, item_b) -> conf (item_a => item_b)
    
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
#------------------------------------------------------------------------------ 
    
    
    #create the default dicts which will be updated in the funcitons above
    pairs_count_dict = defaultdict(int)
    items_count_dict = defaultdict(int)
    
    for i in receipts:
        #rules_dict is updated iteratively here through the function update_pair_counts
        pairs_count_dict = update_pair_counts(pairs_count_dict, i)
        
        #items_dict is updated iteratively here through the function update_item_counts
        items_count_dict = update_item_counts(items_count_dict, i)
    
    
    #call filter_rules_by_conf to only include relationships which meet the
    #confidence threshold
    rules_dict = filter_rules_by_conf(pairs_count_dict, items_count_dict, threshold)
    
    return(rules_dict)
    