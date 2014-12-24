# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 23:39:04 2014

@author: girish
"""

a,b = [int(x) for x in input().split()]
li = [int(x) for x in input().split()]
li.sort()
su = 0
count=0
t=0
while su<b or count>a:
    su+=li[t]
    t+=1
    count+=1
print(count-1)
    