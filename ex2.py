# make infinite circles, start with a small circle, then draw a bigger circle around it
import turtle
from turtle import *
speed(1000)
x=0
while True:
    x+=1
    for i in range(72):
        forward(x)
        right(5)
    penup()
    left(90)
    forward(10)
    right(90)
    backward(1)
    pendown()