# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 18:39:31 2014

@author: girish
"""

takein = [ int(x) for x in input().split()]
nos = takein[0]
take = takein[1:]
work = list()
freq = list()

last=0
anslist =[] 
anslist.append(take.copy())
for qq in range(nos):
    wokr = len(take)
    count=0
    t=0
    while t<wokr:
        
        if count==0:
            work.append(take[t])
            count+=1
            t+=1
        elif work[-1] == take[t]:
            while(work[-1]==take[t]):
                count+=1
                t+=1
                if t >=wokr:
                    break
            freq.append(count)
            count=0
        else:
            freq.append(count)
            count=0
    if count!=0:
        freq.append(count)
    take.clear()
    for i in range(len(freq)):
#        print(freq[i],work[i],end=" ")
        take.append(freq[i])
        take.append(work[i])
        
    
    
    anslist.append(take.copy())
    freq.clear()
    work.clear()
    last = len(take)
    
    
max1 = len(max(anslist,key = lambda x : len(x)))

for z in range(len(anslist)):
    removal=0
    nodot = abs(int(len(anslist[z])-max1))
    for q in range(nodot):
        print(".",end="") 
    for a in range(len(anslist[z])):
        if a!=len(anslist[z])-1:
            print(anslist[z][a],end=" ")
            removal+=len(str(anslist[z][a]))-1
            
        else:
            print(anslist[z][a],end="")
    for q in range(nodot-removal):
        print(".",end="")
    print()
max1 = len(max(anslist[1:],key = lambda x : len(x)))
print(max1)
        
    
        
   

        
