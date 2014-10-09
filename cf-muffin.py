# -*- coding: utf-8 -*-
"""
Created on Thu Oct  2 01:18:47 2014

@author: girish
"""


a,b = [ int (x) for x in input().split()]
up=a
down=1
for i in range(1,b):
    print(i , a-i)
    up*=(a-i)
    down*=(i+1)
print(up/down)