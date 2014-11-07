# -*- coding: utf-8 -*-
"""
Created on Fri Nov  7 16:10:33 2014

@author: girish
"""

import functools
def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)

    if r > n:
        return
    indices = list(range(r))
    print(indices)

    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

def getallsets(li):
    anslist =[]

    for i in range(2,len(li)+1):
        anslist.extend(combinations(li,i))
    su = sum(li)
    
    for r in anslist:
        su+=functools.reduce(lambda x,y:x^y,r)
    return su

iteration = int(input())
for i in range(iteration):
    input()
    li = [int(x) for x in input().split()]
    print(getallsets(li))
        
        