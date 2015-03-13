# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 11:33:11 2015

@author: Girish
"""

def swap(li,t,t2):
    tmp = li[t]
    li[t]=li[t2]
    li[t2]=tmp
    
def swap_list(li,t,t2):
    li = li[:t]+li[t2:t-1:-1]+li[t2+1:]
    return li
t = int(input())
li = [int(x) for x in input().split()]
index=set([])
for i in range(t-1):
    if li[i]>li[i+1]:
        index.add(i)
        index.add(i+1)
if len(index) ==2:
    t = max(index)
    t2 = min(index)
    swap(li,t,t2)
    tog =True
else:
    t = max(index)
    t2 = min(index)
    li= swap_list(li,t2,t)
    tog=False
    
real = sorted(li)

if real ==li and tog:
    print("yes")
    print("swap {} {}".format(t2+1,t+1))
elif real ==li and not tog:
    print("yes")
    print("reverse {} {}".format(t2+1,t+1))
else:
    print("no")
        



    