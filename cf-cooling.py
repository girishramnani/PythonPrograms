# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 23:37:28 2014

@author: girish
"""

iteration = int(input())

for i in range(iteration):
    count=0
    t=int(input())
    li = [int(x) for x in input().split()]
    li2 = [int(y) for y in input().split()]
    li.sort()
    li2.sort()
    p=0
    r=0
    while(r<t ):
        if li[p]>li2[r]:
            r+=1
        else:
            p+=1
            r+=1
            count+=1
    print(count)
    
            
    
    