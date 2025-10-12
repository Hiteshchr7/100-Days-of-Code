from tkinter import *
from tkinter import messagebox
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
data_dict = {}
try:
    data = pandas.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    org_data = pandas.read_csv("data/french_words.csv")
    data_dict = org_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")

card = {}
flip_timer = None

# ---------------------------- Functions for buttons ------------------------------- #
def card_flip():
    canvas.itemconfig(card_lang, text="English", fill="white")
    canvas.itemconfig(card_word, text=f"{card['English']}", fill="white")
    canvas.itemconfig(canvas_image, image=card_back_img)

def card_change():
    global card, flip_timer
    if flip_timer:
        window.after_cancel(flip_timer)
    if not data_dict:
        messagebox.showinfo("Congratulations!", "You've learned all the words!")
        window.quit()
        return
    card = random.choice(data_dict)
    canvas.itemconfig(card_lang, text="French", fill="black")
    canvas.itemconfig(card_word, text=f"{card['French']}", fill="black")
    canvas.itemconfig(canvas_image, image=card_front_img)
    flip_timer = window.after(3000, card_flip)

def known_card():
    data_dict.remove(card)
    file = pandas.DataFrame(data_dict)
    file.to_csv("data/words_to_learn.csv", index=False)
    card_change()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, card_flip)

# Canvas
canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="./images/card_front.png")
card_back_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_front_img)
card_lang = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Buttons
right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=known_card)
right_button.grid(row=1, column=1)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=card_change)
wrong_button.grid(row=1, column=0)

card_change()
window.mainloop()
