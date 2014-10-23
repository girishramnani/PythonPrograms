# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:08:11 2014

@author: girish
"""

iteration = int(input())
for z in range(iteration):
        
    r = int(input())
   
    ans = (4*(r**2))+0.25
    print("Case {}: {}".format(z+1,ans))