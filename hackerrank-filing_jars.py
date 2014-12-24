# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 22:19:57 2014

@author: girish
"""

a,b = [int(z) for z in input().split()]
ans=0
for x in range(b):
    li = [ int(z) for z in input().split()]
    ans +=((abs(li[0]-li[1])+1)*li[2])
print(int(ans/a))