# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 12:40:50 2014

@author: girish
"""
import sys
diction = dict()
def byt(n):
    if n<4:
        return n
    t=diction.get(n,-1)
    if  t!=-1:
        return t
    a=byt(n//2)
    b=byt(n//3)
    c=byt(n//4)
    t=a+b+c
    diction[n//2]=a
    diction[n//3]=b
    diction[n//4]=c
    if t>n:
        return t
    else:
        return n

while True:
    i=sys.stdin.readline().replace("\n","")
    
    if len(i)==0:
        break
    i=int(i)
    print(byt(i))
    
    
        
