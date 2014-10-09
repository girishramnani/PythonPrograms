from math import sin, cos, radians
from pyx import *

angle = 10
factor = 1.0 / (cos(radians(angle)) + sin(radians(angle)))

c=canvas.canvas()
c.text(0,0,"SDGSDG")
