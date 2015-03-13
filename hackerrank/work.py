# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 15:20:14 2015

@author: Girish
"""
def joseph(n,k):
    if n==1:
        return 1
    return (joseph(n-1,k+1)+(k-1)) % (n+1)
def ans(li):
    li = list(range(1,li+1))
    skip=0
    i=0
    while len(li)>1:
        i+=skip
        i = (i)%len(li)
        del(li[i])
        skip+=1
    return li[0]
    
t = int(input())
for x in range(t):
    print(joseph(int(input()),0))
    
    
    
    