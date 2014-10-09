# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 00:15:45 2014

@author: girish
"""


def mergesort(elist,count):
    total=[]
    #print(count)
    low=0
    high=len(elist)
    #print(len(elist))
    if len(elist)<2:
       return elist,count
    mid=int((low+high)/2)
    enlist=[]
    y,count=mergesort(elist[:mid],count)
    z,count=mergesort(elist[mid:high],count)
    i=0
    j=0

    while(i<len(y) and j<len(z)):
        if y[i]<=z[j]:
           enlist.append(y[i])
           i+=1

        else:
             count+=abs((len(y))-i)
             enlist.append(z[j])
             j+=1

    enlist+=y[i:];
    enlist+=z[j:]

    return enlist,count


iteration = int(input())
ans=[]
for i in range(iteration):
    input()
    m=input().split()
    m=list(map(int,m))
    ans.append(mergesort(m,0)[1])
for i in range(iteration):
    print(ans[i])
    

    