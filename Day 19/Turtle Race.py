from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500,height=400)

colors = ["violet","indigo","blue","green","yellow","orange","red"]
bet_choice = screen.textinput(title="Place your bet.",prompt="Which turtle will win the race?Enter a color: ")


turtles = []
dist = 0
is_race_on = False
for i in range(len(colors)) :
    temp_turtle = Turtle(shape="turtle")
    temp_turtle.penup()
    temp_turtle.color(colors[i])
    turtles.append(temp_turtle)
    turtles[i].goto(x=-230,y=-100+dist)
    dist += 30


if bet_choice :
    is_race_on = True

while is_race_on :
    for ttl in turtles :
        if ttl.xcor() > 230:
            is_race_on = False
            winner_color = ttl.pencolor()
            if winner_color == bet_choice :
                print(f"You have won! The {winner_color} is the winning color.")
            else:
                print(f"You have lost! The {winner_color} is the winning color.")

        move = random.randint(0,10)
        ttl.forward(move)











screen.exitonclick()