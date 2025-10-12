from turtle import Turtle

def draw_center_line():
    center_line = Turtle()
    center_line.color("white")
    center_line.hideturtle()
    center_line.penup()
    center_line.goto(0, 300)
    center_line.setheading(-90)

    for _ in range(30):
        center_line.pendown()
        center_line.forward(10)
        center_line.penup()
        center_line.forward(10)
