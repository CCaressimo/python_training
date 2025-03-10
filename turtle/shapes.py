import turtle as t
import random

billy = t.Turtle()
t.colormode(255)
billy.shape("turtle")


def create_circle():
    """Draw a circle"""
    for _ in range(0, 360):
        billy.pendown()
        billy.forward(10)
        billy.right(1)

def create_square():
    """Draw a square"""
    billy.color("#10a4c2")
    for _ in range(0,4):
        billy.pendown()
        billy.forward(100)
        billy.right(90)

def dashed_lines():
    """Draw dashed lines"""
    for _ in range(0,50):
        billy.pendown()
        billy.forward(5)
        billy.right(1)
        billy.penup()
        billy.forward(5)
        billy.right(1)

def draw_shapes(num_sides):
    billy.speed(0)
    angle = 360 / num_sides
    for _ in range(num_sides):
        billy.forward(25)
        billy.right(angle)

for shape_side_n in range(3,361):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    billy.color(r,g,b)
    draw_shapes(shape_side_n)

# dashed_lines()
# create_circle()
# create_square()

screen = t.Screen()
screen.exitonclick()