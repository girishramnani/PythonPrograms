# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:34:34 2014

@author: girish
"""

num = int(input())
z  =  [ int(w) for w in input().split()]
intaken = int(input())

for gir in range(intaken):
    w1=z.copy()
    swift = int(input())
    for w in range(len(z)):
        w1[w]+=z[(w-swift)%(num)]
    z=w1
z = 1000000007
print(int(sum(w1)%z))
