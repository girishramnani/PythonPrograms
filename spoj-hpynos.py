# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 21:06:40 2014

@author: girish
"""
def brea(n):
    su=0
    while n>0:
        t=n%10
        su+=(t*t)
        n//=10
    return su
j = int(input())
s=set([])
bol=True
count=0
while bol:
    j=brea(j)
    count+=1
    if j==1:
        print(count)
        break
    elif j in s:
        print(-1)
        break
    else:
        s.add(j)
        
        
    
    
    
