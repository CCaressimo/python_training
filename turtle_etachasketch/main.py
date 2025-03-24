from turtle import Turtle, Screen

billy = Turtle()
screen = Screen()

def move_forward():
    billy.forward(10)

def move_backward():
    billy.backward(10)
    
def turn_clockwise():
    billy.right(10)

def turn_counterclockwise():
    billy.left(10)

def clear():
    billy.reset()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counterclockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
