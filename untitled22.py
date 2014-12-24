# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 19:10:13 2014

@author: girish
"""

Testcase = int(input())

for _ in range(Testcase):
    n = int(input())
    c = 5*(2*n%3)
    if c > n:
        print -1
    else:
        print ('5' * (n-c) + '3'*c)