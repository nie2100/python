import turtle

t = turtle.Turtle()
t.left(90)
t.penup()
t.backward(500)
t.pendown()
t.pencolor('green')
t.pensize(2)


def tree(brancheLen):
    if brancheLen > 5:
        t.forward(brancheLen)
        t.right(20)
        tree(brancheLen - 15)
        t.left(40)
        tree(brancheLen - 15)
        t.right(20)
        t.backward(brancheLen)


tree(150)
t.hideturtle()
turtle.done()
