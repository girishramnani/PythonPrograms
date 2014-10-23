# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 02:19:06 2014

@author: girish
"""
from math import *


try:
    iteration = int(input())
    for z in range(iteration):
        U,W,v,V,u,w = [int(x) for x in input().split()]
        X=(w-U+v)*(U+v+w)
        x=(U-v+w)*(v-w+U)
        Y=(u-V+w)*(V+w+u)
        y=(V-w+u)*(w-u+V)
        Z=(v-W+u)*(W+u+v)
        z=(W-u+v)*(u-v+W)
        a=math.sqrt(x*Y*Z)
        b=math.sqrt(y*Z*X)
        c=math.sqrt(z*X*Y)
        d=math.sqrt(x*y*z)
        volume=sqrt((-a+b+c+d)*(a-b+c+d)*(a+b-c+d)*(a+b+c-d))/(192*u*v*w)
        
        print(round(volume,4))
except:
    print(0)
        