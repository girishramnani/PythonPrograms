# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 17:57:46 2014

@author: girish
"""
def createDict(t1):
    t= dict()
    for z in t1:
        t[z] = t.get(z,0)+1
    return t
wr = input()
word = createDict(wr)
bo = len(wr)%2 ==1
oddlen=0
for v in word.values():
    oddlen+=(v&1)
if bo and oddlen<2:
    print("YES")
else:
    print("NO")
    

