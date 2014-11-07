# -*- coding: utf-8 -*-
"""
Created on Thu Nov  6 03:25:59 2014

@author: girish
"""

st =input()
st=st.lower()
st = "".join(st.split(" "))

li=set(st)
print(li)
if len(li)!=26:
    print("not pangram")
else:
    print("pangram")
    
   