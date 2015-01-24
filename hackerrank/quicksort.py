# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:58:00 2015

@author: Girish
"""

for x in range(int(input())):
    li =[int(x) for x in input().split(" ")]
    pivot = li[0]
    li1=[x for x in li if x <pivot]
    li2=[x for x in li if x>=pivot]
    ans = li1+li2
    for x in ans:
        print(str(x)+" ",end="")
    print()