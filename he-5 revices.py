# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 19:51:16 2014

@author: girish
"""

# -*- coding: utf-8 -*-1
"""
Created on Fri Oct  3 19:03:50 2014

@author: girish
"""
import itertools
def findsubsets(S):
    set1 = set()
    for i in range(len(S)+1):
        
        set1=set1.union(set(itertools.combinations(S, i)))
    ans_se=set()
    for q in set1:
        ans_se.add(sum(q))
        
    return len(ans_se)
iteration = int(input())
for di in range(iteration):
    z = int(input())
    li= [ int(x) for x in input().split()]
    print(findsubsets(li))
        
    
                
        
    
