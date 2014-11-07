# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 23:59:19 2014

@author: girish
"""

    
string = input()
substring = input()
count=0
x=len(substring)
for i in range(len(string)-len(substring)+1):
    if string[i:i+x]==substring:
        count+=1
print(count)
    
    
