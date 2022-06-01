from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()

        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.shape("turtle")

    def up(self):
        self.forward(MOVE_DISTANCE)

    def down(self):
        y_cor = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), y_cor)

    def start_from(self):
        self.goto(STARTING_POSITION)

    def is_that_finished(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
