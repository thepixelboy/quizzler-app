from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#cee5d0"
FONT = ("Arial", 20, "italic")
GREEN = "#1eae98"
DARK_GREEN = "#2f5d62"
RED = "#f29191"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", fg=DARK_GREEN, bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question = self.canvas.create_text(150, 125, width=280, text="Question", font=FONT, fill=DARK_GREEN)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.button_true_image = PhotoImage(file="./images/true.png")
        self.button_true = Button(image=self.button_true_image, highlightthickness=0, command=self.true_pressed)
        self.button_true.grid(row=2, column=0)

        self.button_false_image = PhotoImage(file="./images/false.png")
        self.button_false = Button(image=self.button_false_image, highlightthickness=0, command=self.false_pressed)
        self.button_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")

        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz")
            self.button_true.config(state="disabled")
            self.button_false.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg=GREEN)
        else:
            self.canvas.config(bg=RED)

        self.window.after(1000, self.get_next_question)
