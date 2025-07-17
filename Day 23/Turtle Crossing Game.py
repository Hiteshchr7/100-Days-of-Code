import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
score = Scoreboard()
cars = CarManager()


screen.listen()

screen.onkeypress(fun=player.move, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move()
    
    # Checking if player finishes a level 
    if player.ycor() > 280 :
        player.win()
        score.update_level()
        cars.increase_speed()

    # Checking if player collides with a car
    for car in cars.all_cars:
        if player.distance(car) < 20 :
            score.gameover()
            game_is_on = False



screen.exitonclick()
