import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")
screen.onkey(player.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.car_move()

    # check if turtle hit a car
    for car in car_manager.car_list:
        if player.distance(car.pos()) <= 25:
            game_is_on = False
            score.game_over()

    # check if turtle hit the finish line
    if player.finish_line():
        player.start_pos()
        score.increment_level()
        car_manager.increase_speed()


screen.exitonclick()