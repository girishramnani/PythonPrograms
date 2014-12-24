# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 21:33:12 2014

@author: girish
"""

iteration = int(input())
for z in range(iteration):
    word = input()
    count=0
    for x in range(len(word)-1):
        if word[x] ==word[x+1]:
            count+=1
    print(count)
        