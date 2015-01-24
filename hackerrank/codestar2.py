# -*- coding: utf-8 -*-
"""
Created on Sat Jan 24 16:49:50 2015

@author: Girish
"""


a,b = [int(x) for x in input().split()]
li=[]
for x in range(a):
    t=input().split()
    li.append((int(t[0]),int(t[1])))
li2=[]  
for x in range(b):
    t=input().split()
    li2.append((int(t[0]),int(t[1])))
count1=0
count2=0   
for bi in li:
    if bi in li2:
        count1+=1
done =set([])
for i in range(len(li)):
    for i2 in range(len(li2)):
        if i2 in done:
            continue
        if li[i][1]==li2[i2][1]:
            done.add(i2)
            count2+=1
print(count2,count1)