# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 21:15:52 2014

@author: girish
"""

iteration = int(input())
for i in range(iteration):
    xpr = input()
    stack = [] 
    ex = ""
    for j in range(len(xpr)):
        if xpr[j] == '(':
            continue
        elif xpr[j] >='a' and xpr[j] <='z':
            ex+=xpr[j]
        elif xpr[j] == ')':
            ex +=stack.pop()
        else:
            stack.append(xpr[j])
            
    print(ex)