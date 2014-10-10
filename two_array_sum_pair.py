# -*- coding: utf-8 -*-
"""
Created on Sat Oct 11 01:52:41 2014

@author: girish
"""

list1 = [ int(x) for x in input().split()]
list2= [ int(x) for x in input().split()]

question = int(input())
for i in list1:
    if question-i in list2:
        print (i , question-i)
    
    