# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 12:18:32 2014

@author: girish
"""
def createDict(t1):
    t= dict()
    for z in t1:
        t[z] = t.get(z,0)+1
    return t
for i in range(int(input())):
    t = input()
    if len(t) & 1:
        print(-1)
        continue
    t1=t[:len(t)//2]
    t2=t[len(t)//2:]
    
    ans=0
    for i in range(len(t1)):
        if t1[i] in t2:
            l = t2.index(t1[i])
            t2 = t2[:l]+t2[l+1:]
        else:
            ans+=1
    print(ans)
        
        
    
    print(ans)
    
            
            
    
    