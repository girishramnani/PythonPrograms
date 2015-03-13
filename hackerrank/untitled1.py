# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 15:54:38 2015

@author: Girish
"""

test = int(input())
a,b = [int(x) for x in input().split()]
count=0
li =[int(x) for x in input().split() ]
for i in li:
    if i<0:
        count+=1
sum1=0
if count >=b:
    for x in range(b):
        sum1+=(-li[x])
    sum1+=sum(li[b:])
else:
    if b%2==0:
        
        
        
        
