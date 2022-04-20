from turtle import Turtle

#define constants
ALIGNMENT = "center"
FONT = ('Arial', 8, 'normal')

# create Scoreboard class from Turtle Superclass
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:      # function to read last score from data.txt file record and load it as high score on console
            self.high_score = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

# function to update the scoreboard
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

# function to write current score to data.txt file
    def reset_score(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

# function to keep increase score
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
