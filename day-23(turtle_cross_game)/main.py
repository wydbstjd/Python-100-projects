# 1단계: 게임 방법
#     1. 거북이는 ‘위’ 키를 누르면 앞으로 움직입니다. 뒤로 가거나, 왼쪽, 오른쪽으로 움직이지 않고, 앞으로만 움직입니다.
#     2. 자동차는 y축 범위 내에서 무작위로 생성되고, 화면의 오른쪽 가장자리에서 왼쪽 가장자리로 움직입니다.

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
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.go_up, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    # 자동차 생성 및 이동
    car_manager.create_cars()
    car_manager.move_cars()

    # 자동차와 충돌했을 때
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # 결승선 통과했을 때
    if player.is_at_finish_line():
        player.reset_pos()
        car_manager.level_up()
        scoreboard.increase_level()


screen.exitonclick()