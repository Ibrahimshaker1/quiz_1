import tkinter as tk
import time
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"
class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score_cont = self.quiz.score
        # self.text = self.tex.current_question
        self.window = tk.Tk()
        self.window.config(pady=20, padx=20, width=500, height=500)
        self.window.title("Quizzler")
        self.window.configure(background=THEME_COLOR)
        self.score = tk.Label(text=f"score:{self.score_cont}", bg=THEME_COLOR)
        self.score.grid(column=1, row=0)
        self.canvas = tk.Canvas(width=300, height=250, background="white")
        self.canvas_text = self.canvas.create_text(
            150,
            125,
            width=200,
            text="question",
            font=("Arial", 15, "italic")
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        true_image = tk.PhotoImage(file="true.png")
        self.true_button = tk.Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true_button.grid(column=0, row=2)
        false_image = tk.PhotoImage(file="false.png")
        self.false_button = tk.Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false_button.grid(column=1, row=2)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        text = self.quiz.next_question()
        self.canvas.config(bg="white")
        self.canvas.itemconfig(self.canvas_text, text=text)

    def true_press(self):
        ans = "True"
        check = self.quiz.check_answer(ans)
        if check:
            self.score.config(text=f"score{self.quiz.score}")
            self.canvas.config(bg="green", highlightthickness=0)
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
            self.window.after(1000, self.get_next_question)


    def false_press(self):
        ans = "False"
        check = self.quiz.check_answer(ans)
        if check:
            self.score.config(text=f"score{self.quiz.score}")
            self.canvas.config(bg="green", highlightthickness=0)
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red", highlightthickness=0)
            self.window.after(1000, self.get_next_question)

    # def get_feedback(self, check):
    #    if check:
    #        self.canvas.config(bg="green")
    #        self.window.after(1000, self.get_next_question)
