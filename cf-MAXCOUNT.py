# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 20:57:26 2014

@author: girish
"""
def Itemgetter(n):
    def item(w):
        return w[n]
    return item
    

iteration = int(input())
for i in range(iteration):
    freq = dict()
    x = int(input())
    li =[ int (w) for w in input().split()]
    for q in li:
        freq[q]= freq.get(q,0)+1
    m=max(freq.items(),key=Itemgetter(1))
    print(m[0]+" "+m[1])