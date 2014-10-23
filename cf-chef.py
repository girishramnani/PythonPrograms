# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 15:55:29 2014

@author: girish
"""
def listgcd(li):
    i,j = li[:2]
    q=gcd(i,j)
    for k in li[2:]:
        q=gcd(k,q)
    return q
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)
        
iteration = int(input())
for i in range(iteration):
    li = list(map(int,input().split()))[1:]
    w = listgcd(li)
    li2 = list(map(lambda a : str(int(a/w)),li))
    li2 = " ".join(li2)
    print(li2)
    
    

