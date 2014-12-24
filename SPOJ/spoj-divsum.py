# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 15:16:53 2014

@author: girish
"""
import math
iteration = int(input())
for i in range(iteration):
    num = int(input())
    su=1
    for z in range(2,int(math.sqrt(num)+1)):
        if num%z==0:
            if num%z==z:
                
                su+=z
            else:
                su+=z+(num//z)
                
    print(su)