# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 16:03:41 2014

@author: girish
"""

while(True):
    num = int(input())
    if num==0:
        break
    anslist=dict()
    t=2
    while(num>1):
        count=0
        while(num%t==0):
            num//=t
            count+=1
        if count!=0:
            anslist[t] =count
        if t==2:
            t+=1
        else:
            t+=2
    anslist = sorted(anslist.items(), key=lambda x :x[1])
    for k,v in anslist:
        print("{}^{}".format(k,v),end=" ")
    print()
        
            