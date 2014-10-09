# -*- coding: utf-8 -*-
"""
Created on Sun Sep  7 13:24:07 2014

@author: girish
"""
import numpy
import matplotlib
import pylab


GRAPH9 = {0: set([1, 2, 3, 4, 5, 6]),
          1: set([0, 2, 3, 4, 5, 6]),
          2: set([0, 1, 3, 4, 5, 6]),
          3: set([0, 1, 2, 4, 5, 6]),
          4: set([0, 1, 2, 3, 5, 6]),
          5: set([0, 1, 2, 3, 4, 6]),
          6: set([0, 1, 2, 3, 4, 5]),
          7: set([1, 3, 4, 6]),
          8: set([0, 3, 4, 5, 6]),
          9: set([0, 5, 6, 7]),
          10: set([1, 2, 4, 9]),
          11: set([1, 2, 4, 6]),
          12: set([0, 2, 4, 6]),
          13: set([1, 2, 4, 5]),
          14: set([0, 1, 4, 6]),
          15: set([1, 4, 5, 6]),
          16: set([0, 1, 2, 4, 6]),
          17: set([0, 1, 2, 4, 5, 6]),
          18: set([2, 4, 5, 6, 13]),
          19: set([1, 2, 3, 5, 6]),
          20: set([0, 1, 2, 4, 5]),
          21: set([1, 2, 4, 5, 15]),
          22: set([0, 9, 4, 5, 13]),
          23: set([0, 1, 2, 3, 5, 20]),
          24: set([0, 1, 2, 3, 4, 5, 6]),
          25: set([0, 1, 2, 4, 5]),
          26: set([1, 2, 4, 5, 10, 22]),
          27: set([1, 2, 3, 5, 6]),
          28: set([0, 1, 3, 5]),
          29: set([2, 26, 4, 5, 6]),
          30: set([0, 2, 4, 6, 7]),
          31: set([20, 4, 21, 6]),
          32: set([1, 2, 4, 20, 28]),
          33: set([0, 4, 5, 6, 8, 22]),
          34: set([0, 2, 4, 5, 15]),
          35: set([1, 2, 5, 6, 9, 28]),
          36: set([24, 2, 3, 4, 6]),
          37: set([0, 1, 2, 4, 6, 10, 29]),
          38: set([0, 24, 11, 5, 6]),
          39: set([0, 1, 22, 6, 17]),
          40: set([0, 1, 2, 3, 5, 15]),
          41: set([11, 2, 3, 5, 6]),
          42: set([16, 1, 2, 5]),
          43: set([0, 1, 2, 4, 22]),
          44: set([32, 3, 6, 24, 27, 29]),
          45: set([1, 2, 4, 5, 16, 18, 37]),
          46: set([1, 5, 6, 7, 8, 12, 14]),
          47: set([8, 20, 2, 4]),
          48: set([0, 16, 2, 5, 14]),
          49: set([2, 21, 18, 6, 15])}



def load_graph(graph_url=0):
    print("entered the function")
    """
    Function that loads a graph given the URL
    for a text representation of the graph

    Returns a dictionary that models a graph
    """
    graph_file = open("alg_phys-cite.txt")
    print("opened the url")
    graph_text = graph_file.read()
    print("read the file")
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]

    print ("Loaded graph with" + str(len(graph_lines)) + "nodes")

    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))
    print("graph returned")
    return answer_graph



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

Plot = in_degree_distribution(load_graph())
print("generated distribution graph")
matplotlib.pyplot.bar(Plot.values(),Plot.keys(),1,10,log=True)


