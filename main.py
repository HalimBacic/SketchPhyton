import turtle
from const import constants
from functions.FunctionsSketch import *

screen = turtle.Screen()
screen.bgcolor("#fc6358")

turtle = turtle.Turtle()
screen.listen()
screen.onkeypress(lambda: forward(turtle), constants.forward)
screen.onkeypress(lambda: back(turtle), constants.backward)
screen.onkeypress(lambda: rotateleft(turtle), constants.rot_left)
screen.onkeypress(lambda: rotateright(turtle), constants.rot_right)
for item in constants.allcommands:
    screen.onkeyrelease(lambda: stop(turtle), item)

screen.mainloop()
