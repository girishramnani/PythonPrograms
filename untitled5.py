# -*- coding: utf-8 -*-
"""
Created on Fri Oct 24 16:30:57 2014

@author: girish
"""


print("enter each row on a seperate line and to terminate type 0")
li=list()
while(True):
    inter_li = input()
    if inter_li =='0':
        break
    inter_li = tuple(map(int,inter_li.split()))
    li.append(inter_li)
if li == []:
    print("you havent entered any matrix" )
    quit()
print("you entered : {}".format(li))
p = list(zip(*li))
t=len(p)-1
lis = [str(a)+str(b) for a in p[t] for b in p[t-1]]
t-=2
while len(lis[0]) != len(li[0]):
    lis = [ str(d)+str(c) for d in lis for c in p[t] ]
    t-=1
for j in lis:print(j)