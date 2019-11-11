import turtle
import math

turtle.bgcolor("black")

heart = turtle.Turtle()
heart.speed(0)
def curve():
    heart.speed(0)
    for i in range(200):
        heart.right(1)
        heart.forward(1)

heart.color("red","pink")

heart.begin_fill()
heart.left(140)
heart.forward(111.65)
curve()
heart.left(120)
curve()
heart.forward(111.65)
heart.end_fill()
heart.hideturtle()



turtle.done()
