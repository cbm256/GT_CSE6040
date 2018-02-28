#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 00:50:42 2018

@author: hunter
"""

#Exercise 3 (grade_dicts_test: 2 points). Write some code to compute a new 
#dictionary, grade_dicts, that maps names of students to dictionaries 
#containing their scores. Each entry of this scores dictionary should be keyed
#on assignment name and hold the corresponding grade as an integer. For
#instance, grade_dicts['Thorny']['Exam 1'] == 100.

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

#find how many lists we have in popped_gades
popped_num_lists = len(popped_grades)

#find how many elements are in each list in popped_grades
popped_num_elements = len(popped_grades[0])


#convert the elements of the list which may be converted into ints into ints
#using try except
for i in range(0 , popped_num_lists):
    for j in range(0 , popped_num_elements):
        try:
            popped_grades[i][j] = int(popped_grades[i][j])
        except:
            popped_grades[i][j] = popped_grades[i][j] 
        
#print(popped_grades)

#create the dictionary named grade_lists
grade_lists = {t[0]:t[1:] for t in popped_grades}


#find how many lists we have in grades
num_lists = len(grades)

#find how many elements are in each list in grades
num_elements = len(grades[0])

#create a dictionary called grade_dicts
grade_dicts = {}
temp_exam = {}

#here we update each 
for k in range(1 , num_lists):
    temp_student = grades[k][0]
    for l in range(1 , num_elements):
        #find the grade by indexing
        temp_grade = grades[k][l]
        #update the temp exam score dictionary
        temp_exam[grades[0][l]] = temp_grade
    #update the grade_dicts dictionary 
    #*********** adding .copy() to temp_exam is VERY important ****************
    #**** .copy() prevents every student's exam scores from being updated *****
    grade_dicts[temp_student] = temp_exam.copy()







