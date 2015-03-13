# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 11:03:23 2015

@author: Girish
"""

def rotate(n):
    t=0
    su=0
    while n>0:
        t=n%10
        su= (10*su)+t
        n//=10
    print(su)

def revRecur(n,ro=0):
    if n//10==0:
        return (ro*10)+n
    else:
        return revRecur(n//10,(10*ro)+(n%10))
    
print(revRecur(12345))