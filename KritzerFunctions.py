import turtle
bob = turtle.Turtle()

def pentagon(distance):
    for times in range(5):
        bob.forward(distance)
        bob.right(72)

def polygon(distance,sides):
    angle = 360/sides
    bob.color(color)
    bob.begin_fill()
    for times in range(sides):
        bob.forward(distance)
        bob.right(angle)
    bob.end_fill()

def jump(x,y):
    bob.penup()
    bob.goto(x,y)
    bob.pendown()


def star(distance):
    for times in range(5):
        bob.forward(distance)
        bob.right(144)
        
def explosion(distance,color):
    bob.color(c)
    for times in range(8):
        bob.forward(distance)
        bob.right(135)

def circle(distance):
    bob.circle(100)
    bob.color("red")

def portal():
    for times in range(60):
        c = (times*4,times*4,times*4)
        polygon(3,125-times*2,c) of times
        bob.right(92)
    
    
    
