# Use turtle graphics to make an infinite spiral
import turtle
from turtle import *

speed(1000)
i = 0.01
while True:
    i +=0.01
    forward(i)
    right(5)