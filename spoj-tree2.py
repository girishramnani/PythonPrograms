# -*- coding: utf-8 -*-
"""
Created on Mon Sep 22 21:21:31 2014

@author: girish
"""


def is_a_tree():
    
    a,b = [ int(x) for x in input().split(" ") ]
    li = []
    
    for i in range(b):
        j=0
        node1,node2 = [int(y) for y in input().split(" ")]
      
        if len(li) == 0 :
            li.append([node1,node2])
        else:
            while j<len(li):
           
                if node1 and node2 in li[j]:
                    return "NO"
                    break
                elif node1 in li[j]:
                    li[j].append(node2)
                    j+=1
                elif node2 in li[j]:
                    li[j].append(node1)
                    j+=1
                else:
                    li.append([node1,node2])
                    j+=1
    return "YES"
              
print(is_a_tree())