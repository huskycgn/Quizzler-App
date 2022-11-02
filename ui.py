from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        # Quizquestion
        self.quiz = quiz_brain
        self.question = ''
        self.window = Tk()
        self.window.title('Quizzler')
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.mycan = Canvas(width=300, height=250)
        self.mycan.grid(column=0, row=1, columnspan=2, pady=50, padx=20)
        self.question_text = self.mycan.create_text(
            150,
            125,
            width=280,
            fill=THEME_COLOR,
            text=self.question,
            font=('Arial', 20, 'italic'))
        self.scorelabel = Label(text='Score: 0', bg=THEME_COLOR, padx=20, pady=20, fg='white')
        self.scorelabel.grid(row=0, column=1)
        self.trueimage = PhotoImage(name='truei', file='images/true.png')
        self.falseimage = PhotoImage(name='falsi', file='images/false.png')
        self.truebutton = Button(image='truei',
                                 bg=THEME_COLOR,
                                 highlightthickness=0,
                                 padx=20,
                                 pady=20,
                                 command=self.true_pressed)
        self.truebutton.grid(column=0, row=2)
        self.falsebutton = Button(image='falsi',
                                  bg=THEME_COLOR,
                                  highlightthickness=0,
                                  padx=20,
                                  pady=20,
                                  command=self.false_pressed)
        self.falsebutton.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.mycan.configure(bg='white')
        if self.quiz.still_has_questions():
            self.scorelabel.config(text=f'Score: {self.quiz.score}')
            q_text = self.quiz.next_question()
            self.mycan.itemconfig(self.question_text, text=q_text)
        else:
            self.mycan.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.truebutton.config(state=DISABLED)
            self.falsebutton.config(state=DISABLED)

    def true_pressed(self):
        is_right = self.quiz.check_answer('True')
        self.give_feedback(is_right)

    def false_pressed(self):
        is_right = self.quiz.check_answer('False')
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if not is_right:
            self.mycan.configure(bg='red')
            self.window.after(1000, self.get_next_question)
        else:
            self.mycan.configure(bg='green')
            self.window.after(1000, self.get_next_question)
