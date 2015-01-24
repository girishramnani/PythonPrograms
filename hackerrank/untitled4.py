# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 21:11:17 2015

@author: Girish
"""
from math import floor,ceil,sqrt
word = input()
x =floor(sqrt(len(word)))
y = ceil(sqrt(len(word)))
li=[]
rl =[]
for z in range(len(word)):
    rl.append(word[z])
    if z % x==0 and z!=0:
        li.append(rl)
        rl = []


for a in list(zip(*li)):
    print("".join(a),end=" ")
    
    