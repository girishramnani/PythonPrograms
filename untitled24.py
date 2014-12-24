# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 16:46:04 2014

@author: girish
"""

import PIL.Image as Im
import matplotlib.pyplot as plt
import numpy as np
image =Im.open("g.jpg").convert('L')
image.save("girish.jpg")
im =np.array(image)
t = np.shape(im)

plt.figure()

plt.plot(image)

'''the threshhold filter'''
#for i in range(t[0]):
#    for j in range(t[1]):
#        im[i][j]= 0 if im[i][j] <175 else 255
#        


'''the negative filter '''
#for i in range(t[0]):
#    for j in range(t[1]):
#        im[i][j]=abs(255-im[i][j])
img2 = Im.fromarray(im)
img2.save("girish123.jpg")