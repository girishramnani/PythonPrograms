# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 23:01:57 2014

@author: girish
"""
import pythonds
pythonds.
def lps(word):

   n = len(word);
   
   L=[[0 for _ in range(n)] for _ in range(n)]  
 
   for i in range(n):
      L[i][i] = 1;
 
   for cl in range(2,n+1):
    
        for i in range(n-cl+1):
        
            j = i+cl-1;
            if (word[i] == word[j] and cl == 2):
               L[i][j] = 2;
            elif (word[i] == word[j]):
               L[i][j] = L[i+1][j-1] + 2;
            else:
               L[i][j] = max(L[i][j-1], L[i+1][j]);
   
   return L[0][n-1];

k=input()
print(lps(str(input())))