from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from Center_dashline import draw_center_line
import time

screen = Screen()
ball = Ball()
score = Scoreboard()

screen.bgcolor("black")
screen.setup(800, 600)
screen.title("PONG: Classic Arcade Game")
screen.tracer(0)
draw_center_line()

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Checking Collision with the Wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()

    # Checking Collision with Right Paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0:
        ball.bounce_paddle()

    # Checking Collision with Left Paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -320 and ball.x_move < 0:
        ball.bounce_paddle()

    # Checking for balls missed by right paddle
    if ball.xcor() > 380:
        score.l_point()
        ball.respawn()

    # Checking for balls missed by left paddle
    if ball.xcor() < -380:
        score.r_point()
        ball.respawn()
    
    # Game over condition
    if score.l_score == 10 or score.r_score == 10 :
        game_is_on = False
        score.gameover()

screen.exitonclick()
