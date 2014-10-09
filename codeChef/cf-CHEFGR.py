# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 01:16:55 2014

@author: girish
"""

iteration = int(input())

for _ in range(iteration):
    a , b = [ int(x) for x in input().split()]
    li = [ int(y) for y in input().split()]
    m = max(li)
    exp =m*a-sum(li)
    
    if  exp==b or (b-exp)%a==0:
        print("Yes")
    else:
        print("No")