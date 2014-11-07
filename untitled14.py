# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 16:55:12 2014

@author: girish
"""

def show(li):
    for x in li:
        yield x
print(list(show([1,2,3,4])))