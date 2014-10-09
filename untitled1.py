# -*- coding: utf-8 -*-
"""
Created on Sat Sep 20 12:03:29 2014

@author: girish
"""


x = set([])
it = int(input())
temp =2
for i in range(it):
    
    
    while(it%temp==0):
       
        x.add(temp)
        it/=temp
    temp+=1
    
y = list(x)
print(y[-1])