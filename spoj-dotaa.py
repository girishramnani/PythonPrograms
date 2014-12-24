# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 16:09:09 2014

@author: girish
"""

for i in range(int(input())):
    
    a,b,c = [int(x) for x in input().split()]
    count=0
    for i in range(a):
        t = int(input())
        count+=(t-1)//c
    if count>=b:
        print("YES")
    else:
        print("NO")
            