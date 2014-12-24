# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 12:59:30 2014

@author: girish
"""
import numpy
import PIL.Image as im 
x= im.open("ww.jpg")
out=x.resize((10000,8000))
t = numpy.asarray(out)
print(numpy.shape(t))
