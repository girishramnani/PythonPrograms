# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 16:21:01 2014

@author: girish
"""

str1 = list(input())
str2 = list(input())
i=0
while i <len(str1):
    if str1[i] not in str2:
        del(str1[i])
    else:
        i+=1
i=0
while i <len(str2):
    if str2[i] not in str1:
        del(str2[i])
    else:
        i+=1
print(str1,str2)   
i=0
maxcount=float("-inf")
for i in range(len(str1)):
    count=0
    str3=str2.copy()
    if str1[i] in str3:
        str3 = str3[str3.index(str1[i])+1:]
        count+=1
        for j in range(i+1,len(str1)):
            if str1[j] in str3:
                str3=str3[str3.index(str1[j])+1:]
                count+=1
    if maxcount<count:
        maxcount=count
print(maxcount)
#        
#

