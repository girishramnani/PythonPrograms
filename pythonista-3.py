# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 23:53:48 2014

@author: girish
"""

input()
li = set([int(x) for x in input().split()])

input()
li2 = set([int(x) for x in input().split()])

x = li.symmetric_difference(li2)
x = sorted(x)
for w in x : 
    print(w)