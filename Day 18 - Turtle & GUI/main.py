from turtle import *
import colorgram
import random

#rgb_colors = []
#colors = colorgram.extract('painting.jpg', 13)

#def random_color(color_obj):
#    for color in color_obj:
#        r = color.rgb.r
#        g = color.rgb.g
#        b = color.rgb.b
#        new_color = (r, g, b)
#        rgb_colors.append(new_color)

timmy = Turtle()
colormode(255)
timmy.speed(0)
timmy.hideturtle()
color_list = [(240, 242, 245), (223, 236, 228), (236, 230, 216), (140, 176, 207), (25, 32, 48), (26, 107, 159), (237, 225, 235), (209, 161, 111), (144, 29, 63), (230, 212, 93), (4, 163, 197), (218, 60, 84), (229, 79, 43)]

def make_row():
    dot_count = 0
    while dot_count < 18:
        timmy.dot(20, random.choice(color_list))
        timmy.forward(30)
        dot_count += 1


def spot_painting():
    y_cord = -250
    timmy.penup()
    timmy.setposition(-250, y_cord)
    column_count = 0
    while column_count < 18:
        make_row()
        y_cord += 30
        column_count += 1
        timmy.setposition(-250, y_cord)


spot_painting()

screen = Screen()
screen.exitonclick()
