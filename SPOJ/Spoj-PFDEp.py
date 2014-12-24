# -*- coding: utf-8 -*-
"""
Created on Wed Oct 15 21:06:59 2014

@author: girish
"""
def removedDependencies(wlist , num):
    for j in wlist.values():
        if num in j:
            j.remove(num)
    

a,b = [int(x) for x in input().split()]
wlist = {x:[] for x in range(1,a+1)}
for i in range(b):
    q = [int(w) for w in input().split()]
    constraint = q[2:]
    wlist[q[0]].extend(constraint)

bol = True
while(len(wlist)>0 and bol):
    bol =False
    for j in wlist.keys():
        if len(wlist[j]) == 0:
            removedDependencies(wlist,j)            
            print(j,end=" ")
            del(wlist[j])
            
            bol=True
            break
print()
        

