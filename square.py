import turtle

window = turtle.Screen()           #create a window 
window.bgcolor("light green")      #bg colour of window is light green
window.title("Turtle")             #tutle of window will be Turtle
skk = turtle.Turtle()              #create a turtle pointer


for i in range(4):                  
    skk.forward(100)               #goes forward by 100 steps
    skk.right(90)                  #turns right by 90 degrees


turtle.done()                      #end of turtle file

