# -*- coding: utf-8 -*-
"""
Created on Sat Dec 13 22:44:03 2014

@author: girish
"""
import numpy
import random
def randomMatrix(n):
    r=[]
    for i in range(n):
        r.append([random.random() for i in range(n)])
    base = numpy.array(r).reshape((n,n))
    return base
def po(a,b): 
    if b==0:
        return numpy.identity(len(a))
    if b==1:
        return a
    if b%2==0:
        return po(a.dot(a),b//2)
    return a.dot(po(a,b-1))

