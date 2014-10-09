# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 23:56:53 2014

@author: girish
"""

import math
iteration = int(input())
ans_list=[]
for i in range(iteration):
    num = input().split()
    num = list(map(int,num))
    temp_ans = (num[0]-num[2])**2+(num[1]-num[3])**2
    temp_ans =round(math.sqrt(temp_ans)/2,6)
    ans_list.append(temp_ans)
print()
for j in range(iteration):
    print(ans_list[j])
