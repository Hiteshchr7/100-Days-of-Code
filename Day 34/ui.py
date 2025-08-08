from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self,quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR,padx=20,pady=20)
        self.canvas = Canvas(height=250,width=300,background="white")
        self.ques_text = self.canvas.create_text(150,125,width=280,text="text",fill=THEME_COLOR,font=("Arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.score = Label(text="Score: 0",bg=THEME_COLOR,fg="white")
        self.score.grid(row=0,column=1)

        check_img = PhotoImage(file="./images/true.png")
        self.right = Button(image=check_img,highlightthickness=0,command=self.true_choice)
        self.right.grid(row=2,column=0)

        cross_img = PhotoImage(file="images/false.png")
        self.wrong = Button(image=cross_img,highlightthickness=0,command=self.false_choice)
        self.wrong.grid(row=2,column=1)

        self.get_next_ques()
        self.window.mainloop()

    def get_next_ques(self):
        self.canvas.config(background="white")
        if self.quiz.still_has_questions():
            self.score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.ques_text,text=q_text)
        else :
            self.canvas.itemconfig(self.ques_text,text="You have completed the quiz.")
            self.right.config(state="disabled")
            self.wrong.config(state="disabled")

    def true_choice(self):
        self.feedback(self.quiz.check_answer("True"))
    
    def false_choice(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self,is_right):
        if is_right:
            self.canvas.config(bg="green")
        else :
            self.canvas.config(bg="red")
        self.window.after(500,self.get_next_ques)
        

            