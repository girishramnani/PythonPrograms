# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 19:56:15 2014

@author: girish
"""

iteration = int(input())
ans_list=[]
for i in range(iteration):
    li = input().split(" ")
    li =list(map(int,li))
    ans_list.append(pow(li[0],li[1],10))
    
for j in range(iteration):
    
    print(ans_list[j])