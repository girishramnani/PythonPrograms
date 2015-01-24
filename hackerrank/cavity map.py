# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:01:14 2015

@author: Girish
"""
li=[]
for x in range(int(input())):
    li.append(list(map(int,input())))
def check(li,x,y):
    moves = [(-1,0),(1,0),(0,1),(0,-1)]
    for i,j in moves:
        if li[x][y] < li[x+i][y+j]:
            return False
    return True
    
for x in range(len(li)):
    for y in range(len(li)):
        if x==0 or x==(len(li)-1) or y==0 or y==(len(li)-1):
            print(li[x][y],end="")
        else:    
            if check(li,x,y):
                print("X",end="")
            else:
                print(li[x][y],end="")
    print()
        
    
    