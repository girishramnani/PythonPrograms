# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 00:25:32 2014

@author: girish
"""

iteration = int(input())
li = [ int(x) for x in input().split()]
li=sorted(li)
print(li)
min1=float("inf")
anslist=[]
for i in range(iteration-1):
    diff = abs(li[i]-li[i+1])
    if min1>diff:
        min1=diff
        anslist.clear()
        anslist.append(li[i])
        anslist.append(li[i+1])
    elif min1==diff:
        anslist.append(li[i])
        anslist.append(li[i+1])
for i in anslist: print(i,end=" ")
        
    