import turtle as t
import random

turtle = t.Turtle()

t.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


directions = [0, 90, 180, 270]
turtle.pensize(12)
turtle.speed(0)

for move in range(500):
    turtle.color(random_color())
    turtle.forward(25)
    turtle.setheading(random.choice(directions))
