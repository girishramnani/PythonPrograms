# -*- coding: utf-8 -*-
"""
Created on Tue Oct 14 22:53:38 2014

@author: girish
"""

def isWin(num):
    if num<0:
        return
    moves = [num-1,num-3,num-4]
    for i in moves:
        if not isWin(i):return False
    
    
isWin(3)