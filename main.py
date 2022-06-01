import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)


tim = Player()
screen.listen()
screen.onkey(key="Up", fun=tim.up)
screen.onkey(key="Down", fun=tim.down)
car = CarManager()
score = Scoreboard()


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move()

    for one_car in car.AllCar:
        if one_car.distance(tim) < 20:
            score.end()
            game_is_on = False

    if tim.is_that_finished():
        tim.start_from()
        car.level_up()
        score.increase()

screen.exitonclick()
