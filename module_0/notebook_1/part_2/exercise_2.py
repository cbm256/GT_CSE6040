#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:02:12 2018

@author: hunter
"""

#Exercise 2 (grade_lists_test: 1 point). Write some code to compute a new 
#dictionary, named grade_lists, that maps names of students to lists of their 
#exam grades. The grades should be converted from strings to integers. 
#For instance, grade_lists['Thorny'] == [100, 90, 80].

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

#create a copy of list
popped_grades = grades[:]

#remove first list in grades (index 0)
popped_grades.pop(0)

#find how many lists we have
num_lists = len(popped_grades)

#find how many elements are in each list
num_elements = len(popped_grades[0])


#convert the elements of the list which may be converted into ints into ints
#using try except
for i in range(0 , num_lists):
    for j in range(0 , num_elements):
        try:
            popped_grades[i][j] = int(popped_grades[i][j])
        except:
            popped_grades[i][j] = popped_grades[i][j] 
        
#print(popped_grades)

#create the dictionary named grade_lists
grade_lists = {t[0]:t[1:] for t in popped_grades}



