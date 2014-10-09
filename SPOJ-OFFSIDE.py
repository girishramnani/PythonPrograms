# -*- coding: utf-8 -*-
"""
Created on Fri Sep 26 20:38:26 2014

@author: girish
"""
def getFirstTwoElem(array,b):
    
    for i in range(b):
        max1=array[i]
        for j in range(i,len(array)):
            if max1 > array[j]:
                r=j
                temp=array[i]
                array[i]=array[r]
                array[r]=temp
    return array[0], array[1]
        
def helper(x,man2):
    
    if x<man2 :
        return "Y"
    return "N"
        
ans_list=[]               
    
    

while(True):
    a,b = [int(j) for j in input().split(" ")]
    if a==0 and b ==0:
        break
    x = input().split(" ")
    y = input().split(" ")
    x = list(map(int,x))
    y = list(map(int,y))
    man1,man2=getFirstTwoElem(y,b)
    temp = min(x)
    ans_list.append(helper(temp,man2))
    
for i in range(len(ans_list)):
    print(ans_list[i])
    
     
 


    