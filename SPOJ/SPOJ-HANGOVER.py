# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 18:10:40 2014

@author: girish
"""
ans_list = [] 
while(True):
    temp = float(input())
    if(temp == 0.00):
        break
    
    n=2
    
    sum1=0
    while(sum1<temp):
        sum1+=(1/n)
        n+=1
    n-=2
    ans_list.append(str(n)+" card(s)")
    
for i in range(len(ans_list)):
    print(ans_list[i])

