#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jan 22 13:57:57 2018

@author: hunter
"""

#Exercise 4 (update_pair_counts_test: 2 points). Start by implementing a 
#function that enumerates all item-pairs within an itemset and updates a 
#table in-place that tracks the counts of those item-pairs.
#You may assume all items in the given itemset (itemset argument) are distinct, 
#i.e., that you may treat it as you would any set-like collection. You may also 
#assume pair_counts is a default dictionary.


#sample input for pair_counts: sample_pair_counts = defaultdict(int)
#sample input for itemset:  sample_itemset = set("error")


from collections import defaultdict
from itertools import combinations # Hint!
from itertools import permutations

def update_pair_counts (pair_counts, itemset):
    """
    Updates a dictionary of pair counts for
    all pairs of items in a given itemset.
    """
    assert type (pair_counts) is defaultdict

    #
    # YOUR CODE HERE
    #
    
    #combinations(itemset, 2) returns all of the 2 pair combinations
    #loop through each pair i,j in combinations(itemset, 2)
    for i , j in combinations(itemset, 2):
        #print(i,j)
        #this assures that we count (i,j) and (j,i) separetely (essentially as permutations)
        #we count how often every pair (i,j) and (j,i) occurs
        pair_counts[(i, j)] += 1
        pair_counts[(j, i)] += 1
    
    return(pair_counts)
    
    
    """
    #this could also work, but it was specified we should use combinations
    for i , j in permutations(itemset, 2):
        #print(i,j)
        pair_counts[(i,j)] += 1
    return(pair_counts)
    """