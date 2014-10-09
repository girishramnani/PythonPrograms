# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 17:01:39 2014

@author: girish
"""

iteration = int(input())
ans_list=[]
for i in range(iteration):
    input()
    no_of = int(input())
    sum1=0
    for j in range(no_of):
        sum1+=int(input())
    if(sum1 % no_of == 0):
        ans_list.append("YES")
    else:
        ans_list.append("NO")
        
for k in range(iteration):
    print(ans_list[k])
        