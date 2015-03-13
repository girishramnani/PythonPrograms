# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 16:20:05 2015

@author: Girish
"""
t2=63303212889375877567328165411288303907410870625225931671654121339922293885519921
def factmul(n):
    li=1
    i=0
    ans=1
    for j in range(2,n+1):
        li=(li*j)
        ans=(ans*li)
        i+=1
    
    return ans
for x in range(int(input())):
    t = int(input())

    print("Case {}: {}".format(x,factmul(t)%63303212889375877567328165411288303907410870625225931671654121339922293885519921))
        