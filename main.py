import random
from turtle import Screen, Turtle
import time
from player import Player
from car_manager import CarManager
from score import Score

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
car = CarManager()
score = Score()

screen.listen()
screen.onkey(player.move_up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    for cars in car.all_cars:
        if cars.distance(player) < 22:
            game_is_on = False
            score.game_over()
    if player.is_at_finishline():
        player.go_to_start()
        car.level_up()
        score.increase_level()

screen.exitonclick()
