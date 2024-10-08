import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600, startx=2000)
screen.tracer(0)

player = Player()
cars = CarManager()

screen.listen()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    cars.move()
    player.check_if_finished()
    for car in cars.list():
        if car.distance(player) < 20:
            game_is_on = False
    screen.update()


screen.exitonclick()
