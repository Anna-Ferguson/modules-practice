import turtle
import random

def reset():
    turtle.clearscreen()

def setup():
    turtle.speed(0)
    turtle.screensize(1000,800)

def setrandomcolor():
    n = random.randint(1,4)
    if n ==1:
        turtle.color("blue")
    if n == 2:
        turtle.color("red")
    if n == 3:
        turtle.color("green")
    if n == 4:
        turtle.color("purple")


def drawrectangle(width, height):
    setrandomcolor()
    for i in range(2):
        turtle.forward(width)
        turtle.left(90)
        turtle.forward(height)
        turtle.left(90)

def done():
    turtle.done()

def drawAllrectangles (x,y, width, height, rotation, offset, count):
    r = 360/count
    turtle.pu()
    turtle.setheading(rotation)
    turtle.setposition(x, y)
    turtle.pd()
    for i in range(count):
        turtle.pu()
        turtle.forward(offset)
        turtle.pd()
        drawrectangle(width, height)
        turtle.pu()
        turtle.backward(offset)
        turtle.left(r)

def drawcircle (x,y, offset, count, radius):
    r = 360/count
    turtle.pu()
    turtle.setposition(x,y)
    for i in range(count):
        setrandomcolor()
        turtle.pu()
        turtle.forward(offset+radius)
        turtle.pd()
        turtle.circle(radius)
        turtle.pu()
        turtle.backward(offset+radius)
        turtle.left(r)

def superpattern(x,y, width, height, rotation ,offset, count,radius):
    for i in range(count):
        x = random.randint(-200,200)
        y = random.randint(-200,200)
        a = random.randint(1,2)
        turtle.pu()
        turtle.setposition(x,y)
        turtle.pd()
        if a == 1:
            drawAllrectangles(x, y, width, height, rotation, offset, count)
        elif a == 2:
            drawcircle(x,y, offset, count,radius)
