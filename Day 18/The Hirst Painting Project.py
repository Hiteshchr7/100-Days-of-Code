"""import colorgram
colors =  colorgram.extract('hirst_painting.jpg', 34)
rgb_color_tuple = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_color_tuple.append((r,g,b))
print(rgb_color_tuple)"""
import random
from turtle import Turtle,Screen,colormode
colormode(255)
color_list =[(196, 166, 105), (133, 167, 194), (46, 103, 147), (147, 89, 40), (9, 21, 54), (189, 156, 33), (225, 208, 112), (62, 22, 9), (68, 120, 77), (58, 12, 23), (185, 140, 166), (136, 181, 149), (136, 28, 12), (131, 76, 105), (14, 42, 26), (18, 53, 137), (121, 26, 41), (170, 101, 137), (92, 152, 97), (175, 189, 217), (86, 121, 184), (183, 99, 86), (22, 93, 65), (67, 153, 170), (210, 177, 204), (89, 77, 14), (167, 209, 177), (12, 89, 106), (161, 204, 212), (220, 179, 172)]

hirst_turtle = Turtle()
hirst_turtle.speed("fastest")
hirst_turtle.hideturtle()
hirst_turtle.setheading(225)
hirst_turtle.penup()
hirst_turtle.fd(300)
hirst_turtle.setheading(0)



def create_a_line(no_of_dots,dist_bw_dots):
    for i in range(no_of_dots):
        hirst_turtle.dot(20,random.choice(color_list))
        hirst_turtle.fd(dist_bw_dots)
    hirst_turtle.left(90)
    hirst_turtle.fd(dist_bw_dots)
    hirst_turtle.right(90)
    hirst_turtle.backward(dist_bw_dots*no_of_dots)

for i in range(10):
    create_a_line(10,50)

screen = Screen()
screen.exitonclick()