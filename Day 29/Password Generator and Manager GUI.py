from tkinter import *
from tkinter import messagebox
from random import shuffle,randint,choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list = []
    password_list.extend([choice(letters) for i in range(randint(8, 10))])
    password_list.extend([choice(symbols) for i in range(randint(2, 4))])
    password_list.extend([choice(numbers) for i in range(randint(2, 4))])
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get().strip()
    email = email_entry.get().strip()
    password = password_entry.get().strip()
    if len(website) == 0 or len(password)== 0 :
        messagebox.showwarning(title="Warning",message=f"You have left some details empty. \nPlease fill all the details.")
    else:
        is_ok = messagebox.askokcancel(title=website,message=f"These are the Details entered: \nEmail:{email} \nPassword:{password} \nDo you want to Save?")
        if is_ok :
            with open("data.txt",mode="a") as file:
                file.write(f"{website} || {email}|| {password} \n")
                website_entry.delete(0,END)
                password_entry.delete(0,END)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager GUI App")
window.config(padx=50,pady=50)

#Canvas
canvas = Canvas(width=200,height=200)
pic =  PhotoImage(file="logo.png")
canvas.create_image(100,100,image=pic)
canvas.grid(row=0,column=1)

# Labels
website_label =  Label(text="Website:")
website_label.grid(row=1,column=0,sticky="e")

email_label = Label(text="Email/Username:")
email_label.grid(row=2,column=0,sticky="e")

password_label = Label(text="Password:")
password_label.grid(row=3,column=0,sticky="e")

#Entry
website_entry = Entry()
website_entry.focus()
website_entry.grid(row=1,column=1,columnspan=2,sticky="ew")

email_entry = Entry()
email_entry.insert(0,"@gmail.com")
email_entry.grid(row=2,column=1,columnspan=2,sticky="ew")

password_entry = Entry(width=33)
password_entry.grid(row=3,column=1,sticky="w")

#Buttons
pass_button = Button(text="Generate Password",command=generate_password)
pass_button.grid(row=3,column=2,sticky="e")

add_button = Button(text="Add",command=save)
add_button.grid(row=4,column=1,columnspan=2,sticky="ew")
window.mainloop()

