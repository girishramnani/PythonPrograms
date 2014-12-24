# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 22:26:49 2014

@author: girish
"""

i = int(input())

li=[int(input()) for x in range(i)]
w=0
for z in li:
    w=w^z
print(w)
          