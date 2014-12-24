# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 20:02:15 2014

@author: girish
"""
def wrapper(f):
    
    def func(args,he):
        print(he)
        print("am")
        return f(args)
    return func
    
@wrapper
def girihs(st):
    print(st)


girihs("work","I")
#class gir(Exception):
#    def __cause__(self):
#        return "he haha"
#    def __repr__(self):
#        return "self made exception"
#    def __str__(self):
#        
#        return self.__repr__()
#        
#try:
#    raise gir
#except gir as g:
#    print(g)
    