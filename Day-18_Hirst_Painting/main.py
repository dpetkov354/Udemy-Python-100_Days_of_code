import colorgram
import turtle
from turtle import Screen
import random

# GET COLORS
colors = colorgram.extract('image.jpg', 30)

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    main_color = (r, g, b)
    rgb_colors.append(main_color)
print(rgb_colors)

turtle.colormode(255)
rgb_colors = [(202, 164, 110), (149, 75, 50), (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20),
              (134, 163, 184), (197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), (14, 98, 70),
              (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77), (183, 205, 171), (36, 60, 74),
              (19, 86, 89), (82, 148, 129), (147, 17, 19), (27, 68, 102), (12, 70, 64), (107, 127, 153),
              (176, 192, 208), (168, 99, 102)]
turtle.shape("turtle")
turtle.color("chartreuse4")
turtle.speed(0)
turtle.hideturtle()


def create_row():
    for _ in range(10):
        color = random.choice(rgb_colors)
        turtle.dot(10, color)
        turtle.penup()
        turtle.forward(20)
        turtle.pendown()


def move_without_painting():
    turtle.penup()
    turtle.forward(20)
    turtle.pendown()


def right_end_turn():
    turtle.left(180)
    move_without_painting()
    turtle.left(270)
    move_without_painting()
    turtle.left(90)


def left_end_turn():
    turtle.right(180)
    move_without_painting()
    turtle.right(270)
    move_without_painting()
    turtle.right(90)


for row in range(5):
    create_row()
    right_end_turn()
    create_row()
    left_end_turn()

screen = Screen()
screen.exitonclick()
