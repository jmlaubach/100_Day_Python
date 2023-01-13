from turtle import *
from random import randint

timmy = Turtle()
timmy.speed(8)
timmy.width(3)

colors = ["red", "SeaGreen3", "yellow2", "SkyBlue1", "tan1"]
directions = [90, 180, 270, 360]

def random_walk(c, d):
    while True:
        timmy.color(c[randint(0, 4)])
        timmy.right(d[randint(0, 3)])
        timmy.forward(10)


random_walk(colors, directions)

screen = Screen()
screen.exitonclick()