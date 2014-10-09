# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 12:16:52 2014

@author: girish
"""
def fact(x):
    ans=1
    for i in range(1,x+1):
        
        ans= ans*i
    return ans
x = int(input())

t = fact(x)

ans=0


while(t>1):
    temp=int(t%10)
    ans+=temp
    t/=10
    
print(ans)