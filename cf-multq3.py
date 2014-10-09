# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 03:00:59 2014

@author: girish
"""

a,b = [ int(x) for x in input().split()]
array=[0]*a
for i in range(b):
    x ,y,z = [int(k) for k in input().split()]
    
    count=0    
    if x:
        for z in array[y:z+1]:
            if z%3==0:
                count+=1
        print(count)
#        print(array)
    else:
        for q in range(y,z+1):
            array[q]+=1
#        print(array)
    