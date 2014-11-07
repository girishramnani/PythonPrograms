# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 17:40:50 2014

@author: girish
"""

graph = {'A': [ 'E', 'B'], 
    'B':  ['F','A', 'E'] ,
    'C':[ 'D' ,'G', 'F'], 
    'D':  ['G', 'C' ,'H' ],
    'E': [ 'A' ,'F', 'B'] ,
    'F':  ['B', 'E', 'C'], 
    'G':  ['D', 'C'], 
    'H':  ['D'] }
    


def bfs(graph):
    queue=[]
    visited=[]
    queue.append('A')
    while(queue):
        x = queue[0]
        
        del(queue[0])
        
        
        
        if not (x in visited):
            print(x,end=" ")
            queue.extend(graph[x])
            visited.append(x)
            
bfs(graph)