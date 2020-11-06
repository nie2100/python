import turtle

t = turtle.Turtle()


def drawSpiral(t, linLen):
    if linLen > 0:
        t.forward(linLen)
        t.right(90)
        drawSpiral(t,linLen-5)

drawSpiral(t,200)

turtle.done()