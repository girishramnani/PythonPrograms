# -*- coding: utf-8 -*-1
"""
Created on Fri Oct  3 19:03:50 2014

@author: girish
"""

iteration = int(input())
for di in range(iteration):
    z = int(input())
    li= [ int(x) for x in input().split()]
    allMasks = (1 << z);
    ans_set=set([])
    for i in range(allMasks):
        sum1=0
        
        binaryrep=list(bin(i))[2:]
        binaryrep=list(map(int,binaryrep))
        while(len(binaryrep)<z):
            binaryrep.insert(0,0)
        for k in range(len(binaryrep)):
            if binaryrep[k]:
                sum1+=li[k]
        ans_set.add(sum1)
    print(len(ans_set))
                
        
    
