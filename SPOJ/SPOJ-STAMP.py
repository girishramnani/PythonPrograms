# -*- coding: utf-8 -*-
"""
Created on Wed Sep 17 01:20:31 2014

@author: girish
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Sep 16 08:43:19 2014

@author: girish
"""

iteration = int(input())
ans_list=list()

for i in range(iteration):
    ans_num=0
    ans_count=0
    num = input().split(" ")
    num = list(map(int,num))
    friend_list=input().split(" ")
    
    friend_list = list(map(int,friend_list))
    friend_list.sort()
    #1print(friend_list)
    for k in range(num[1]):
        ans_num+=friend_list.pop()
        ans_count+=1
        if ans_num>=num[0]:
            break
    
    if ans_num>=num[0]:
        ans_list.append(str(ans_count)+"\n")
    else:
        ans_list.append("impossible\n")
for q in range(len(ans_list)):
    print("Scenario #"+str(q+1)+":")
    print(ans_list[q])
    