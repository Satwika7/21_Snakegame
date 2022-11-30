from turtle import Turtle
ALIGNMNET = "right"
FONT = ('arial', 12, 'normal')

class Score(Turtle):

     def __init__(self):
         super().__init__()
         self.score = 0
         self.color("white")
         self.penup()
         self.hideturtle()
         self.goto(0, 280)
         self.update_score()

     def game_over(self):
         self.goto(0,0)
         self.write("GAME OVER", align=ALIGNMNET, font=FONT)

     def update_score(self):

         self.clear()
         self.write(f"score : {self.score}", align=ALIGNMNET, font=FONT)
         self.score += 1

