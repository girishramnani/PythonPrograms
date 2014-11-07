# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 21:56:55 2014

@author: girish
"""
import math

iteration = int(input())
for i in range(iteration):
    it = int(input())
    count=False
    
    while(it>1):
        count = not count
        if (it & (it-1)==0):
            it//=2
        else:
            it=2**(int(math.log2(it)))
    
    if count:
        print("Richard")
    else:
        print("Louise")