# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 21:23:10 2014

@author: girish
"""

a = int(input())
b = int(input())
t=0
for z in range(a,b+1):
    for w in range(z,b+1):
        xor=z^w
        if xor > t:
            t=xor
print(t)