# -*- coding: utf-8 -*-
"""
Created on Sat Nov  8 17:09:52 2014

@author: girish
"""
def multidisplay(x,y):
    product=int(x)*int(y)
    productLength = len(str(product))
    print(" "*(productLength-len(x))+x)
    for z in range(productLength-len(y)-1):
        print(" ",end="")
    print("*",end="")
    print(y)
    if len(y)!=1:
        print(" "*(productLength-len(y)-1)+"-"*(len(y)+1))
        for z in range(len(y)):
            ans=int(x)*int(y[-1-z])
            print(" "*(productLength-len(str(ans))-z),end="")
            print(ans)
        
    
    print("-"*(productLength))
    print(product)
    
        
    
    
        
def sumdisplay(x,y):
    sp = max(len(x),len(y))
    sp +=1
    for z in range(sp-len(x)):
        print(" ",end="")
    print(x)
    print("+",end="")
    for z in range(sp-len(y)-1):
        print(" ",end="")
    print(y)
    for z in range(sp):
        print("-",end="")
    print()
    t=int(x)+int(y)
    
    for z in range(sp-len(str(t))):
        print(" ",end="")
    print(t)
def subdisplay(x,y):
    sp = max(len(x),len(y))
    sp +=1
    for z in range(sp-len(x)):
        print(" ",end="")
    print(x)
    print("-",end="")
    for z in range(sp-len(y)-1):
        print(" ",end="")
    print(y)
    for z in range(sp):
        print("-",end="")
    print()
    t=int(x)-int(y)
    
    for z in range(sp-len(str(t))):
        print(" ",end="")
    print(t)
    
    
iteration = int(input())
for i in range(iteration):
    word=input()
    if '+' in word:
        l = word.split("+")
        sumdisplay(l[0],l[1])
    elif '-' in word:
        l = word.split("-")
        subdisplay(l[0],l[1])
    else:
        t = word.split("*")
        multidisplay(t[0],t[1])
    print()
    
        