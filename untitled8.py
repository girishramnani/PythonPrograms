# -*- coding: utf-8 -*-
"""
Created on Fri Oct 31 16:53:04 2014

@author: girish
"""

def insertionSort(li):
    l = len(li)
    for i in range(1,l):
        temp = li[i]
        j=i-1
        while li[j]>temp and j>=0:
            li[j+1]=li[j]
            j-=1
        li[j+1]=temp
        
        for z in li:
            print(z,end=" ")
        print()
intake = int(input())
li = [ int(x) for x in input().split()]
insertionSort(li)