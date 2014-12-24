# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 11:49:22 2014

@author: girish
"""

def checkPalindrome(word,index=None):
    i=0
    j=len(word)-1
    while not i >=j:
        if i ==index:
            i+=1
        elif j==index:
            j-=1
        else:
            if word[j] != word[i]:
                return False
            i+=1
            j-=1
            
    return True

for i  in range(int(input())):
    t = input()
    if checkPalindrome(t):
        print(-1)
        continue
    for x in range(len(t)):
        if checkPalindrome(t,x):
            print(x)
            break
    else:
        print(-1)
    