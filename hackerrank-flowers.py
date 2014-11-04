# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 21:46:36 2014

@author: girish
"""

a,b = [int(x) for x in input().split()]
dif = a-b
li = [ int(x) for x in input().split()]
li.sort(reverse=True)

t=0
su=0
r=a//b
aa=0
for i in range(1,r+1):
    
    for k in range(1,b+1):
        su+=(i*li[aa])
        aa+=1
        
    
if a%b!=0:
    su+=(li[-1]*(r+1))
print(su)
