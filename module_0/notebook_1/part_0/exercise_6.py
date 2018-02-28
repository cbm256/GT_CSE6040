#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 17:54:16 2018

@author: hunter
"""

#Exercise 6 (report_exam_avg_test: 1 point). Let a, b, and c represent three 
#exam scores as numerical values. Complete the function, 
#report_exam_avg(a, b, c) so that it computes the average score (equally weighted) 
#and returns the string, 'Your average score is: XX', where XX is the average 
#rounded to one decimal place. For example:

#sample input for a,b,c ->  a = 100, b = 80, c = 95

def report_exam_avg(a, b, c):
    #assert is_number(a) and is_number(b) and is_number(c)
    #
    # YOUR CODE HERE
    #
    
    #find the average score
    average_score = (a + b + c) / 3
    
    #round to 1 decimal place
    average_score = round(average_score,1)
    
    #turn average_score into a string
    average_score_string = str(average_score)
    
    #concatenate strings
    output_string = "Your average score: " + average_score_string
    #return answer
    return(output_string)