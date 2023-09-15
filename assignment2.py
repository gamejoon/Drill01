import turtle

def move_turtle(theta):
    turtle.setheading(theta)
    turtle.forward(50)
    turtle.stamp()

turtle.shape("turtle")

turtle.onkey(move_turtle(90), "w")
turtle.onkey(move_turtle(270), "s")
turtle.onkey(move_turtle(0), "d")
turtle.onkey(move_turtle(180), "a")
turtle.listen()

turtle.exitonclick()