from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#cd858a"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
check_mark = "✔"
reps = 0
time_to_start= None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global reps
    window.after_cancel(time_to_start)
    check_label.config(text="")
    canvas.itemconfig(timer_content,text="00:00")
    timer.config(text="Timer")
    reps = 0
    start_button.config(state="normal")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    start_button.config(state="disabled")
    work_time = WORK_MIN * 60
    short_break_time = SHORT_BREAK_MIN * 60
    long_break_time =  LONG_BREAK_MIN * 60
    
    if reps % 8 == 0 :
        timer.config(text="Break",fg=RED)
        count_down(long_break_time)

    elif reps % 2 == 0 :
        timer.config(text="Break",fg=PINK)
        count_down(short_break_time)

    else :
        timer.config(text="Timer",fg=GREEN)
        count_down(work_time)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10 :
        count_sec = "0" + str(count_sec)
    if count_min < 10 :
        count_min = "0" + str(count_min)

    canvas.itemconfig(timer_content, text=f"{count_min}:{count_sec}")
    if count > 0 :  
        global time_to_start
        time_to_start = window.after(1000,count_down,count - 1)
    else :
        start_timer()
        mark = ""
        for i in range(reps//2) :
            mark += check_mark
        check_label.config(text=mark)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)
#Canvas
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=tomato_img )
timer_content = canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))
canvas.grid(row=1,column=1)
#Label/Button
timer =  Label(text="Timer",font=(FONT_NAME,45))
timer.config(bg=YELLOW,fg=GREEN)
timer.grid(row=0,column=1)

start_button = Button(text="Start",highlightthickness=0,command=start_timer)
start_button.grid(row=2,column=0)

check_label = Label(fg=GREEN,bg=YELLOW,font=(FONT_NAME,12,"bold"))
check_label.grid(row=3,column=1)

reset_button = Button(text="Reset",highlightthickness=0,command=reset_timer)
reset_button.grid(row=2,column=2)
window.mainloop()