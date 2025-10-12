from turtle import Turtle,Screen,colormode
import random
colormode(255)
the_ninja_turtle = Turtle()
the_ninja_turtle.shape("turtle")
colours = ["medium blue","cyan","aquamarine","green yellow","yellow","crimson","medium slate blue","magenta"]

#function that generats any random color for turtle
def random_color():
    r =random.randint(0,255)
    g =random.randint(0,255)
    b =random.randint(0,255)
    return (r,g,b)
 
# 1. Draw a Dashed line 
for _ in range(25):
    the_ninja_turtle.fd(10)
    the_ninja_turtle.penup()
    the_ninja_turtle.fd(10)
    the_ninja_turtle.pendown() 

# 2. Draw all shapes from a triangle to a decagon
def draw_shapes(sides):
    the_ninja_turtle.color(random.choice(colours))
    angle = 360/sides
    for sides in range(sides):
        the_ninja_turtle.fd(100)
        the_ninja_turtle.right(angle)

for side in range(3,10+1):
    draw_shapes(side)

# 3. Random Walking turtle
the_ninja_turtle.pensize(15)
the_ninja_turtle.speed("fastest")
directions = [0,90,180,270]
for _ in range(200):
    the_ninja_turtle.color(random_color())
    the_ninja_turtle.fd(30)
    the_ninja_turtle.setheading(random.choice(directions))
   

# 4. Making a Spirograph
the_ninja_turtle.pensize(1)
the_ninja_turtle.speed("fastest")
def draw_spirograph(shift):
    for _ in range(int(360/shift)):
        the_ninja_turtle.color(random_color())
        the_ninja_turtle.circle(100)
        the_ninja_turtle.left(shift)
draw_spirograph(5)



screen = Screen()
screen.exitonclick()