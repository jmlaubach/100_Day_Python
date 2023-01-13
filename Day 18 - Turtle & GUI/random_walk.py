from turtle import *
import random

timmy = Turtle()
timmy.speed(8)
timmy.width(3)

colors = ["red", "SeaGreen3", "yellow2", "SkyBlue1", "tan1"]
directions = [90, 180, 270, 360]

def random_walk(c, d):
    while True:
        timmy.color(random.choice(c))
        timmy.right(random.choice(d))
        timmy.forward(10)


random_walk(colors, directions)

screen = Screen()
screen.exitonclick()