#Squarespiral2.py
import turtle
t=turtle.Pen()
t.speed(0)
t.pensize(10)
t.width(3)


colors=["red","yellow","blue","green"]
for x in range(100):
    t.pencolor(colors[x%4])
    t.forward(x*2) 
    t.left(91)

turtle.clearscreen()