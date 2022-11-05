from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.sety(280)
        self.color("white")
        self.write("Score: {}".format(self.score), False, 'center', font=('Arial', 8, 'normal'))

    def increase_score(self):
        self.score += 1
        self.undo()
        self.write("Score: {}".format(self.score), False, 'center', font=('Arial', 8, 'normal'))