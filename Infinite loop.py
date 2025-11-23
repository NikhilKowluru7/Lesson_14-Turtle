import turtle
turtle.Screen().bgcolor("red")
a = turtle.Turtle()
size = 0
turtle.Screen().setup(500,500)
while True:
    for i in range(4):
        size=size+5
        a.forward(size)
        a.left(90)

turtle.done()