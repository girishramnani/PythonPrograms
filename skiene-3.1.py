# -*- coding: utf-8 -*-
"""
Created on Thu Oct  9 18:34:28 2014

@author: girish
"""


def comp():
    paralist = list(input())
    arangedList = []
    for i in range(len(paralist)):
        if paralist[i]=="(":
            arangedList.append(paralist[i])
        elif paralist[i] == ")" and len(arangedList) ==0 :
            return False
        else:
            arangedList.pop()
    if len(arangedList) == 0:
        return True
        
            
print(comp())        