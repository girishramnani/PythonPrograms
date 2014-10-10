# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 00:28:21 2014

@author: girish
"""

class heap(list):
    def __init__(self):
        list.__init__(self)
    def __repr__(self):
        return "heap ("+list.__repr__(self)+")"
        
    def add(self, item):
        
        


c= heap()
c.append(435)
print(c)