import turtle

window = turtle.Screen()
turtle.speed(2)
window.bgcolor("black")
circle_pattern = turtle.Turtle()
circle_pattern.color("white")

for i in range(30):
    circle_pattern.circle(5 * i)
    circle_pattern.circle(-5 * i)
    circle_pattern.left(i)

turtle.exitonclick()
