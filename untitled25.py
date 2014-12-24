# -*- coding: utf-8 -*-
"""
Created on Fri Dec 19 17:40:17 2014

@author: girish
"""
from PIL import *
from pylab import *
from numpy import *

git = array(Image.open("girish123.jpg").convert("L"))

x =[100,100,400,800]
y=[200,300,500,900]

gray()

show()
def histogramEque(img,numb=256):
    im2 =array(Image.open(img).convert("L"))
    histo,bins = histogram(im2.flatten(),numb,normed=True)
    cdf=histo.cumsum()
    cdf =(255*cdf)/cdf[-1]
    ans = interp(im2.flatten(),bins[:-1],cdf)
    
    return ans.reshape(im2.shape)
im = Image.fromarray(int8(histogramEque("girish123.jpg")))

    
    