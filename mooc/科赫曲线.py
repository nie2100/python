import turtle


def koch(size, n):
    if n == 0:
        turtle.fd(size)
    else:
        for angle in [0, 60, -120, 60]:
            turtle.left(angle)
            koch(size / 3, n - 1)


def main():
    turtle.hideturtle()
    turtle.setup(1000, 1000)
    turtle.penup()
    turtle.goto(-400,150)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor('red')
    level = 4
    koch(600, level)
    turtle.right(90)
    koch(600, level)
    turtle.right(90)
    koch(600, level)
    turtle.right(90)
    koch(600, level)
    turtle.done()


main()
