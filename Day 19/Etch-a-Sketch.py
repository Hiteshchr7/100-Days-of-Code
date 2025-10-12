from turtle import Turtle,Screen
ted = Turtle()
screen = Screen()

def forw():
    ted.forward(10)

def back():
    ted.backward(10)

def clock_turn():
    ted.right(10)

def anti_clock_turn():
  ted.left(10)

def screen_clear():
    ted.speed(0)
    ted.home()
    ted.clear()
    
screen.listen()
screen.onkeypress(fun=forw,key ="w")
screen.onkeypress(fun=back,key ="s")
screen.onkeypress(fun=clock_turn,key ="d")
screen.onkeypress(fun=anti_clock_turn,key ="a")
screen.onkey(fun=screen_clear,key="c")
screen.exitonclick()