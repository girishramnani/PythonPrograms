# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:09:36 2014

@author: girish
"""

def fibo(n,m):
    li = [0 for _ in range(m+1)]
    li[0]=0
    li[1]=1
    for j in range(2,m+1):
        li[j]=li[j-1]+li[j-2]
    return li[n],li[m]
    
    

iteration = int(input())
for j in range(iteration):
    
    first,last = [int(x) for x in input().split()]
    sum1=0
    fibo_second,fibo_first=fibo(first+1,last+2)
    fibo_first-=1
    fibo_second-=1
    
    sum1+=((fibo_first-fibo_second)%1000000007)
    
   
    print(sum1)
       
