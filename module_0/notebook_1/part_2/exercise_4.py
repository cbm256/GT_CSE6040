#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:56:13 2018

@author: hunter
"""

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

#Exercise 4 (avg_grades_by_student_test: 1 point). Write some code to compute
#dictionary named avg_grades_by_student that maps each student to his or her 
#average exam score. For instance, avg_grades_by_student['Thorny'] == 90.
#Hint. The statistics module of Python has at least one helpful function.

#create a copy of list
popped_grades = grades[:]
#Exercise 4 (avg_grades_by_student_test: 1 point). Write some code to compute a 

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
num_lists = len(grades)

#find how many elements are in each list in grades
num_elements = len(grades[0])

avg_grades_by_student = {}

#find the average of each students scores
for k in range(1 , num_lists):
    #find the average of each list
    temp_average_score = sum(grade_lists[grades[k][0]]) / len(grade_lists[grades[k][0]])
    
    #find the corresponding students name
    temp_student = grades[k][0]
    
    #update the temp exam score dictionary
    #temp_exam[grades[0][l]] = temp_grade
    
    #update avg_grades_by_student
    avg_grades_by_student[temp_student] = temp_average_score
    

    
    
    
    
    
    
    
    
    
    