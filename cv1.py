# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 14:45:46 2014

@author: girish
"""

import numpy

from scipy.ndimage import filters
from PIL import Image

from pylab import *
import os
numpy.broadcast_arrays
def denoise(im,U_init,tolerance=0.1,tau=0.125,tv_weight=100):
    m,n = im.shape# size of noisy image
    # initialize
    U = U_init
    Px=im# x-component to the dual field
    Py=im# y-component of the dual field
    error = 1
    while (error > tolerance):
        Uold = U
        # gradient of primal variable
        GradUx = roll(U,-1,axis=1)-U# x-component of U's gradient
        GradUy = roll(U,-1,axis=0)-U# y-component of U's gradient
        # update the dual varible
        PxNew = Px + (tau/tv_weight)*GradUx
        PyNew = Py + (tau/tv_weight)*GradUy
        NormNew = maximum(1,sqrt(PxNew**2+PyNew**2))
        Px = PxNew/NormNew# update of x-component (dual)
        Py = PyNew/NormNew# update of y-component (dual)
        # update the primal variable
        RxPx = roll(Px,1,axis=1)# right x-translation of x-component
        RyPy = roll(Py,1,axis=0)# right y-translation of y-component
        DivP = (Px-RxPx)+(Py-RyPy)# divergence of the dual field.
        U = im + tv_weight*DivP# update of the primal variable
        # update of error
        error = linalg.norm(U-Uold)/sqrt(n*m);
    return U,im-U
gir = array(Image.open("dirty.jpg"))


w = gir.shape

   

imshow(im)
plot((0,640),(0,480),'k')
plot((0,640),(480,0),'k')
show()




#fir = Image.open("images\\beach.jpg").convert('L')
#reg=fir.crop((500,500,2000,2000))
#reg = reg.transpose(Image.ROTATE_180)
#fir.paste(reg,(500,500,2000,2000))
#fir.save("giir.jpg")
