# -*- coding: utf-8 -*-
"""
Created on Wed Dec 10 22:37:28 2014

@author: girish
"""
def checkPalindrome(word):
    return word[::-1]==word
iteration = int(input())
for i in range(iteration):
    boo = True
    word = input()
    
    for x in range(len(word)):
        if checkPalindrome(word[:x]+word[x+1:]):
            print(x)
            boo = False
            break
    if boo:
        print(-1)
        
            
       
 