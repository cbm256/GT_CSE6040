#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:09:34 2018

@author: hunter
"""

#Exercise 11: Your task. (basket_rules_test: 4 points). Your final task in this 
#notebook is to mine this dataset for pairwise association rules. In particular, 
#your code should produce (no pun intended!) a final dictionary, basket_rules, 
#that meet these conditions (read carefully!):

#1.  The keys are pairs (a,b), where a and  b are item names (as strings)
#2.  The values are the corresponding confidence scores, conf(a => b)
#3.  Only include rules  a => b where item  a occurs at least MIN_COUNT times
#    and conf(a => b) is at least THRESHOLD.

#Each line of groceries_file is some customer's shopping basket. The items that the 
#customer bought are stored as a comma-separated list of values.


#sample input parameters for find_assoc_rules
#input_string = groceries_file  (created below)
#threshold = .6
#min_count = 10



import requests
response = requests.get ('https://cse6040.gatech.edu/datasets/groceries.csv')
groceries_file = response.text  # or response.content for raw bytes

print (groceries_file[0:250] + "...\n... (etc.) ...") # Prints the first 250 characters only



    
#import necessary modules    
from collections import defaultdict
from itertools import permutations
    
#-------------------functions called within find_assoc_rules-------------------
#------------------------------------------------------------------------------
#to begin solving this problem, we will first turn groceries_file 
#into a list of sets
def strings_to_list_of_sets(input_string):
    #first, groceries_file is turned into a list of strings, where each line of of
    #input_string is one element of the list
    list_of_strings = str.splitlines(input_string)
    
    #each element of groceries_string_list is turned into set, with ',' used
    #as a delimiter
    #find the length of wordlist_of_strings
    num_strings = len(list_of_strings)
        
    #create a copy of words that will become the list of sets
    list_of_sets = list_of_strings[:]
        
    #iterate through each string (word) in the list called words 
    for i in range(0 , num_strings):
        temp_string = list_of_strings[i]
        #set turns a string into a set of unique words
        list_of_sets[i] = set(temp_string.split(","))
        
    return(list_of_sets)


#pair_counts is a defaultdict and itemset is a set of strings
#this function updates how often pair of letters occurs
def update_pair_counts (pair_counts, itemset):
    #loop through each element i in itemset
    for i , j in permutations(itemset, 2):
    #print(i,j)
        pair_counts[(i,j)] += 1
    return(pair_counts)
    

#item_counts is a defaultdict and itemset is a set of strings
#this function updates how often each item occurs
def update_item_counts(item_counts, itemset):
    #loop through each element i itemset
    for i in itemset:
        item_counts[i] += 1
    return(item_counts)
  
#see exercise_6 for explanation    
def filter_rules_by_conf_and_count (pair_counts, item_counts, threshold, min_count):
    conf_rules = {} # (item_a, item_b) -> conf (item_a => item_b)

    for i , j in pair_counts:
        #number of occurences of the pair i,j in pair_counts
        temp_pair_count = pair_counts[(i, j)]
        
        #number of occurences of the item i in item_counts
        temp_item_count = item_counts[i]
        
        #confidence level of i => j
        temp_conf = temp_pair_count / temp_item_count  
        
        #check if temp_conf meets the confidence threshold
        if temp_conf >= threshold and temp_item_count >= min_count:
            #if it does meet this level, add it to rules
            conf_rules[(i, j)] = temp_conf
            
    return conf_rules



#------------------------------------------------------------------------------ 
def find_assoc_rules(input_string, threshold, min_count):
    #
    # YOUR CODE HERE
    #
    
    receipts = strings_to_list_of_sets(input_string = input_string)
    
    
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
    rules_dict = filter_rules_by_conf_and_count(pairs_count_dict, items_count_dict, threshold, min_count)
    
    return(rules_dict)
    
    
