# -*- coding: utf-8 -*-
"""
Created on Thu Sep 11 17:01:39 2014

@author: girish
"""

iteration = int(input())
ans_list=[]
for i in range(iteration):
    level =1
    no_of = int(input())
#    ite=100
#    while(True):
#        if(pow(ite,3,1000)==888):
#            if(level == no_of):
#                
#                ans_list.append(ite)
#                break
#            level+=1
#        ite+=1
#        
    ans_list.append((no_of-1)*250+192)
    
    
        
for k in range(iteration):
    print(ans_list[k])
        