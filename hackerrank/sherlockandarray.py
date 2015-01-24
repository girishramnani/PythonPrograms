# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:30:41 2015

@author: Girish
"""

for z in range(int(input())):
    input()
    bol=False
    li = [int(x) for x in input().split()]
    su1=[li[0]]
    for z in range(1,len(li)):
        su1.append(li[z]+li[z-1])
    for z in range(1,len(li)):
        k1=su1[z]
        k2 =su1[len(li)-1]-su1[z-1]
        if k1 ==k2:
            print("YES")
            break
    else:
        print("NO")
            