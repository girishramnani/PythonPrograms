# -*- coding: utf-8 -*-
"""
Created on Thu Feb  5 12:04:32 2015

@author: Girish
"""

# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 20:30:41 2015

@author: Girish
"""

for z in range(int(input())):
    input()
    bol=False
    li = [int(x) for x in input().split()]
    su1=0
    ts=sum(li)
    for z in range(1,len(li)):
        su1 +=li[z-1]
        su2 = ts-su1
        if su1 ==su2:
            print("YES")
            bol = True
            break
    if not bol :
        print("NO")