# -*- coding: utf-8 -*-
"""
Created on Wed Oct  1 21:47:32 2014

@author: girish
"""

chant = str(input())

iteration = int(input())
ans_list=[]

for i in range(iteration):
    a,b = [int(x) for x in input().split()]
    length = len(chant)
    a%=length
    a-=1
    b%=length
    b-=1
    if chant[a]==chant[b]:
        ans_list.append("Yes")
    else:
        ans_list.append("No")
        
for q in range(iteration):
    print(ans_list[q])
        

