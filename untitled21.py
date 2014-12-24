# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 00:08:49 2014

@author: girish
"""

def acode_second_try(s):
    n = len(s)
    f = [0 for i in range(1 + n)]
    f[n] = 1
    for i in range(n - 1, -1, -1):
        j=s[i]
        if s[i] != '0':
            f[i] = f[1 + i]
            if 1 + i < n:
                if 10 * int(s[i]) + int(s[1 + i]) <= 26:
                    f[i] += f[2 + i]
    return f[0]



i = input().strip()
while i[0] != '0':
	print(acode_second_try(i))
        
	i = input().strip()

