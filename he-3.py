# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 18:18:44 2014

@author: girish
"""

iteration = int(input())
for i in range(iteration):
    no_of_guitars= int(input())
    list_of_guitars = set([int(x) for x in input().split()])
    print((2**len(list_of_guitars))-1)