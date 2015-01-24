# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 16:05:15 2015

@author: Girish
"""

li=[]
for x in range(int(input())):
    
    t=int(input())
    if t!=-1:
        li.append(t)
li2=[int(input()) for x in range(int(input()))]


def sort_with_add(li1,li2):
    ans = []
    x = len(li1)
    y= len(li2)
    i=0
    j=0
    while i<x and j<y:
        if li1[i]>li2[j]:
            ans.append(li2[j])
            j+=1
        else:
            ans.append(li1[i])
            i+=1
    
    ans.extend(li1[i:])
    ans.extend(li2[j:])
    return ans

for x in sort_with_add(li,li2):
    print(x)
        
        
        
    