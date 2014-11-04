# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 22:56:40 2014

@author: girish
"""
def ser(li,q1,d):
    for k in range(d):
        if not (q1[k] in li[k]):
            return False
    return True
iteration = int(input())
for i in range(iteration):
    a,b=[int(x) for x in input().split()]
    li=list()
    for x in range(a):
        li.append(input())
    d,c=[int(x) for x in input().split()]
    li2=list()
    for x in range(d):
        li2.append(input())
    bot =True
    for z in range(1,a-d+2):
        if ser(li[z-1:],li2,d)==True:
            print("YES")
            bot=False
            break
    if bot:
        print("NO")
            
    
        
        