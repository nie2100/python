import turtle

t = turtle.Turtle()

points = {'left': (-400, -200),
          'top': (0, 400),
          'right': (400, -200)}


def drawTriangle(points, color):
    t.fillcolor(color)
    t.penup()
    t.goto(points['top'])
    # t.pendown()
    t.begin_fill()
    t.goto(points['left'])
    t.goto(points['right'])
    t.goto(points['top'])
    t.end_fill()


def getMid(p1, p2):
    return ((p1[0] + p2[0]) / 2, (p1[1] + p2[1]) / 2)


def sierpinsi(degree, points):
    colormap = ['blue', 'red', 'green', 'white', 'yellow', 'orange','pink','orange']
    drawTriangle(points, colormap[degree])
    if degree > 0:
        sierpinsi(
            degree - 1,
            {
                'left': points['left'],
                'top': getMid(points['left'], points['top']),
                'right': getMid(points['left'], points['right']),
            }
        )
        sierpinsi(
            degree - 1,
            {
                'left': getMid(points['left'], points['top']),
                'top': points['top'],
                'right': getMid(points['top'], points['right']),
            }
        )

        sierpinsi(degree - 1,
                  {
                      'left': getMid(points['left'], points['right']),
                      'top': getMid(points['top'], points['right']),
                      'right': points['right'],
                  })


sierpinsi(7, points)
