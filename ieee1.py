# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 18:28:16 2014

@author: girish
"""

z = [int(x) for x in input().split()]
li = [ int(w) for w in input().split()]
li.sort()
print(li[z[2]-1])