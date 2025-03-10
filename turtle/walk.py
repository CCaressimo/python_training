import turtle as t
import random

billy = t.Turtle()
t.colormode(255)
degree = [0, 45, 90, 135, 180, 225, 270, 315]


billy.shape("turtle")
billy.width(8)
billy.speed(0)

def random_walk():
    for _ in range(0,10000):
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
            
        billy.color(r,g,b)
        billy.setheading(random.choice(degree))
        billy.forward(30)


random_walk()


screen = t.Screen()
screen.exitonclick()