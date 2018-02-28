#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:44:03 2018

@author: hunter
"""

# Generate `latin_rules`:
#
# YOUR CODE HERE
#

#sample input for parameter input_text -> latin_text (defined in exercise_1)
#sample input for parameter threshold -> threshold = .5


#import the regular expression module 're'
import re
from collections import defaultdict
from itertools import combinations # Hint!
from itertools import permutations

def pairwise_text_miner(input_text, threshold):
#-------------------------------all subfunctions-------------------------------
    #create the function 
    def normalize_string(s):
        assert type (s) is str
        #
        # YOUR CODE HERE
        #
        
        #first, make the string s all lower case
        lower_string = s.lower()
    
        #remove all non-alphanumeric data (except spaces)
        stripped = re.sub(r'([^\s\w]|_)+', '', lower_string)
        
        
        #remove all numeric data
        normalized_text = re.sub(r'[0-9]+', '', stripped)
        
        return(normalized_text)
        
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
        
        
#------------------------------end of all subfunctions-------------------------
      
        
    #normalize the text
    normalized_string = normalize_string(input_text)
    
    #get list of normalized words
    normal_words_list = get_normalized_words(normalized_string)
    
    #get sets of individual letters of each word
    normalized_sets = make_itemsets(normal_words_list)
    
    #find all relationships of letter pairs that pass the threshold
    association_rules = find_assoc_rules(normalized_sets, threshold)
    
    return(association_rules)