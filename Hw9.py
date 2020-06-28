# 9,18

from turtle import Screen, Turtle

turtle = Turtle()
def blink_on():
    turtle.write("WELCOME", align="center", font=("Impact", 50))
    screen.ontimer(blink_off, 1000)

def blink_off():
    turtle.undo()
    screen.ontimer(blink_on, 1000)

screen = Screen()

blink_on()

screen.exitonclick()

