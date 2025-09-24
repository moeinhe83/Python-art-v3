# Library
from turtle import *
from colorsys import *

# Title
title("Art With Python")
bgcolor('black')
pensize(3)
speed(0)
h = 0

# Draw
for i in range(140):
    color = hsv_to_rgb(h, 1, 1)
    pencolor(color)
    h += 0.01
    circle(i, 100)
    right(80)
    circle(i, -50)
done()

# Create By Moein Heshmati
# Finish
# moeinit.com
