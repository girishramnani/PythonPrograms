# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 14:00:39 2014

@author: girish
"""
import collections

def GeneratePeg(n,b):
    """ here the n and the b elements would be False"""
    d =collections.OrderedDict()
    for i in range(5):
        for j in range(5-i):
            d[(i,j)]=True
    d[(n,b)]=False
    return d
def FindEmpty(peg):
    empty = []
    for k,v in peg.items():
        if not v:
            empty.append(k)
    return empty
def generateNearest(k,peg):
    li=[]
    test=[]
    for i in range(len(k)):
        a,b = k[i]
        test.extend([(a,b-1),(a,b+1),(a+1,b-1),(a+1,b),(a-1,b),(a-1,b+1)])
    for j,d in test:
        if peg.get((j,d),False):
            li.append((j,d))
    return li
def generateValid(peg):
    k = FindEmpty(peg)
    li = generateNearest(k,peg)
    ww = set(generateNearest(li,peg))
    print(ww)
   
        
    
peg = GeneratePeg(2,1)

def recursiveSolving(peg,filled,li):
    if filled ==1:
        return li
    
        

            
            
              
