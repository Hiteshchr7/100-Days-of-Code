from turtle import Turtle
  
move_dist = 20
Up = 90
Down = 270
Right = 0
Left = 180
Start_Position = [(0,0),(-20,0),(-40,0)]

class Snake :

    def __init__(self):
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]
    
    def create_snake(self):
        for position in Start_Position:
          self.add_segment(position) 

    def add_segment(self,position):       
        seg = Turtle(shape="square")    #seg == segment
        seg.color("white")
        seg.penup()
        seg.goto(position)
        self.snake.append(seg)

    def extend(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for seg in range(len(self.snake)-1,0,-1):
            new_x = self.snake[seg-1].xcor()
            new_y = self.snake[seg-1].ycor()
            self.snake[seg].goto(new_x,new_y)
        self.head.forward(move_dist)

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)
    
    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)
    
   
        






