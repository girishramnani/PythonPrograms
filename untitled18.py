# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 02:41:51 2014

@author: girish
"""
from math import sqrt

iteration = int(input())
for z in range(iteration):
    a,b = [int(x) for x in input().split()]
    a1 = int(sqrt(a))
    count=4
    
    for i in range(1,a1):
        if float(sqrt(a-(i*i))).is_integer():
            count+=4
    if count<=b or b==0:
        print("possible")
    else:
        print("impossible")
    
    
    