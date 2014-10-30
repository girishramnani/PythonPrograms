# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 19:50:43 2014

@author: girish
"""

while(True):
    x = int(input())
    if x == -1:
        break
    else:
        li = [int(input()) for w in range(x)]
    w = sum(li)
    if w % x != 0 :
        print(-1)
    else:
        count=0
        avg = w/x
        for i in li:
            if avg>i:
                count+=abs(avg-i) 
            
        print(int(count))
        