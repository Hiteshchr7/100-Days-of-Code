from turtle import Screen
import time
from Snake import Snake
from Food import Food
from Scoreboard import Scoreboard


screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Classic Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()
screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.right,"Right")
screen.onkey(snake.left,"Left")


snake_on_move = True
while snake_on_move :
    time.sleep(0.1)
    screen.update()

    snake.move()
    # Checking for Food Collision
    if snake.head.distance(food) <15:
        food.change()
        snake.extend()
        score.increase_score()
    # Checking for Wall Collision
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        snake_on_move = False
        score.gameover()
    # Checking for Collision with Tail
    for seg in snake.snake[1:]:
        if snake.head.distance(seg)< 10 :
            snake_on_move = False
            score.gameover()


screen.exitonclick()