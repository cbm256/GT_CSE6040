#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 16:49:54 2018

@author: hunter
"""

#Exercise 6 (avg_grades_by_assignment_test: 1 point). Write some code to 
#compute a dictionary, avg_grades_by_assignment, which maps each exam to 
#its average score.

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

#first we transpose grades
grades_transposed = list(map(list, zip(*grades)))

#create a copy of list
popped_grades = grades_transposed[:]

#remove first list in grades (index 0)
popped_grades.pop(0)

#find how many lists we have
num_lists_popped = len(popped_grades)

#find how many elements are in each list
num_elements_popped = len(popped_grades[0])


#convert the elements of the list which may be converted into ints into ints
#using try except
for i in range(0 , num_lists_popped):
    for j in range(0 , num_elements_popped):
        try:
            popped_grades[i][j] = int(popped_grades[i][j])
        except:
            popped_grades[i][j] = popped_grades[i][j] 
        
#print(popped_grades)

#create the dictionary named grade_lists
grade_lists = {t[0]:t[1:] for t in popped_grades}

#find the number of lists in grades
num_lists = len(grades_transposed)

#find how many elements are in each list in grades
num_elements = len(grades_transposed[0])

#create avg_grades_by_assignment dictionary
avg_grades_by_assignment = {}

#find the average of each exam score
for k in range(1 , num_lists):
    #find the average of each list
    temp_average_score = sum(grade_lists[grades_transposed[k][0]]) / len(grade_lists[grades_transposed[k][0]])
    
    #find the corresponding exam name
    temp_exam = grades_transposed[k][0]
    
    #update the temp exam score dictionary
    #temp_exam[grades[0][l]] = temp_grade
    
    #update avg_grades_by_assignment
    avg_grades_by_assignment[temp_exam] = temp_average_score
    

    
    
    
    
    
    
    
    
    
    







