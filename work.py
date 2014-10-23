# -*- coding: utf-8 -*-
"""
Created on Sat Oct 18 12:08:18 2014

@author: girish
"""

import PIL

from scipy.ndimage import filters
from PIL import Image

from pylab import *
import os

im = PIL.Image("banana.jpg")
plot(im)