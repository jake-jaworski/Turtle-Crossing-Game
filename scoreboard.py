from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 1
        self.level_update()

    def increment_level(self):
        self.clear()
        self.level += 1
        self.level_update()

    def level_update(self):
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over!", align="center", font=FONT)
