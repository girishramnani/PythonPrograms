# -*- coding: utf-8 -*-
"""
Created on Sun Dec 14 23:40:38 2014

@author: girish
"""
import math

from fractions import Fraction as f
su=0
for z in range(int(input())):
    su+=f(input())
su+=1
print(math.ceil(su))