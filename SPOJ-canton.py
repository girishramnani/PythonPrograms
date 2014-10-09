# -*- coding: utf-8 -*-
"""
Created on Sun Sep 14 21:08:24 2014

@author: girish
"""
def getlastadder(num):
    ans=1
    f=1
    while(ans<num):
        f+=1
        ans+=f
        
    print(f)
        
    
    
getlastadder(14)
        