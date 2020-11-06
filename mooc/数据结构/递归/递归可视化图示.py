import turtle

t = turtle.Turtle()

points = {'left': (-200, -100),
          'top': (0, 200),
          'right': (200, -100)}

def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()

drawTriangle(points,'red')


turtle.done()
