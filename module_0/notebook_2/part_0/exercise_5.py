#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 18:50:47 2018

@author: hunter
"""

#Exercise 5 (update_item_counts_test: 2 points). Implement a procedure that, 
#given an itemset, updates a table to track counts of each item.
#As with the previous exercise, you may assume all items in the given itemset 
#(itemset) are distinct, i.e., that you may treat it as you would any set-like 
#collection. You may also assume the table (item_counts) is a default dictionary.

#sample input for pair_counts: sample_item_counts = defaultdict(int) 
#sample input for itemset:  sample_itemset = set("error")


def update_item_counts(item_counts, itemset):
    #
    # YOUR CODE HERE
    #
    
    #loop through each element i itemset
    for i in itemset:
        item_counts[i] += 1
    
    return(item_counts)
