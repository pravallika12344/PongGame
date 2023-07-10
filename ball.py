from turtle import Turtle
class Ball(Turtle):
     
     #initialising turtle object for ball

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.xmove=10
        self.ymove=10
        self.move_speed=0.1
    
    #moving ball continuosly increasing x and y cor


    def move(self):
        x_cor=self.xcor()+self.xmove
        y_cor=self.ycor()+self.ymove
        self.goto(x_cor,y_cor)

    #bouncing back when ball hits the wall

    def bounce_y(self):
        self.ymove*=-1

    # bouncing and increasing speed of ball when it hits paddle

    def bounce_x(self):
        self.xmove*=-1
        self.move_speed*=0.9

    # if the paddle missed the ball


    def resetposition(self):
        self.goto(0,0)
        self.bounce_x()

    
