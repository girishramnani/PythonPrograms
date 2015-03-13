# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:53:47 2015

@author: Girish
"""

t =int(input())
li = [int(x) for x in input().split()]
count = dict()
for x in li:
    count[x] = count.get(x,0)+1
for w in range(100):
    print("{} ".format(w)*count.get(w,0),end="")
print()