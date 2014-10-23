# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 21:43:55 2014

@author: girish
"""


num = int(input())
z  =  [ int(w) for w in input().split()]

w1=z.copy()
while(True):
    swift = int(input())
    if swift == 0:
        break
    for w in range(len(z)):
        w1[w]+=z[(w-swift)%(num)]
    print(w1)
        
        