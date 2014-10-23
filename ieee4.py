# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 22:20:27 2014

@author: girish
"""
import itertools

def allans(list1):
    combi=list()
    for q in range(1,len(list1)+1):
        combi.extend(list(itertools.combinations(list1,q)))
    return  combi
def listgcd(li):
    if len(li)==1:
        return li[0]
    i,j = li[:2]
    q=gcd(i,j)
    for k in li[2:]:
        q=gcd(k,q)
    return q
def gcd(a,b):
    if b==0:
        return a
    else:
        return gcd(b,a%b)

num = int(input())
li = [ int(w) for w in input().split()]
combilist = allans(li)
numtr= int(input())
for y in range(numtr):
    
    count=0
    gcdmatch=int(input())
    for kw in range(len(combilist)):
        if listgcd(combilist[kw]) == gcdmatch:
            count+=1
            
    
    print(count)
            
  

