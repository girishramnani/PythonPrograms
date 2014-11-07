# -*- coding: utf-8 -*-
"""
Created on Wed Nov  5 23:50:30 2014

@author: girish
"""
iteration = int(input())
li = [ int(x) for x in input().split()]
dic1 = dict()
for k in li:
    dic1[k]=dic1.get(k,0)+1
input()
li2 = [ int(x) for x in input().split()]
dic2 = dict()
for k in li2:
    dic2[k]=dic2.get(k,0)+1

for k,v in dic1.items():
    dif=dic2.get(k)-v
    for z in range(dif) : print(k,end=" ")
    del(dic2[k])
for k,v in dic2.items():
    for a in range(v):
        print(k,end=" ")