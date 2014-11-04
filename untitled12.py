# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 17:14:38 2014

@author: girish
"""

str1=list(input())
str2 = list(input())
le = min(len(str2),len(str1))
count=0
while(str1):
    x = str1.pop()
    if x in str2:
        str2.remove(x)
    else:
        count+=1
count+=len(str2)
print(count)
        