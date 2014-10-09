# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 14:20:22 2014

@author: girish
"""
import math

def isPrime(n):
    if n%2 == 0:
        return False
    else:
        for i in range(3,int(math.sqrt(n)),2):
            if n%i==0:return False
        return True


iteration = int(input())
for j in range(iteration):
    
    nth = int(input())
    if nth == 1:
        print (2)
    elif nth ==2:
        print(3)
    elif nth ==3:
        print(5)
    elif nth == 4:
        print(7)
    elif nth ==5:
        print(11)
    else:
        low =(nth*(math.log(nth)))+(nth*math.log(math.log(nth)))-nth
        low = int(low)        
        up = int(low+nth)
        
        print(low , up)
        
    