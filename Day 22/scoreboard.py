from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.create_scorecard()

    


    def create_scorecard(self):
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update()

    def update(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))

    def l_point(self):
        self.l_score += 1
        self.update()
    
    def r_point(self):
        self.r_score += 1
        self.update()
    
    def gameover(self):
        self.goto(0,0)
        self.write(arg="Game Over", align="center", font=("Arial",24,"normal"))
        self.goto(0,-40)
        if self.l_score == 10 :
            self.write(arg="Left Side has Won", align="center", font=("Arial",18,"normal"))
        elif self.r_score == 10 :
            self.write(arg="Right Side has Won", align="center", font=("Arial",18,"normal"))


