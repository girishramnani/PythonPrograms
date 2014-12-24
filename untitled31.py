# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 15:11:54 2014

@author: girish
"""

a,b = [int(x) for x in input().split()]
li = [int(input()) for z in range(a)]
t=[]
count=0
for x in range(1,a):
    for z in range(a):
        if x+z<=a:
            if sum(li[z:z+x])%b==0:
                count+=1
if sum(li)%b==0:
    count+=1
print(count)