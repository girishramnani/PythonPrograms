# -*- coding: utf-8 -*-
"""
Created on Sun Nov  2 22:37:59 2014

@author: girish
"""
import math

def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)


def lcm(a,b):
    temp = gcd(a,b)
    return (a*b)//temp
    
iteration = int(input())
for i in range(iteration):
    non = int(input())
    li = [ int(x) for x in input().split() ]
    anslist =list()
    anslist.append(str(li[0]))
    for j in range(non-1):
        anslist.append(str(lcm(li[j],li[j+1])))
    anslist.append(str(li[-1]))
    print(" ".join(anslist))
        