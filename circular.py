import turtle

radius = 50
turtle.speed(4)

for rings in range(10):
    #turtle.penup()
    turtle.goto(1, +radius)
    turtle.pendown()
    turtle.circle(radius)
    radius += 10
