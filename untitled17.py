# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 02:10:12 2014

@author: girish
"""
a,b = [int(x) for x in input().split()]
li = [int(x) for x in input().split()]
count=0
for i in range(a-1):
    for j in range(i+1,a):
        if abs(li[i]-li[j])==b:
            count+=1
print(count)
            