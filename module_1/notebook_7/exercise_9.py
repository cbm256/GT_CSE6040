#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 11 23:06:05 2018

@author: hunter
"""


#Let's use primitives to tidy up the original WHO TB data set. First, here is the raw data.

who_raw = pd.read_csv('who.csv')

print("=== WHO TB data set: {} rows x {} columns ===".format(who_raw.shape[0],
                                                              who_raw.shape[1]))
print("Column names:", who_raw.columns)

print("\n=== A few randomly selected rows ===")
import random
row_sample = sorted(random.sample(range(len(who_raw)), 5))
display(who_raw.iloc[row_sample])


#The data set has 7,240 rows and 60 columns. Here is how to decode the columns.
#*Columns 'country', 'iso2', and 'iso3' are different ways to designate the 
#  country and redundant, meaning you only really need to keep one of them.
#*Column 'year' is the year of the report and is a natural variable.
#*Among columns 'new_sp_m014' through 'newrel_f65', the 'new...' prefix indicates 
#  that the column's values count new cases of TB. In this particular data set, 
#  all the data are for new cases.
#*The short codes, rel, ep, sn, and sp describe the type of TB case. They stand 
#  for relapse, extrapulmonary, pulmonary not detectable by a pulmonary smear test 
#  ("smear negative"), and pulmonary detectable by such a test ("smear positive"), respectively.
#*The codes 'm' and 'f' indicate the gender (male and female, respectively).
#*The trailing numeric code indicates the age group: 014 is 0-14 years of 
#  age, 1524 for 15-24 years, 2534 for 25-34 years, etc., and 65 stands for 65 years or older.
#In other words, it looks like you are likely to want to treat all the columns 
#as values of multiple variables!


#Exercise 8 (3 points). As a first step, start with who_raw and create a 
#new data frame, who2, with the following properties:
#*All the 'new...' columns of who_raw become values of a single variable, case_type. 
#  Store the counts associated with each case_type value as a new variable called 'count'.
#*Remove the iso2 and iso3 columns, since they are redundant with country (which you should keep!).
#*Keep the year column as a variable.
#*Remove all not-a-number (NaN) counts. Hint: You can test for a NaN using Python's math.isnan().
#*Convert the counts to integers. (Because of the presence of NaNs, the counts 
#  will be otherwise be treated as floating-point values, which is undesirable 
#  since you do not expect to see non-integer counts.)



from math import isnan

#
# YOUR CODE HERE
#

#first, get all variabls that start with new (variables not like those listed below)
col_vals = who_raw.columns.difference(['country','iso2','iso3','year'])

#melt these values into a column variable named key associated with new variable count
who2 = melt(who_raw, col_vals, 'case_type', 'count')

#remove redundant variables iso2 and iso3
del who2['iso2']
del who2['iso3']

#remove all nan's
who2 = who2[who2['count'].apply(lambda x: not isnan(x))]

#convert counts into integers




who2['count'] = who2['count'].apply(lambda x: int(x))







