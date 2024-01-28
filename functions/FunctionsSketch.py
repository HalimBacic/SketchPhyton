from const import constants

def forward(turtle):
    turtle.forward(constants.step)

def back(turtle):
    turtle.backward(constants.step)

def rotateleft(turtle):
    turtle.left(constants.angle)

def rotateright(turtle):
    turtle.right(constants.angle)

def stop(turtle):
    turtle.backward(0)
