from turtle import *
import random

timmy = Turtle()
colormode(255)
timmy.speed(0)
timmy.width(2)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


def spirograph():
    spin = 0
    while spin <= 360:
        timmy.color(random_color())
        timmy.circle(100)
        timmy.right(5)
        spin += 5

        
spirograph()

screen = Screen()
screen.exitonclick()