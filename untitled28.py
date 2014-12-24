# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 12:50:11 2014

@author: girish
"""

li=[]
def factfun(t):
    
    fact=1
    for i in range(2,t+1):
        fact*=i
    return fact
for z in range(1,100001):
    t = z
    mul = factfun(t)//t
    
    real=0
    for k in range(1,t+1):
        ans=0
        for w in range(1,t+1):
            ans+=(abs(k-w))
        real+=(mul*ans)
    li.append(real%1000000007)
print(li)       