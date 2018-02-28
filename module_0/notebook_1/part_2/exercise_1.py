#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 22:34:01 2018

@author: hunter
"""

#Exercise 1 (assignments_test: 1 point). Write some code to compute a new 
#list named assignments[:], to hold the names of the class assignments. 
#(These appear in the descriptive header element of grades.)

grades = [
    # First line is descriptive header. Subsequent lines hold data
    ['Student', 'Exam 1', 'Exam 2', 'Exam 3'],
    ['Thorny', '100', '90', '80'],
    ['Mac', '88', '99', '111'],
    ['Farva', '45', '56', '67'],
    ['Rabbit', '59', '61', '67'],
    ['Ursula', '73', '79', '83'],
    ['Foster', '89', '97', '101']
]


#find the of elements in each list
num_elements = len(grades[0])

#preallocate a list called assignments
assignments = []

for i in range(1 , num_elements):
    assignments.append(grades[0][i])
    












