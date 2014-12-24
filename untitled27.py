# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 12:30:25 2014

@author: girish
"""


        
import itertools as it

for i in range(int(input())):
    t = int(input())
    w=it.permutations(range(1,t+1))
    ans=0
    for z in w:
        print(z)
    
    
        
        
            
            
