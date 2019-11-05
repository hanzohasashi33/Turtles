import turtle

n = input('Enter the side of the polygon you want to draw :')
l = input('Enter the length of the side of polygon you want :')
window = turtle.Screen()
window.bgcolor("gold")
window.title("POLYGON DRAWING")

polygon = turtle.Turtle()

externalangle = 360/n

for i in range(n):
    polygon.forward(l)
    polygon.right(externalangle)

turtle.done()
