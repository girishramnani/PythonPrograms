# -*- coding: utf-8 -*-
"""
Created on Sun Sep 21 14:10:52 2014

@author: girish
"""

iteration = int(input())
ans_list=[]
question_list = []
for j in range(iteration):
    temp = input().split(" ")
    temp = list(map(int,temp))
    question_list.append(temp)
for i in range(iteration):

    n=(2*question_list[i][2])/(question_list[i][0]+question_list[i][1])
    d=(question_list[i][1]-question_list[i][0])/(n-5)
    a=question_list[i][0]-(2*d)
    ans_list.append([int(a),int(n),int(d)])

for i in range(iteration):
    print(ans_list[i][1])
    for j in range(ans_list[i][1]):
        print((ans_list[i][0]+(j*ans_list[i][2])),end=" ")
    