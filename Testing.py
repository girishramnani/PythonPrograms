# -*- coding: utf-8 -*-
"""
Created on Thu Sep  4 21:22:04 2014

@author: girish
"""


EX_GRAPH0 = { 0:set([1,2]),
              1:set([]),
              2:set([])}

EX_GRAPH1 = { 0:set([1,4,5]),
              1:set([2,6]),
              2:set([3]),
              3:set([0]),
              4:set([1]),
              5:set([2]),
              6:set([])}
              
EX_GRAPH2 = { 0:set([1,4,5]),
              1:set([2,6]),
              2:set([3,7]),
              3:set([7]),
              4:set([1]),
              5:set([2]),
              6:set([]),
              7:set([3]),
              8:set([1,2]),
              9:set([4,5,6,7,3,0])}
   
    
def make_complete_graph(num_nodes):
    
    """
    this function provides a directed graph with 
    maximum edges possible   
    """    

    graph = dict()
    for dummy_i in range(num_nodes):
        graph[dummy_i] = set([values for values in range(num_nodes)])
        graph[dummy_i].remove(dummy_i)
    return graph

def compute_in_degrees(digraph):
    
    """  
    this function provides the in_degree for 
    each node in the digraph
    """
    
    output_graph=digraph.fromkeys(digraph)
    for dummy_i in digraph.keys():
        output_graph[dummy_i] = 0
    for dummy_j in digraph.keys():
        for dummy_k in digraph.keys():
            if dummy_j in digraph.get(dummy_k):
                output_graph[dummy_j]+=1
            
    return output_graph

def in_degree_distribution(digraph):
    
    """ 
    this method provides the unnormalized distribution of in_degree using the 
    compute_in_degree method
    """
    
    dummy_graph = compute_in_degrees(digraph)
    output_graph = dict()
    set_list = set(dummy_graph.values())
    
    for dummy_i in set_list:
        for dummy_j in dummy_graph.values():
            if dummy_i == dummy_j:
                
                if output_graph.get(dummy_i) == None:
                    output_graph[dummy_i]=1
                else :
                    output_graph[dummy_i]+=1
    return output_graph

