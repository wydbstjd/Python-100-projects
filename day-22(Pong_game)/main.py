# 1. Create the screen
# 2. Create and move a paddle
# 3. Create another paddle
# 4. Create the ball and make it move
# 5. Detect collision with wall and bounce
# 6. Detect collision with paddle
# 7. Detect when paddle misses
# 8. Keep score
# 기존 강의에서 키다운 업데이트 및 패들과 공이 겹칠 때 공 떨림 현상 개선

from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

# 키 이벤트 설정
screen.listen()
screen.onkeypress(lambda: r_paddle.key_down("Up"), "Up")
screen.onkeyrelease(lambda: r_paddle.key_up("Up"), "Up")
screen.onkeypress(lambda: r_paddle.key_down("Down"), "Down")
screen.onkeyrelease(lambda: r_paddle.key_up("Down"), "Down")
screen.onkeypress(lambda: l_paddle.key_down("w"), "w")
screen.onkeyrelease(lambda: l_paddle.key_up("w"), "w")
screen.onkeypress(lambda: l_paddle.key_down("s"), "s")
screen.onkeyrelease(lambda: l_paddle.key_up("s"), "s")

def move_paddles():
    if r_paddle.key_state["Up"]:
        r_paddle.go_up()
    if r_paddle.key_state["Down"]:
        r_paddle.go_down()
    if l_paddle.key_state["w"]:
        l_paddle.go_up()
    if l_paddle.key_state["s"]:
        l_paddle.go_down()
    screen.ontimer(move_paddles, 20)  # 20ms마다 반복 실행

# 패들 이동 시작
move_paddles()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # Detect collision the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with paddle
    current_time = time.time()
    if (ball.distance(r_paddle) < 50 and ball.xcor()) > 320 or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        if current_time - ball.last_bounce_time > 0.3:
            ball.bounce_x()

    # Detect paddle misses
    if ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
