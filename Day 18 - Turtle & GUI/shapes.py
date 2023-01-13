from turtle import *
from random import randint

timmy = Turtle()
timmy.shape("turtle")


def draw_shape(sides, angle):
    for x in range(sides):
        timmy.right(angle)
        timmy.forward(100)


shapes = [
    {"shape": "triangle", "sides": 3, "angle": 120},
    {"shape": "square", "sides": 4, "angle": 90},
    {"shape": "pentagon", "sides": 5, "angle": 72},
    {"shape": "hexagon", "sides": 6, "angle": 60},
    {"shape": "heptagon", "sides": 7, "angle": 51.42857142857143},
    {"shape": "octagon", "sides": 8, "angle": 45},
    {"shape": "nonagon", "sides": 9, "angle": 40},
    {"shape": "decagon", "sides": 10, "angle": 36}
]

for s in shapes:
    shape_side = s["sides"]
    side_angle = s["angle"]
    draw_shape(shape_side, side_angle)

screen = Screen()
screen.exitonclick()

