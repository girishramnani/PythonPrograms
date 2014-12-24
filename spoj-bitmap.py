# -*- coding: utf-8 -*-
"""
Created on Fri Dec 12 15:16:31 2014

@author: girish
"""
def findmin(a,b,li):
   
    minx = float("inf")
    for x,y in li:
        tx = abs(x-a)+abs(y-b)
    
        if tx <minx:
            minx =tx
        
    return minx
    
        
iteration = int(input())
for i in range(iteration):
    loc = list()
    a,b = [ int(x) for x in input().split()]
    
    li =[list(map(int,list(input()))) for _ in range(a) ]
    
    for i in range(a):
        for j in range(b):
            if li[i][j]==1:
                loc.append((i,j))
    ansbox=[]
    for i in range(a):
        lit=[]
        for j in range(b):
            if li[i][j]==0:
                lit.append(findmin(i,j,loc))
            else:
                lit.append(0)
        ansbox.append(lit)
    ans=''
    for i in range(a):
        for j in range(b):
            print(ansbox[i][j],end=" ")
        print()
    
            