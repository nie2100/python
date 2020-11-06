import turtle

turtle.setup(650, 350, 200, 200)
turtle.pu()
turtle.fd(-250)
turtle.pd()
turtle.pensize(5)
turtle.pencolor('green')
turtle.seth(-40)
for i in range(4):
    turtle.circle(40, 80)
    turtle.circle(-40, 80)
turtle.circle(40, 80 / 2)
turtle.fd(40)
turtle.circle(16, 180)
turtle.fd(40 * 2 / 3)
turtle.done()
