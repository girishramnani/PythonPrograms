# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 19:46:47 2014

@author: girish
"""
def permu(b,a):
    ans=1
    for i in range(b,b-a,-1):
        ans*=i
    return ans
iteration = int(input())
for j in range(iteration):
    a,b =[int(x) for x in input().split()]
    print(permu(b,a))
