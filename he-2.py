# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:47:41 2014

@author: girish
"""
import math


def seive(li):
    list1 = [1]*(li+1)
    list1[0]=0
    list1[1]=0
    for i in range(2,int(math.sqrt(li))+1):
        if list1[i]:
            q=i*i
            while q <li+1:
                list1[q]=0
                q+=i
    primelist=[i for i in range(li+1) if list1[i]==1 ]
    
    length = len(primelist)
    
    for d in range(length):
        for a in range(0,d):
            if primelist[d]-primelist[a] in primelist:
                print(primelist[d],end=" ")
                                
                break
    print()
        
iteration = int(input())

for i in range(iteration):
    inp = int(input())
    seive(inp)
    

                
        
        
        
    