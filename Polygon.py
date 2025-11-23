import turtle
turtle.Screen().bgcolor("red")
a = turtle.Turtle()
turtle.Screen().setup(500,500)
sides = int(input("Enter the number of sides you want: "))
for i in range(sides):
    a.forward(50)
    a.left(360/sides)
turtle.done()
