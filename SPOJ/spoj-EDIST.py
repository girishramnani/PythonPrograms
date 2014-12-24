# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 20:49:09 2014

@author: girish
"""

iteration = int(input())
for i in range(iteration):
    x=input()
    y=input()
    x=x.capitalize()
    y=y.capitalize()
    count=0
    count+=abs(len(x)-len(y))
    w=min(len(x),len(y))
    for z in range(w):
        if x[z] !=y[z]:
            count+=1
    print(count)