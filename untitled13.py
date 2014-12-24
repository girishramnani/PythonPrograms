# -*- coding: utf-8 -*-
"""
Created on Sun Nov  9 12:26:36 2014

@author: girish
"""

def byt(num):
    if num<2:
        return 0
    if num==2:
        return 1
    q = sum((num//2)+(num//3)+(num//4))
    
        
        return max(q,) 