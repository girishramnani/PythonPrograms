# -*- coding: utf-8 -*-
"""
Created on Mon Sep  8 20:22:35 2014

@author: girish

"""


def ceil(num):
    if num%2==0:
        return int(num/2)
    return int((num+1)/2)

def no_of_square(num):
    no_f=1
    iterate_till =0
    if num %2 ==0:
        iterate_till =int(num/2)
    else :
        iterate_till =int((num+1)/2)
    for i in range(1,iterate_till+1):
        if num % i ==0 :
            print
            no_f+=1
        
    
    return ceil(no_f)


num = int(input())
su=0
for i in range(1,num+1):
    su+=no_of_square(i)
    
print(su)
    
            