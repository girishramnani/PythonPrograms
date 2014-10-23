# -*- coding: utf-8 -*-
"""
Created on Thu Oct 23 14:38:27 2014

@author: girish
"""

iteration = int(input())
filewr = open("data.txt","w")

for j in range(1,iteration+1):

    intial=1
    initailinc=1
    inital2=intial+initailinc
    for z in range(j-1):
        initailinc*=2
        intial =intial+inital2
        inital2=intial+initailinc
    
    filewr.write(str(intial%1000000007)+",")
    filewr.flush()
    
        
        
        
    
#    print("Case {}: {}".format(j+1,accum(li)))
    