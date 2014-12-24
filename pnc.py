# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 12:16:01 2014

@author: girish
"""
li=[]
def factfun(t):
    li.append(0)
    fact=1
    for i in range(1,t+1):
        li.append(fact)
        fact*=i
    
di = dict()
word = input()
for i in word:
    di[i]=di.get(i,0)+1

t = len(word)
deno =1
for z in di.values():
    deno*=factfun(z)
print(factfun(t)//deno)


    

    