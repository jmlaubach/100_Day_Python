from turtle import *

timmy = Turtle()
timmy.shape("turtle")
timmy.color("orange red")

for x in range(15):
    timmy.forward(10)
    timmy.penup()
    timmy.forward(10)
    timmy.pendown()

screen = Screen()
screen.exitonclick()