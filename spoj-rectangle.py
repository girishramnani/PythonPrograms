# -*- coding: utf-8 -*-
"""
Created on Wed Jan  7 10:19:20 2015

@author: Girish
"""
import math
for x in range(int(input())):
    li=[ float(x) for x in input().split()]
    s = sum(li)/2
    area = math.sqrt((s-li[0])*(s-li[1])*(s-li[2])*(s-li[3]))
    print("{:.2f}".format(area))