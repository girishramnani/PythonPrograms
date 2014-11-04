# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 23:30:48 2014

@author: girish
"""

iteration = int(input())
marks = dict()
for i in range(iteration):
    li = input()
    marks[li[0]] = sum([int(x) for x in li[1:]])/3
print("{:.2}".format(marks[input()]))
    