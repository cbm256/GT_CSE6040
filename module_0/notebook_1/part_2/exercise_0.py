#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 17 20:39:25 2018

@author: hunter
"""

#Consider the following dataset of exam grades, organized as a 2-D table and 
#stored in Python as a "list of lists" under the variable name, grades

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

#Exercise 0 (students_test: 1 point). Write some code that computes a new list 
#named students[:], which holds the names of the students as they from 
#"top to bottom" in the table.

#find the number of students
num_students = len(grades)
students = []

#append the names to the students list (remembering that python is 0-indexed)
#note that we start with list 1 (not 0) since list 0 is a list of labels
for i in range(1 , num_students):
    #fill in the element of the list with the student's name
    students.append(grades[i][0])

    
#return(students)
    
    