import turtle as t
import random

billy = t.Turtle()
billy.speed("fastest")
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    color = (r,g,b)
    return color


def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        billy.color(random_color())
        billy.circle(100)
        billy.setheading(billy.heading() + size_of_gap)

spirograph(1)

screen = t.Screen()
screen.exitonclick()
