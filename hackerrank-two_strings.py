# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 19:12:18 2014

@author: girish
"""

iteration =int(input())
for i in range(iteration):
    boolean = False
    str1=input()
    str2=input()
    for j in str1:
        if j in str2:
            print("YES")
            boolean=True
            break
    if boolean==False:
        print("NO")