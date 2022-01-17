import turtle

sq_size = 75

turtle.speed(20)
turtle.pensize(3)

def square(): 
    for i in range(4):
        turtle.forward(sq_size)
        turtle.right(90)

for i in range(100):
    square()
    turtle.right(20)



turtle.done()