from turtle import Turtle, Screen

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.goto(-280,270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level : {self.level}", align="left", font=("Courier", 16, "bold"))

    def increase_level(self):
        self.level +=1
        self.update_scoreboard()


    def game_over(self):
        self.clear()
        self.goto(-75,0)
        self.write("GAME OVER", font=("Courier", 24, "bold"))
        self.goto(-50,-40)
        self.write(f"Level : {self.level}", align="left", font=("Courier", 16, "bold"))
