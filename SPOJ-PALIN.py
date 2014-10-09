# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 18:25:44 2014

@author: girish
"""


j = str(input())
mid = int(len(j)/2)
part1=j[:mid]
part2= j[:mid:-1]
print(part1)
print(part2)