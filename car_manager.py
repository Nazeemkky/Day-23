import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.AllCar = []
        self.carSpeed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_create = random.randint(1, 6)
        if random_create == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=3)
            new_car.color(random.choice(COLORS))
            y_cor = random.randint(-250, 250)
            new_car.goto(x=300, y=y_cor)
            self.AllCar.append(new_car)

    def move(self):
        for car in self.AllCar:
            car.backward(self.carSpeed)

    def level_up(self):
        self.carSpeed += MOVE_INCREMENT
