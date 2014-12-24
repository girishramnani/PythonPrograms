# -*- coding: utf-8 -*-
"""
Created on Sun Oct 26 19:59:32 2014

@author: girish
"""

iteration = int(input())
for i in range(iteration):
    num = int(input())
    if num <2:
        print("Ordinary Number")
        continue
    div =2
    oddpow=0
    evenpow=0
    tempcount=0
    while num>1:
        while num%div==0:
            num/=div
            tempcount+=1
            
        
        if tempcount >0:
            
            if  tempcount%2==0:
                evenpow+=1
            else:
                oddpow+=1
        div+=1
        tempcount=0
    print("Ordinary Number") if oddpow>evenpow else print("Psycho Number")
            
        