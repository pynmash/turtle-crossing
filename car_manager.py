from turtle import Turtle
from random import choice, randrange


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_cars()
        self.move_distance = STARTING_MOVE_DISTANCE

    def create_cars(self):
        for _ in range(25):
            new_car = Turtle()
            new_car.penup()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=randrange(2, 4))
            new_car.color(choice(COLORS))
            new_car.goto(x=randrange(-300, 300, 20), y=randrange(-240, 260, 20))
            self.cars.append(new_car)

    def list(self):
        return self.cars

    def move(self):
        for car in self.cars:
            car.goto(car.xcor() - self.move_distance, car.ycor())
            if car.xcor() < -340:
                car.goto(340, car.ycor())
