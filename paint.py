"""Paint, for drawing shapes.
Author: Humberto Alejandro Rosas Téllez
Author2: Mariana Edith Ramírez Navarrete
"""
import turtle

from turtle import *

from freegames import vector


def line(start, end):
    """Draw line from start to end."""
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)


def square(start, end):
    """Draw square from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circle(start, end):
    """Draw circle from start to end."""
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    """Se dibuja el círculo en 30 pasos cada uno con un ángulo de 12°"""
    for count in range(30):
        forward(end.x - start.x)
        left(12)

    end_fill()


def rectangle(start, end):
    t = turtle.Turtle()
 
    l = int(input("Enter the length of the Rectangle: "))
    w = int(input("Enter the width of the Rectangle: "))
 
    t.forward(l) 
    t.left(90) 
 
    t.forward(w) 
    t.left(90) 
 
    t.forward(l) 
    t.left(90) 
    
    t.forward(w) 
    t.left(90)    


def triangle(start, end):
    f = int(input("Enter the value of the side: "))

    turtle.left(60)

    turtle.forward(f)

    turtle.left(240)
    
    turtle.forward(f)

    turtle.left(240)  
    
    turtle.forward(f)
    #n = 10
    #pen = turtle.Turtle()  
    #for i in range(n * 3):  
    #    pen.forward(i * 10)  
    #    pen.right(120) 
    #turtle.done() 


def tap(x, y):
    """Store starting point or draw shape."""
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None


def store(key, value):
    """Store value in state at key."""
    state[key] = value


state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
"""ADD A COLOR: YELLOW"""
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circle), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()
