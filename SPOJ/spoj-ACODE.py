# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 19:51:53 2014

@author: girish
"""
lookup = dict()
def reAcode(li):
    if lookup.get(li,-1) !=-1:
        return lookup.get(li)
    if int(li)<=26 and int(li)>10 and int(li)!=20:
        return 2
    elif int(li)<=10 or int(li)==20:
        if int(li) !=0:
            return 1
    else:
        p=0
        q=0
        if int(li[:2]) ==10 or int(li[:2]) ==20:
            q=reAcode(li[2:])
        else:
            if int(li[:1]) > 0:
                p=reAcode(li[1:])
            if int(li[:2])<=26:
                if int(li[2])!=0:
                    q= reAcode(li[2:])
        if p == None:
            z= q
        elif q == None : 
            z = p
        else:
            z=p+q
        lookup[li]=z
        return z
        
            
        
    
def Acode(letter):
    queue = list()
    queue.append(letter)
    lookup=dict()
    ans=0
    tempsum=0
    while(queue):
        
        li = queue[-1]
        if len(li)<2:
            
            tempsum=0
        del(queue[-1])
        if int(li) <=26 and int(li)>10 and int(li)!=20:
            ans+=2
            tempsum+2
        elif ( int(li)  <= 10  ) or int(li)==20:
            if int(li) !=0:
                
                ans+=1
                tempsum+=1
        else:
            if int(li[:2]) ==10 or int(li[:2]) ==20:
                queue.append(li[2:])
            else:
                if int(li[:1]) > 0:
                    queue.append(li[1:])
                if int(li[:2])<=26:
                    if int(li[2])!=0:
                        
                        queue.append(li[2:])
    return ans

while(True):
    t = input()
    if int(t)==0:
        break
    else:
        print(reAcode(t))

    
    