# -*- coding: utf-8 -*-
"""
Created on Tue Nov  4 19:36:35 2014

@author: girish
"""
iteration = int(input())
for i in range(iteration):
    n = int(input())
    li = [ int(x) for x in input().split()]
    
    ans = [0 for _ in range(n+1)]
    optimizedSol(li,)
def optimizedSol(li,length,ans):
    
    for i in range(length):
        q=0
        for j in range(0,3):
            q=max(q,sol[j]+ans[3-j])
        ans[i]=q
    print(ans[])
        
            
    

    