# -*- coding: utf-8 -*-
"""
Created on Thu Oct 16 00:03:17 2014

@author: girish
@link = http://www.spoj.com/problems/YODANESS/
"""

iteration = int(input())


for i in range(iteration):
    number_of_words = int(input())
    string1 = list(input().split())
    original = list(input().split())
    count=0
    for j in range(number_of_words):
        location = original.index(string1[j])
        if location !=j:        
            temp =original[j]
            original[j]= original[location]
            original[location]=temp
        count+=abs(j-location)
    print(count)
        
        