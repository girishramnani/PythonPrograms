# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 00:59:43 2014

@author: girish
"""
import collections

iteration = int(input())-1
tree = collections.OrderedDict()

li = [int(x) for x in input().split()]
for x in range(iteration):
    a,b = [int(x) for x in input().split()]
    if tree.get(a)==None and tree.get(b)==None:
        tree[a] = [b]
    elif tree.get(a)==None:
         tree[b].append(a)
    else:
        tree[a].append(b)

    
print(tree)