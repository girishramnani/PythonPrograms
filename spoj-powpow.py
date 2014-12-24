# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:01:17 2014

@author: girish
"""
d=(10**9)+7
for z in range(int(input())):
    a,b,c = [int(x) for x in input().split()]
    ans = ((a**((2**c)**b)))%d
    print(ans)