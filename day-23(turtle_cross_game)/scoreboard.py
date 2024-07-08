from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 1
        self.goto(-280, 250)
        self.update()

    def increase_level(self):
        self.level += 1
        self.update()

    def update(self):
        self.clear()
        self.write(f'Level: {self.level}', align="left", font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", font=FONT, align='center')

