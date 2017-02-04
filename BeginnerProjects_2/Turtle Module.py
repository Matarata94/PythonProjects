import turtle
import time

a = turtle.Turtle()
turtle.tracer(0,0)
turtle.setup(500,500,None,None)
a.pendown()
angle = 179
for i in range(1,89):
    for j in range(1,38):
        a.forward(150)
        a.left(angle)
    angle -= 1


turtle.update()
turtle.done()
