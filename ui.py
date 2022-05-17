from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterFace:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        self.score = Label(text="Score: 0", fg="White", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.score.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="",
            fill=THEME_COLOR,
            font=("Arial", 20, "italic"
                  )
        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_photo = PhotoImage(file="images/true.png")
        self.right_button = Button(image=right_photo, highlightthickness=0, command=self.right)
        self.right_button.grid(column=0, row=2)

        false_photo = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_photo, highlightthickness=0, command=self.wrong)
        self.false_button.grid(column=1, row=2)

        self.get_next_questions()

        self.window.mainloop()

    def get_next_questions(self):
        self.canvas.config(bg="white")
        self.score.config(text=f"Score: {self.quiz.score}")
        try:
            q_text = self.quiz.next_question()
        except IndexError:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.right_button.config(state="disabled")
            self.false_button.config(state="disabled")
        else:
            self.canvas.itemconfig(self.question_text, text=q_text)

    def right(self):
        is_right = self.quiz.check_answer("True")
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_questions)

    def wrong(self):
        is_false = self.quiz.check_answer("False")
        if is_false:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_questions)
