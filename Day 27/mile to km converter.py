from tkinter import *

#window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20,pady=20)

miles_inp = Entry(width=7)
miles_inp.grid(row=0,column=1)

miles_label = Label(text="Miles")
miles_label.grid(row=0,column=2)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(row=1,column=0)

km_op_label = Label(text="0")
km_op_label.grid(row=1,column=1)

km_label = Label(text="Km")
km_label.grid(row=1,column=2)

def convert():
    output = round(1.609 * float(miles_inp.get()),1)
    km_op_label.config(text=f"{output}")
calculate_button = Button(text="Calculate",command=convert)
calculate_button.grid(row=2,column=1)


window.mainloop()