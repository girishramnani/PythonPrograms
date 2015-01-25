# -*- coding: utf-8 -*-
"""
Created on Sun Jan 25 13:16:54 2015

@author: Girish
"""
def create_dict(li):
    di =dict()
    for i in li:
        di[i] = di.get(i,0)+1
    return di
        
for i in range(int(input())):
    input()
    li = [int(x) for x in input().split()]
    t  = sum([ y*(y-1) for x,y in create_dict(li).items() if y >1])
    print(t)
    