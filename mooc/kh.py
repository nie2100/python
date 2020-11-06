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
    turtle.setup(1400, 800)
    turtle.penup()
    turtle.goto(-600, -100)
    turtle.pendown()
    turtle.pensize(1)
    turtle.pencolor('red')
    koch(1200, 5)

    turtle.done()


main()
