# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 11:47:56 2014

@author: girish
"""
import math
while True:
    t = int(input())
    if t ==-1:
        break
    t-=1
    d=(1+((4/3)*t))
    d=math.sqrt(d)
    w = (-1+d)/2
    
    if int(w)-w == 0:
        print("Y")
    else:
        print("N")