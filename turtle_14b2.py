import turtle as t
t.color("green")
t.pensize(3)
for j in range(0,361,10):
    t.seth(j)
    for i in range(4):
        t.forward(100)
        t.left(90)
t.exitonclick()    

