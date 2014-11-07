# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 03:16:25 2014

@author: girish
"""

n,t = input().strip().split();n,t = int(n),int(t)

k = [-1]*n

for i in range(n-1):
    p,c = input().strip().split();p,c = int(p),int(c)
    k[c-1] = p-1
   
r = k.index(-1)

def func(x,y):
    if x == r: return 0
    rt = 1 if abs(x-y) <= t else 0
    if y != r:
       rt += func(x,k[y])
    return rt

pt = 0

for i in range(n):
    pt += func(i,k[i])
    
print(pt)