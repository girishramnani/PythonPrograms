# -*- coding: utf-8 -*-
"""
Created on Thu Oct 30 01:37:31 2014

@author: girish
"""


dictionary = dict()
iteration = int(input())
for i in range(iteration):
    
    li = int(input())
    inpu = input()
    dictionary = {'TTT':0,'TTH':0,'THT':0,'THH':0,'HTT':0,'HTH':0,"HHT":0,'HHH':0}
    for l in range(len(inpu)-2):
        dictionary[inpu[l:l+3]]+=1
    print(li,dictionary['TTT'],dictionary['TTH'],dictionary['THT'],dictionary['THH'],dictionary['HTT'],dictionary['HTH'],dictionary['HHT'],dictionary['HHH'])
    