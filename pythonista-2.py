# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 23:47:13 2014

@author: girish
"""

x=int(input())
y=int(input())
z=int(input())
d=int(input())
li=[[a,b,c] for a in range(x+1) for b in range(y+1) for c in range(z+1) if a+b+c!=d]
print(li)