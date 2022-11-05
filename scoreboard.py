from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.sety(250)
        self.color("white")
        self.write("Score: {}".format(self.score), False, 'center', font=('Arial', 24, 'normal'))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write("Score: {}".format(self.score), False, 'center', font=('Arial', 24, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Arial', 24, 'normal'))
