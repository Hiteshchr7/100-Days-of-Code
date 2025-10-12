from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)  # makes the x and y of shape half or halves dimension of height and width
        self.color("red")
        self.speed("fastest")
        self.change()

    def change(self) :
        x_cor = random.randint(-280,280)
        y_cor = random.randint(-280,280)
        self.goto(x_cor,y_cor)
      
