# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 09:38:39 2015

@author: Girish
"""

t = input()
t2= input()
i=0
count=0
while i<(len(t)-len(t2)+1):
    
    if t[i:i+len(t2)] == t2:
        count+=1
    i+=1
print(count)