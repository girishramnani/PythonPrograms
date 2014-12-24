# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 18:52:06 2014

@author: girish
"""

inputno = int(input())
li= [int(x) for x in input().split()]
count=0
skipset=set()
li.sort()

for t in range(inputno):
    if li[t] in skipset:
        continue
    skipset.update(range(li[t],li[t]+5))
    count+=1
    
print(count)   
    