from turtle import Turtle

Alignment ="center"
Font = ("Courier",14,"normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,280)
        self.update_score()
        self.hideturtle()
        
    def update_score(self):
        self.write(arg = f"Score: {self.score} ", move = False, align = Alignment,font=Font)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game Over",align=Alignment,font=Font)