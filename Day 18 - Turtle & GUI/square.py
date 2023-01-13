from turtle import *

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange red")

for x in range(4):
    timmy.forward(100)
    timmy.left(90)

screen = Screen()
screen.exitonclick()

