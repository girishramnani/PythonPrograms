# -*- coding: utf-8 -*-
"""
Created on Tue Jan 20 21:18:50 2015

@author: Girish
"""



for x in range(int(input())):
    input()
    li = [int(x) for x in input().split()]
    
    t2 = sum([x for x in li if x>0])
    
    c=0
    m1=0
    m2=0
    for x in li:
        m1+=x
        if m1<0:
            m1=0
        if m1>m2:
            m2=m1
    
        
    
    print(m2,t2)
 