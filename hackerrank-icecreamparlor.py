# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 22:40:01 2014

@author: girish
"""
def search(li,n,m):
    for i in range(n):
        t=li[i]
        f=m-t
        for z in range(i+1,n):
            if li[z]==f :
                return i+1,z+1
iteration = int(input())
for i in range(iteration):
    m = int(input())
    n = int(input())
    li=[int(x) for x in input().split()]
    str
    a,b = search(li,n,m)
    print(a,b)
    