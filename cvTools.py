# -*- coding: utf-8 -*-
"""
Created on Fri Oct 17 18:19:28 2014

@author: girish
"""
import os


from scipy.ndimage import filters
from PIL import Image
from numpy import *

def get_images(path):
    
    return [os.path.join(path,f) for f in os.listdir(path) if f.endswith(".jpg")]

def imresize(im,sz):
    img = Image.fromarray(uint8(im))
    img = img.resize((sz))
    return array(img)
    
def compute_average(imlist):
        try:
            average +=array(Image.open(imname))
        except:
            print (imname + " ..skipped")
        average /= len(imlist)
    return array(average, 'uint8')
                
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
    
