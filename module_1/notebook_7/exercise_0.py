#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 27 23:25:24 2018

@author: hunter
"""

#Exercise 0 (ungraded). Run the code cell below to download the data. (This code 
#           will check if each dataset has already been downloaded and, if so, will avoid re-downloading it.)

#------------------------------NOT MY CODE!!-----------------------------------

import requests
import os
import hashlib
import io

def download(file, url_suffix=None, checksum=None):
    if url_suffix is None:
        url_suffix = file
        
    if not os.path.exists(file):
        url = 'https://cse6040.gatech.edu/datasets/{}'.format(url_suffix)
        print("Downloading: {} ...".format(url))
        r = requests.get(url)
        with open(file, 'w', encoding=r.encoding) as f:
            f.write(r.text)
            
    if checksum is not None:
        with io.open(file, 'r', encoding='utf-8', errors='replace') as f:
            body = f.read()
            body_checksum = hashlib.md5(body.encode('utf-8')).hexdigest()
            assert body_checksum == checksum, \
                "Downloaded file '{}' has incorrect checksum: '{}' instead of '{}'".format(file, body_checksum, checksum)
    
    print("'{}' is ready!".format(file))
    
datasets = {'iris.csv': 'd1175c032e1042bec7f974c91e4a65ae',
            'table1.csv': '556ffe73363752488d6b41462f5ff3c9',
            'table2.csv': '16e04efbc7122e515f7a81a3361e6b87',
            'table3.csv': '531d13889f191d6c07c27c3c7ea035ff',
            'table4a.csv': '3c0bbecb40c6958df33a1f9aa5629a80',
            'table4b.csv': '8484bcdf07b50a7e0932099daa72a93d',
            'who.csv': '59fed6bbce66349bf00244b550a93544',
            'who2_soln.csv': 'f6d4875feea9d6fca82ae7f87f760f44',
            'who3_soln.csv': 'fba14f1e088d871e4407f5f737cfbc06'}

for filename, checksum in datasets.items():
    download(filename, url_suffix='tidy/{}'.format(filename), checksum=checksum)
    
print("\n(All data appears to be ready.)")