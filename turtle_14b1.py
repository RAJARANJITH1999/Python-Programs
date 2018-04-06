import turtle
import time
colors = ["red","green","blue"]
turtle.bgcolor("yellow")
i=0
turtle.pensize(3)
for angle in range(0,360,30):
    turtle.seth(angle)
    i=(i+1) % 3
    turtle.color(colors[i])
    turtle.circle(100)

turtle.exitonclick()
