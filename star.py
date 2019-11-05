import turtle

star = turtle.Turtle()     #create a turtle pointer named star

for i in range(5):
    star.forward(50)       #go forward by 50 steps
    star.right(144)        
#turn right by 144 degrees , the base is differently assumed in turtle,just try 36 and see the output.


turtle.done()
