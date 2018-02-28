#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 23 00:28:07 2018

@author: hunter
"""

#Exercise 10 (common_high_conf_rules_test: 1 points). Let's consider any rules 
#with a confidence of at least 0.75 to be a "high-confidence rule."
#Write some code that finds all high-confidence rules appearing in both the 
#Latin text and the English text. Store your result in a list named 
#common_high_conf_rules whose elements are  (a,b) 
#pairs corresponding to the rules  a⇒b

#sample_input for text_1 -> latin_text from exercise_1
#sample_input for text_2 -> english_text
#threshold = .6


english_text = """
But I must explain to you how all this mistaken idea
of denouncing of a pleasure and praising pain was
born and I will give you a complete account of the
system, and expound the actual teachings of the great
explorer of the truth, the master-builder of human
happiness. No one rejects, dislikes, or avoids
pleasure itself, because it is pleasure, but because
those who do not know how to pursue pleasure
rationally encounter consequences that are extremely
painful. Nor again is there anyone who loves or
pursues or desires to obtain pain of itself, because
it is pain, but occasionally circumstances occur in
which toil and pain can procure him some great
pleasure. To take a trivial example, which of us
ever undertakes laborious physical exercise, except
to obtain some advantage from it? But who has any
right to find fault with a man who chooses to enjoy
a pleasure that has no annoying consequences, or
one who avoids a pain that produces no resultant
pleasure?

On the other hand, we denounce with righteous
indignation and dislike men who are so beguiled and
demoralized by the charms of pleasure of the moment,
so blinded by desire, that they cannot foresee the
pain and trouble that are bound to ensue; and equal
blame belongs to those who fail in their duty
through weakness of will, which is the same as
saying through shrinking from toil and pain. These
cases are perfectly simple and easy to distinguish.
In a free hour, when our power of choice is
untrammeled and when nothing prevents our being
able to do what we like best, every pleasure is to
be welcomed and every pain avoided. But in certain
circumstances and owing to the claims of duty or
the obligations of business it will frequently
occur that pleasures have to be repudiated and
annoyances accepted. The wise man therefore always
holds in these matters to this principle of
selection: he rejects pleasures to secure other
greater pleasures, or else he endures pains to
avoid worse pains.
"""

#here pairwise_text_miner from exercise_8 and intersect_keys from exercise_9
#are called (so be sure to source those functions before running this one)
#also the variable latin_text, defined in exercise_1 and exercise_8 is used


#latin_text and english_text will be called in the function 

#this function returns the intersection of relationships which meet the 
#threshold in two seperate pieces of text
def confidence_intersect(text_1, text_2, threshold):
    
    #find the relationships in text_1 and text_2 which meet the threshold
    text_rules_1 = pairwise_text_miner(text_1, threshold)
    text_rules_2 = pairwise_text_miner(text_2, threshold)
    
    
    #find the intersection of relationships between the two texts which 
    #both meet the minimum threshold
    
    intersect_rules = intersect_keys(text_rules_1, text_rules_2)
    
    return(intersect_rules)
    
    
    
    
    
    
    
    
    