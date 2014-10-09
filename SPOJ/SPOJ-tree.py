# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 20:38:44 2014

@author: girish
"""
bol =True
graph = {}
a,b = [ int(x) for x in input().split(" ") ]
for j in range(1,a+1):
    graph[j]=set([])
    
for i in range(b):
   node1,node2 = [int(y) for y in input().split(" ")]
   
   if node2 in graph[node1]:
       print("NO")
       bol= not bol
       break
   else:
       graph[node1].add(node2)
       graph[node2].add(node1)
       
       
if bol:
    print("YES")