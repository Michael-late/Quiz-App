from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzlet")
        self.window.config(background=THEME_COLOR,padx=20,pady=20)

        self.score_label = Label(self.window,text=f"Score: 0", background=THEME_COLOR, fg="white")
        self.score_label.grid(row=0,column=1)
        self.canvas = Canvas(self.window, width=300, height=250)
        self.text_box = self.canvas.create_text(150,125,width=280, text="Quiz Questions", font=("arial",20,"italic"))
        self.canvas.grid(row=1,column=0,columnspan=2, pady=20)
        
        correctIMG = PhotoImage(file="images/true.png")
        self.correctBTN = Button(image=correctIMG,command=lambda: self.check_answer("True"))
        self.correctBTN.grid(row=2, column=0)
        
        wrongIMG = PhotoImage(file="images/false.png")
        self.wrongtBTN = Button(image=wrongIMG,command=lambda: self.check_answer("False"))
        self.wrongtBTN.grid(row=2, column=1)
        
        self.get_next_question()
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text_box, text=q_text)
        else:
            self.correctBTN.config(state="disabled")
            self.wrongtBTN.config(state="disabled")

            
    def check_answer(self,answer : str):
        self.get_score = self.quiz.check_answer(answer)
        self.score_label.config(text=f"Score: {self.get_score[0]}")
        self.feedback(self.get_score[1])
        self.window.after(500,self.get_next_question)
        
    
    def feedback(self, a: bool):
        if a:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="red")
        