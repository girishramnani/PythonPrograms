# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 17:38:57 2014

@author: girish
"""

def naive_max_perm(M, A=None): 
    if A is None: # The elt. set not supplied? 
        A = set(range(len(M))) # A = {0, 1, ... , n-1} 
    if len(A) == 1: return A # Base case -- single-elt. A 
    B = set(M[i] for i in A) # The "pointed to" elements 
    C = A - B # "Not pointed to" elements 
    if C: # Any useless elements? 
        A.remove(C.pop()) # Remove one of them 
        return naive_max_perm(M, A) # Solve remaining problem 
    return A
M = [2, 2, 0, 5, 3, 5, 7, 4]


def Per_max(M):
    count = [0 for i in range(len(M))]
    w = set(range(len(M)))
    
    for  i in M:
        count[i]+=1
    Q= [j for j in range(len(M)) if M[j]==0]
    while Q:
        x = Q.pop()
        w.remove(x)
        ww=M[x]
        count[ww]-=1
        if count[ww]==0:
            Q.append(ww)
    
    
    
print(Per_max(M))