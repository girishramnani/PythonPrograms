# -*- coding: utf-8 -*-
"""
Created on Fri Oct  3 02:19:20 2014

@author: girish
"""

def removeCommon(li1,li2):
    for i in li1:
        if i in li2:
            li2.remove(i)
    return li2

iteration = int(input())

for i in range(iteration):
    letterFor=list()
    letterRiv=list()
    
    internal= int(input())
    for j in range(internal):
        word=str(input())
        
        letterRiv.append(word[0])
        letterFor.append(word[-1])
    if len(removeCommon(letterRiv,letterFor)) ==1:
        print("Ordering is possible.")
    else:
        print("The door cannot be opened.")        
    

    
        