# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 01:42:42 2014

@author: girish
"""

iteration = int(input())
for i in range(iteration):
    inlist = [ int(x) for x in input().split()]
    heap = []    
    for q in range(3):
        heap.extend([int(w) for w in input().split()])
    
   
    for z in range(inlist[3]):
        maxt =max(heap)
        heap.remove(maxt)
        maxt= int(maxt/2)
        heap.append(maxt)
    print(max(heap))