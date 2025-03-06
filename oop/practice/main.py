# import turtle
from prettytable import PrettyTable
# billy = turtle.Turtle()

# print(billy)
# billy.shape("turtle")
# billy.color("#1d149c")
# billy.forward(100)

# my_screen = turtle.Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick

table = PrettyTable()

table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmandor"])
table.add_column( "Type", ["Electric", "Water", "Fire"])
table.align = "l"

print(table)
