# -*- coding: utf-8 -*-
"""
Created on Thu Jan 22 12:20:06 2015

@author: Girish
"""

input()

t = [int(x) for x in input().split()]
t.sort()
min1 = float("inf")
ansli = []
for x in range(len(t)-1):
    if min1>(t[x+1]-t[x]):
        min1 = t[x+1]-t[x]
        ansli.clear()
        ansli.append(t[x+1])
        ansli.append(t[x])
    elif min1 ==(t[x+1]-t[x]):
        ansli.append(t[x+1])
        ansli.append(t[x])
ansli.sort()
print(" ".join(map(str,ansli)))
