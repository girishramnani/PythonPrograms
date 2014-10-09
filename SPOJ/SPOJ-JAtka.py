# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 17:15:17 2014

@author: girish
"""

ans_list =[]

for i in range(10):
    input1 = int(input())
    input2 = int(input())
    ans=(input1+input2)/2
    ans2=input1-ans
    ans_list.append(ans)
    ans_list.append(ans2)

for j in range(20):
    print(int(ans_list[j]))