# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 12:17:33 2015

@author: Girish
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:53:47 2015

@author: Girish
"""

t =int(input())
li=[int(input().split()[0]) for x in range(t) ]
#li = [int(x) for x in input().split()]
count = dict()
for x in li:
    count[x] = count.get(x,0)+1
t = count.get(0,0)
print(t,end=" ")
for w in range(1,100):
    t=count.get(w,0)+t
    print(t,end=" ")
print()