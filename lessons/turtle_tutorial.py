"""Turtle Tutorial"""

from turtle import Turtle, begin_fill, colormode, done
colormode(255)
leo: Turtle = Turtle()
side_length: float = 600.0

leo.speed(2)
leo.hideturtle()
leo.penup()
leo.goto(-300, -250)
leo.pendown()
leo.color("yellow")
leo.pencolor("pink")
leo.fillcolor(105, 23, 65)
leo.begin_fill()

i: int = 0
while (i < 3):
    leo.forward(side_length)
    leo.left(120)
    i = i + 1
leo.end_fill()


bob: Turtle = Turtle()
bob.color(0, 0, 0,)
bob.pencolor(0, 0, 0)
bob.speed(10)
bob.penup()
bob.goto(-300, -250)
bob.pendown()
i: int = 0
while (i < 3):
    side_length = side_length *
    bob.forward(side_length)
    bob.left(123)
    i += 1
done()