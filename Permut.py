# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 23:00:11 2014

@author: girish
"""

while(True):
    no = int(input())
    if no==0:
        break
    
    t = [int(x) for x in input().split()]
    bo = True
    count=0
    for z in range(1,len(t)+1):
        
        if t[t[z-1]-1]==z:
            count+=1
    if count==no:
        print("ambiguous")
    else:
        print("not ambiguous")
    
    
