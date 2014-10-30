# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 13:08:54 2014

@author: girish
"""

iteration= int(input())
for i in range(iteration):
    string = input()
    
    string =string.split(" ")
    for x in range(len(string)):
        
        if 'machula' in string[x]:
            del(string[x])
            break
    if string[0] =='+':
        ans = int(string[3])-int(string[1])
        print(ans,string[0],string[1],string[2],string[3])
    elif string[1] == '+' and string[3] !='=' :
        ans = int(string[3])-int(string[0])
        print(string[0],string[1],ans,string[2],string[3])
    else:
        ans = int(string[0])+int(string[2])
        print(string[0],string[1],string[2],string[3],ans)
        