from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
tim.color("green")
tim.shape("turtle")


def move_forwards():
    tim.forward(10)


def move_back():
    tim.backward(10)


def move_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def move_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.home()


screen.listen()
tim.setheading(90)
screen.onkey(key="a", fun=move_left)
screen.onkey(key="d", fun=move_right)
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
