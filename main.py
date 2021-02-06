from graphics.circle import carea 
from graphics.circle import cperi
import graphics.rect
from graphics.dgraphics.sphere import sarea as a
from graphics.dgraphics.sphere import speri as p
from graphics.dgraphics.cuboid import *

l,m,n=2,3,4
print("****** CIRCLE*****")
print("Area:",carea(l))
print("Perimeter",cperi(l))
print("---------------------------------")
print("****** RECTANGLE*****")
print("Area:",graphics.rect.rarea(l,m))
print("Perimeter",graphics.rect.rperi(l,m))
print("---------------------------------")
print("****** SPHERE*****")
print("Area:",a(n))
print("Perimeter",p(n))
print("---------------------------------")
print("****** CUBOID*****")
print("Area:",cbarea(l,m,n))
print("Perimeter",cbperi(l,m,n))
print("---------------------------------")