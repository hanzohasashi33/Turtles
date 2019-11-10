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
    
'''
If radius is positive, then the arc starts radius turtle steps behind the turtle. 
If radius is negative, then the arc starts radius turtle steps in front of the turtle. 
In both cases, the arc sweeps an angle equal to the angle input.
If angle is positive, then the arc is drawn in a clockwise direction. 
If angle is negative, then the arc is drawn in a counter-clockwise direction. 
If angle is 360 or greater (or -360 or less), then ARC draws a circle.
'''

turtle.exitonclick()
