# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 15:20:55 2019

@author: CL
"""

#For Loop

first_name = ["Ali","Ahmed","Yasir"]
last_name = ["Farooq"]
full_name = []

for i in first_name:
    for j in last_name:
        full_name.append(i + " " +j)
        
print(full_name,end='\n')
        
