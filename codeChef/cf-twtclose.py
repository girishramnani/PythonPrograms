# -*- coding: utf-8 -*-
"""
Created on Wed Oct  8 22:50:04 2014

@author: girish
"""

a, b = [ int(x) for x in input().split()]
clickList = [False]*(a+1)
for i in range(b):
    temp = input().split(" ")
    if temp[0] == "CLOSEALL":
        for i in range(a+1):
            clickList[i]=False
    else:
        clickList[int(temp[1])] = not clickList[int(temp[1])]
    
    count = 0    
    for q in clickList:
        if q:
            count+=1
    print(count)