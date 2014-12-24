# -*- coding: utf-8 -*-
"""
Created on Sun Dec 21 13:37:14 2014

@author: girish
"""

no =0
st=set()
li2=[]
def isSubsetSum(li,su,n):
   
    

a ,b =[int(x) for x in input().split()]
li = [int(input()) for z in range(a)]
print(isSubsetSum(li,b,sum(li)))
   