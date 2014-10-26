# -*- coding: utf-8 -*-
"""
Use only python 3.2.x or above

Created on Fri Oct 24 16:30:57 2014

@author: girish

havent handled the exception for empty matrix so dont enter an empty matrix
i have tested this program in many test cases and it gives ans for all .
and also no external package has been used (as u can see there are no import statements)

example testcase #1:
1 2 3 4       here dont leave any space after 4 or else exception will be thrown
5 6 7 8
0

example output #1:
4321
4325
4361
4365
4721
4725
4761
4765
8321
8325
8361
8365
8721
8725
8761
8765

here the program terminates when it receives a 0
the I/O method can be changed easily
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
    
print("you entered : {}".format(li))
p = list(zip(*li))
t=len(p)-1
lis = [str(a)+str(b) for a in p[t] for b in p[t-1]]
t-=2
while len(lis[0]) != len(li[0]):
    lis = [ str(d)+str(c) for d in lis for c in p[t] ]
    t-=1
for j in lis:print(j)
input()