from turtle import Turtle
class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.turtlesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.setpos(position)

        # 키 상태 추적을 위한 딕셔너리
        self.key_state = {
            "Up": False,
            "Down": False,
            "w": False,
            "s": False
        }

    def key_down(self, key):
        self.key_state[key] = True

    def key_up(self, key):
        self.key_state[key] = False
    def go_up(self):
        if self.ycor() < 250:
            x = self.xcor()
            new_y = self.ycor() + 20
            self.goto(x, new_y)

    def go_down(self):
        if self.ycor() > -240:
            x = self.xcor()
            new_y = self.ycor() - 20
            self.goto(x, new_y)