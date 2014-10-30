# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 23:26:18 2014

@author: girish
"""

li=[0,1,5,8,9,10,17,17,20,24,30]
def CutRod(li,n):
    if n==0:
        return 0
    q=float("-inf")
    
    for i in range(1,n+1):
        q = max(q,li[i]+CutRod(li,n-i))
        
    return q
print(CutRod(li,7))
