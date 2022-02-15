"""A Double Moon- Big-Dipper Combo."""

__author__ = 730477174


from turtle import Turtle, colormode, done
colormode(255)
samantha: Turtle = Turtle()  # My girl samantha is in charge of drawing my black cavnas and night sky with the help of my sqaure_drawer function, thank you, samantha :)!
samantha.color("green")
joe: Turtle = Turtle()  # joe is in charge of none other than the moons within my picture with the help of my circle_drawer fucntion, without him, the beauty of my picture would surely falter, thank you, joe!!
joe.color("pink")  # He is pink because pink is my favorite color
so_many_turtles: Turtle = Turtle()  # so_many_turtles is my favorite turtle because he is in charge of drawing my big dipper with the help of the triangle_star_placer! He has a lot of hard work drawing all those stars which is hard to do beacuse I was unable to create a while loop for the big dipper, making it extremely tedious, not only to read for coders, but also for poor so_many_turtles :(. Thank you so many turtles for all your hard work and dedication!
so_many_turtles.color("white")
probably_the_last_turtle: Turtle = Turtle()  # probably_the_last_turtle is in charge of drawing my land/ grass that the viewer is standing upon while looking at the big dipper and double moon, probably_the_last_turtle also makes use of the rectangle_drawer function to do this. probably_the_last_turtle is also my least favorite turtle >:(.


def main() -> None:
    """The start of my beautiful picture of the sky."""
    samantha.hideturtle()
    samantha.speed(50)
    samantha.fillcolor("black")
    samantha.begin_fill()
    square_drawer(samantha, -370, 335, 800)  # This is where samantha draws the big black square.
    samantha.end_fill()
    probably_the_last_turtle.hideturtle()
    probably_the_last_turtle.speed(50)
    probably_the_last_turtle.fillcolor("green")
    probably_the_last_turtle.begin_fill()
    rectangle_drawer(probably_the_last_turtle, -360, 0, 550, 800)  # This is where probably_the_last_turtle draws my grass.
    probably_the_last_turtle.end_fill()
    joe.hideturtle()
    joe.speed(50)
    joe.fillcolor(176, 172, 84)
    joe.begin_fill()
    circle_drawer(joe, -250, 335, 100)  # Here is where joe draws my moon on the left side.
    joe.end_fill()
    joe.begin_fill()
    circle_drawer(joe, 440, 325, 100)  # This is joe drawing it on the right side :).
    joe.end_fill()
    so_many_turtles.speed(50)
    so_many_turtles.hideturtle()
    so_many_turtles.fillcolor("white")  # The beginning of so_many_turtles' tireless job of making the wonderful big dipper for us. Say, "Thank you so_many_turtles!!!"
    so_many_turtles.begin_fill()
    triangle_star_placer(so_many_turtles, -50, 200, 10)  # I wanted to make this entire next section of code prettier by using a while loop, but since these numbers don't follow a pattern, I was unable to do so, hence the ugliness of the code :(.
    triangle_star_placer(so_many_turtles, -200, 250, 10)
    triangle_star_placer(so_many_turtles, -125, 225, 10)
    triangle_star_placer(so_many_turtles, 75, 150, 10)
    triangle_star_placer(so_many_turtles, 50, 175, 10)
    triangle_star_placer(so_many_turtles, 30, 175, 10)
    triangle_star_placer(so_many_turtles, 5, 175, 10)
    triangle_star_placer(so_many_turtles, 75, 175, 10)
    triangle_star_placer(so_many_turtles, -25, 180, 10)
    triangle_star_placer(so_many_turtles, -19, 150, 10)
    triangle_star_placer(so_many_turtles, -10, 130, 10)
    triangle_star_placer(so_many_turtles, 5, 130, 10)
    triangle_star_placer(so_many_turtles, 25, 130, 10)
    triangle_star_placer(so_many_turtles, 50, 130, 10)
    triangle_star_placer(so_many_turtles, 68, 130, 10)
    so_many_turtles.end_fill()
    done()
    return


def square_drawer(turtle_name: Turtle, x: float, y: float, w: float) -> None:
    """Draws the big black square that I will use as the backdrop to the starry sky and moons."""
    turtle_name.penup()
    turtle_name.goto(x, y) 
    turtle_name.setheading(0.0)
    turtle_name.pendown()
    i: int = 0
    while i < 4:  # A while loop is used here in order to draw the square given the proper perameters.
        turtle_name.forward(w)
        turtle_name.right(90)
        i = i + 1
    return


def circle_drawer(turtle_name: Turtle, x: float, y: float, w: float) -> None:
    """Used to draw the two moons within my picture."""
    turtle_name.penup()
    turtle_name.goto(x, y)
    turtle_name.setheading(90.0)
    turtle_name.pendown()
    turtle_name.circle(w)  # We did not learn the circle command but I researched and found the circle just uses w as its radius so it knows how big to make the circle!
    

def rectangle_drawer(turtle_name: Turtle, x: float, y: float, w: float, z: float) -> None:
    """Used to draw the grass/land within my picture."""
    turtle_name.penup
    turtle_name.goto(x, y)
    turtle_name.setheading(0.0)
    turtle_name.pendown()
    i: int = 0
    while i < 2:  # Here i used a while loop that counts up so all sides of the rectangle are drawn. I only count to 2 because both the width and the length are made within one loop, so it only requires 2 loops to complete. z is the length, w is the width.
        if z > w:
            turtle_name.forward(z)
            turtle_name.right(90)
        turtle_name.forward(w)
        turtle_name.right(90)
        i = i + 1


def triangle_star_placer(turtle_name: Turtle, x: int, y: int, w: float) -> None:
    """Used to draw the stars within my picture, however the stars aren't actual stars and they are triangles but at least they look pretty :)."""
    i: int = 0
    turtle_name.penup()
    turtle_name.goto(x, y)
    turtle_name.color(255, 255, 255)
    turtle_name.pendown()
    turtle_name.begin_fill()
    while (i < 3):  # This just creates a normal triangle like in the turtle tutorial, but with the added addition of choosing the size of the triangle, which in this case was 10 for all of them.
        turtle_name.forward(w)
        turtle_name.left(120)
        i = i + 1
    turtle_name.end_fill()


if __name__ == "__main__":
    main()