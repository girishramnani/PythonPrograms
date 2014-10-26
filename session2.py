# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 16:30:57 2014

@author: girish
"""


li=[(1,2,3),(5,6,7),(9,10,11)]
p = list(zip(*li))
t=len(p)-1
lis = [str(a)+str(b) for a in p[t] for b in p[t-1]]
t-=2
while len(lis[0]) != len(li[0]):
    lis = [ str(d)+str(c) for d in lis for c in p[t] ]
    t-=1
print(lis)