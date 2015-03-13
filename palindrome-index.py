# -*- coding: utf-8 -*-
"""
Created on Sat Feb  7 13:33:51 2015

@author: Girish
"""
t = int(input())
for i2 in range(t):
    word = input()
    for i in range(len(word)):
        t2=t[:i]+t[i+1:]
        if str(t2) ==str(t2[::-1]):
            print(i)
            break