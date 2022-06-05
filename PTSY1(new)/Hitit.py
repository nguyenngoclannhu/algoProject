 from turtle import *
from random import randint
class Sprite(Turtle):
    def __init__(self, x, y, speed, shape='circle', color='black'):
        super().__init__()
        self.speed(10)
        self.penup()
        self.goto(x,y)
        self.color(color)
        self.shape(shape)
        self.step = speed

    def move_up(self):
        self.setheading(90)
        self.goto(self.xcor(), self.ycor() + self.step)

    def move_down(self):
        self.setheading(-90)
        self.goto(self.xcor(), self.ycor() - self.step)
    
    def move_left(self):
        self.setheading(180)
        self.goto(self.xcor() - self.step, self.ycor())
    
    def move_right(self):
        self.setheading(0)
        self.goto(self.xcor() + self.step, self.ycor())
    
    def is_collide(self, sprite):
        dist = self.distance(sprite.xcor(),sprite.ycor())
        if dist < 30:
            return True
        else:
            return False
    
    def set_move(self, x_start, y_start, x_end, y_end):
        self.x_start = x_start
        self.y_start = y_start 
        self.x_end = x_end 
        self.y_end = y_end
        self.goto(x_start,y_start)
        self.setheading(self.towards(x_end,y_end))
    
    def make_steps(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.set_move(self.x_end, self.y_end, self.x_start, self.y_start)
    

player = Sprite(0, -150, 10, shape = 'circle', color = 'orange')
scr = player.getscreen()
scr.listen()

scr.onkey(player.move_up, "Up")
scr.onkey(player.move_down, "Down")
scr.onkey(player.move_left, "Left")
scr.onkey(player.move_right, "Right")

monsters = []
for i in range(10):
    y = randint(-90,150)
    monster = Sprite(0, y , 5, shape = 'square', color = 'red')
    monster.set_move(randint(-100,0),y, randint(0,100),y)
    monsters.append(monster)

goal = Sprite(0, 200, 10, shape = 'triangle', color = 'green')

total_score = 0
while total_score < 2:
    for monster in monsters: 
        monster.make_steps()
    if player.is_collide(goal):
        player.goto(0,-150)
        total_score += 1
    
    for monster in monsters:
        if player.is_collide(monster):
            player.goto(0,-150)
            total_score -= 1

    if total_score < 0:
        goal.hideturtle()
        break

for monster in monsters:
    monster.hideturtle()
player.hideturtle()

pen = Turtle()x
pen.hideturtle()
pen.penup()
pen.goto(-50,0)
if total_score == -1:
    pen.color("red")
    pen.write("Game over!", font = ("Cambria",20,"bold"))
elif total_score == 2:
    pen.color("darkgreen")
    pen.write("You win!", font = ("Cambria", 40, "italic"))

exitonclick()