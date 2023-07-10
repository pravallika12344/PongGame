from turtle import Turtle
class ScoreBoard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.l_score=0
        self.r_score=0
        self.penup()
        self.color("white")
        self.update_scoreboard()
    
    #updating score each time ball goes to touch paddles

    def update_scoreboard(self):
        self.clear()
        self.goto(-100,200)
        self.write(self.l_score,align="center",font=("Courier",80,"normal"))
        self.goto(100,200)
        self.write(self.r_score,align="center",font=("Courier",80,"normal"))
     
     # incrementing lscore

    def l_point(self):
       self.l_score+=1
       self.update_scoreboard()
    
    # incrementing rscore

    def r_point(self):
        self.r_score+=1
        self.update_scoreboard()
