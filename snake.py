from turtle import Turtle

class Snake:
    def __init__(self):
        self.starting_position = [(0, 0), (-20, 0), (-40, 0)]
        self.segments = []

        for position in self.starting_position:
            new_segment = Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def move_snake(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            self.segments[seg_num].goto(self.segments[seg_num - 1].xcor(), self.segments[seg_num - 1].ycor())

        self.segments[0].forward(20)