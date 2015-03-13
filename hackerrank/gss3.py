# -*- coding: utf-8 -*-
"""
Created on Fri Jan 30 12:26:51 2015

@author: Girish
"""

class Node:
    def __init__(self):
        self.value=None
        self.left=None
        self.right =None



def add_to_tree(num,node):
    if node.value == None:
        node.value = num
    elif node.value >num:
        if node.left ==None:
            node.left=Node()
        add_to_tree(num,node.left)
    else:
        if node.right ==None:
            node.right=Node()
        add_to_tree(num,node.right)
    

def segment_tree(li,tree,low,high):
    if abs(low-high)==1:
        tree.value=li[low]
    else:
        tree.value = sum(li[low:high])
        print(tree.value)
        if tree.left ==None:
            tree.left = Node()
        mid =(low+high)//2
        segment_tree(li,tree.left,low,mid)
        if tree.right ==None:
            tree.right = Node()
        segment_tree(li,tree.right,mid,high)
 
x= Node()
segment_tree([1,2,3,4],x,0,4)      
def getsum(in1,in2,low=0,high=4,tree=x):
    if in1==low and in2 ==high:
        return tree.value
    
    
    