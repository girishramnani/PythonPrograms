# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:29:25 2014

@author: girish
"""

iteration = int(input())
for i in  range(iteration):
    temp = int(input())
    qotient = temp/2048
    temp %=2048
    
    temp=bin(temp)
    
    count=0
    temp = temp[2:]
    temp = list(map(int,temp))
    
    print(int(sum(temp)+qotient))
    