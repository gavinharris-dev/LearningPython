import turtle
import random

turtle.colormode(255)
turtle.speed(80)

angle = 5

def straight():
    
    for i in range(0, 100, angle):
        turtle.pencolor( random.randint(0, 254), random.randint(0, 254), random.randint(0, 254) )
        turtle.circle(50)
        turtle.forward(angle)
        turtle.circle(50)


def corner():
    for i in range(int((360 / angle) / 4)):
        turtle.pencolor( random.randint(0, 254), random.randint(0, 254), random.randint(0, 254) )
        turtle.circle(50)
        turtle.right(angle)
        
def square():
    for i in range(4):
        corner()
        straight()
   
square()
 
turtle.done()