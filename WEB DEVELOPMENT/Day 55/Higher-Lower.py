from flask import Flask
import random
app = Flask(__name__)

num = random.randint(0,9)
@app.route("/")
def home():
    return '<h1><b>Guess a number between 0 and 9</b></h1>' \
    '<img src="https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif">'

@app.route("/<int:n>")
def func(n):
    if n<num :
        return '<h1 style="color: red"><b>Too Low, Try Again!</b></h1>' \
        '<img src="https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif">'
    elif n>num:
        return '<h1 style="color: purple"><b>Too High, Try Again!</b></h1>' \
        '<img src="https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif">'
    else :
        return '<h1 style="color: green"><b>You Found me!</b></h1>' \
        '<img src="https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif">'
if __name__ == "__main__" :
    app.run(debug=True)