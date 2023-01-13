from turtle import *
import random

timmy = Turtle()
colormode(255)
timmy.speed(8)
timmy.width(3)

colors = ["red", "SeaGreen3", "yellow2", "SkyBlue1", "tan1"]
directions = [90, 180, 270, 360]

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def random_walk(c, d):
    while True:
        timmy.color(random_color())
        timmy.right(random.choice(d))
        timmy.forward(10)


random_walk(colors, directions)

screen = Screen()
screen.exitonclick()