# import colorgram as cg

# colors = cg.extract('hirst.jpeg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

import turtle as t
import random

color_list = [(195, 8, 69), (231, 54, 132), (194, 164, 15), (112, 178, 214), (199, 77, 15), (216, 162, 101), (34, 187, 112), (29, 104, 167), (14, 23, 64), (20, 29, 168), (212, 136, 175), (231, 224, 7), (197, 34, 130), (15, 181, 210), (231, 167, 197), (126, 189, 163), (10, 48, 29), (40, 131, 75), (141, 217, 203), (61, 22, 10), (60, 13, 27), (108, 91, 210), (235, 64, 34), (131, 217, 230), (183, 17, 9)]
billy = t.Turtle()
screen = t.Screen()
screen.setup(width=1000, height=1000)
t.colormode(255)
billy.speed("fastest")
billy.penup()
billy.setheading(225)
billy.forward(300)
billy.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    billy.dot(20, random.choice(color_list))
    billy.forward(50)

    if dot_count % 10 == 0:
        billy.setheading(90)
        billy.forward(50)
        billy.setheading(180)
        billy.forward(500)
        billy.setheading(0)

screen.exitonclick()
