from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-280,260)
        self.write(arg=f"Level: {self.level}",align="left",font=FONT)

    def update_level(self):
        self.level += 1
        self.clear()
        self.write(arg=f"Level: {self.level}",align="left",font=FONT)

    def gameover(self):
        self.home()
        self.write(arg="Game Over", align="center", font=FONT)
