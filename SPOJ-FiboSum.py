# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 22:09:36 2014

@author: girish
"""

def fibo(n):
    if n == 0:
        return 0
    elif n==1:
        return 1
    else:
        return fibo(n-1)+fibo(n-2)

iteration = int(input())
ans_list=[]
for j in range(iteration):
    
    first,last = [int(x) for x in input().split()]
    sum1=0
    fibo_second=fibo(first+1)
    fibo_first = fibo(first)
    sum1+=(fibo_first+fibo_second)
    
    for i in range(first+1,last):
        new_fibo=fibo_first+fibo_second
        
        sum1+=new_fibo
        fibo_first=fibo_second
        fibo_second=new_fibo
    ans_list.append(sum1%1000000007)
            
for q in range(iteration):
    print(ans_list[q])