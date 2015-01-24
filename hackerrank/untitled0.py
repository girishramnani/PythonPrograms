# -*- coding: utf-8 -*-
"""
Created on Tue Jan 13 08:50:54 2015

@author: Girish
"""
import faulthandler
faulthandler.enable
def undwind(f):
    def word(*args):
        return "hello" + f(*args)
    return word
@classmethod
def work():
    return " he he"

t= work()
print(work())
t = input()
t2 = "bob"
i =0
k = len(t2)
count=0
while i<(len(t)-len(t2)+1):
    
    flag = True
    if t2[0] == t[i]:
        for j in range(1,len(t2)):
        
            if t[i+j] != t2[j]:
                flag = False
        if flag:
            count+=1
    i+=1
print(count)

