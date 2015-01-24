# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:22:35 2015

@author: Girish
"""

t = int(input())
w = [int(x) for x in input().split()]
print(len(w))
while len(w)>1:
    l = min(w)
    w = [x-l for x in w if x-l>0]
    print(len(w))