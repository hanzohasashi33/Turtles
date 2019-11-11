import turtle


window = turtle.Screen()
turtle.speed(2)
colors = ['red','purple','blue','green','orange','yellow']
rainben = turtle.Pen()
turtle.bgcolor('black')

for i in range(360):
    rainben.pencolor(colors[i%6])
    rainben.width(i/100 + 1)
    rainben.forward(i)
    rainben.left(59)

