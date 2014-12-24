# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 20:44:28 2014

@author: girish
"""

i = int(input())
for z in range(i):
    a,b = [int(x) for x in input().split()]
    if b==0:
        print("Airborne wins.")
    else:
        print("Pagfloyd wins.")