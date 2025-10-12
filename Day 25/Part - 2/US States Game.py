import turtle 
import pandas

screen =  turtle.Screen()
screen.title("US States Game")

img = "blank_states_img.gif"
screen.addshape(img)
turtle.shape(img)



data =  pandas.read_csv("50_states.csv")
states_list = data.state.to_list()
state_text = turtle.Turtle()

#ans_state = screen.textinput(title=f"{guess}/50 States", prompt="What's another state's name?")
guess =  0
guess_list = []
while guess < 50 :
    state_text.hideturtle()        
    state_text.penup()
    ans_state = screen.textinput(title=f"{guess}/50 States Guessed ", prompt="What's another state's name?")
    if ans_state is None or ans_state == "exit" :
        missed_states =[]
        for state in states_list:
            if state not in guess_list:
                missed_states.append(state)
        df = pandas.DataFrame(missed_states)
        df.to_csv("States_to_Remember.csv")
        break
    ans_state = ans_state.title()
    if ans_state in states_list and ans_state not in guess_list:
        guess+=1
        x_cor = data[data.state == ans_state].x.item()
        y_cor = data[data.state == ans_state].y.item()
        
        state_text.goto(x_cor,y_cor)
        state_text.write(ans_state)
        guess_list.append(ans_state)

print(guess_list)
screen.mainloop()