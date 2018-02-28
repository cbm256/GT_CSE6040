#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  8 12:41:53 2018

@author: hunter
"""

#------------------------------------------------------------------------------
#importing the yelp html file and turning it into a string  (not my code)

import requests
import os
import hashlib

if os.path.exists('.voc'):
    data_url = 'https://cse6040.gatech.edu/datasets/yelp-example/yelp.htm'
else:
    data_url = 'https://github.com/cse6040/labs-fa17/raw/master/datasets/yelp.htm'

if not os.path.exists('yelp.htm'):
    print("Downloading: {} ...".format(data_url))
    r = requests.get(data_url)
    with open('yelp.htm', 'w', encoding=r.encoding) as f:
        f.write(r.text)

with open('yelp.htm', 'r') as f:
    yelp_html = f.read().encode(encoding='utf-8')
    checksum = hashlib.md5(yelp_html).hexdigest()
    assert checksum == "4a74a0ee9cefee773e76a22a52d45a8e", "Downloaded file has incorrect checksum!"
    
with open('yelp.htm') as yelp_file:
    yelp_html = yelp_file.read()


#------------------------------------------------------------------------------
    
#   Exercise (5 points): Extracting the ranking
#Write some Python code to create a variable named rankings, which is a list of 
#dictionaries set up as follows:
#rankings[i] is a dictionary corresponding to the restaurant whose rank is i+1. 
#For example, from the screenshot above, rankings[0] should be a dictionary 
#with information about Gus's World Famous Fried Chicken.Each dictionary, 
#rankings[i], should have these keys:
#rankings[i]['name']: The name of the restaurant, a string.
#rankings[i]['stars']: The star rating, as a string, e.g., '4.5', '4.0'
#rankings[i]['numrevs']: The number of reviews, as an integer.
#rankings[i]['price']: The price range, as dollar signs, e.g., '$', '$$', '$$$', or '$$$$'.
#Of course, since the current topic is regular expressions, you might try to apply them (possibly combined with other string manipulation methods) find the particular patterns that yield the desired information 
    
import re






#------------------------------------------------------------------------------  
#lists of the pertinent information are created

#all names are preceded by this pattern:
names = re.findall(r'\<span>(.*?)\<\/span>\<\/a>', yelp_html)
    
#all stars (ratings) have this pattern:
stars = re.findall(r'rating\-large\" title\=\"(.*?) star rating', yelp_html)

#numrevs matches this pattern (re.DOTALL matches across new lines, since that
#is the pattern in the html file)
numrevs = re.findall(r'qualifier\"\>(.*?)reviews', yelp_html, re.DOTALL)

#price matches the following pattern
prices = re.findall('price\-range\"\>(.*?)\<\/span>', yelp_html)


#------------------------------------------------------------------------------ 
#create a list of dictionaries
rankings = []

for i in range(len(names)):
    #find the value from the above lists for the current indice of the for loop
    temp_name = names[i]
    temp_stars = stars[i]
    #numrevs should be an int
    temp_numrevs = int(numrevs[i])
    temp_price = prices[i]
    #create the temp dictionary
    temp_dict = {'name' : temp_name, 'stars' : temp_stars, 'numrevs' : temp_numrevs, 'price' : temp_price}
    #append the dictionary to rankings
    rankings.append(temp_dict)


#elements 0,1, and 12 (first two and last) should be removed from the list, 
#since they are advertisements and should not be included
rankings = rankings[2:12]
    
    
    
    
    
    
    
    
    
    
    
    
    

