from turtle import window_width
from pygame import *
import random

#game sprite base class
class GameSprite(sprite.Sprite):
    def __init__(self, x, y, width, height, filename, speed):
        super().__init__()
        self.image = transform.scale(image.load(filename), (width, height))
    
        self.rect = self.image.get_rect()
        self.rect.x = x 
        self.rect.y = y 

        self.speed_x = speed
        self.speed_y = speed 
    
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player():
    def __init__(self, x, y, width, height, speed, color):
        self.rect = Rect(x, y, width, height)
        self.rect.x = x 
        self.rect.y = y 

        self.speed = speed
        self.color = color

        self.point = 0
    
    def draw(self):
        draw.rect(window,self.color,self.rect, border_radius=15)

class Player1(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys[K_DOWN] and self.rect.y < scr_height - self.rect.height:
            self.rect.y += self.speed

class Player2(Player):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed 
        if keys[K_s] and self.rect.y < scr_height - self.rect.height:
            self.rect.y += self.speed 
    
class Ball(GameSprite):
    def update(self):
        global finished
        self.rect.x += self.speed_x # <=> self.rect.x = self.rect.x + self.speed_x
        self.rect.y += self.speed_y

        if self.rect.x < 0 or self.rect.x > scr_width - self.rect.width:
            finished = True 
        
        if self.rect.y < 0 or self.rect.y > scr_height - self.rect.height:
            self.speed_y *= -1

    def checkHit(self):
        if self.rect.x < 0:
            return 1 #player 1 wins
        elif self.rect.x > scr_width - self.rect.width:
            return -1 #player 2 wins
        return 0

class Label():
    def __init__(self, x, y, width, height, color):
        self.rect = Rect(x, y, width, height)
        self.clr = color 
    
    def setText(self, text, fontsize, txtClr):
        self.image = font.Font(None, fontsize).render(text, True, txtClr)
    
    def draw(self):
        draw.rect(window, self.clr, self.rect)
        window.blit(self.image, (self.rect.x, self.rect.y))

class Computer(Player):
    def update(self, ball):
        if ball.rect.y > self.rect.y:
            temp = self.speed
        elif ball.rect.y <= self.rect.y:
            temp = (-1)*self.speed
        
        if ball.rect.x > scr_width / 2:
            temp = 0
        
        self.rect.y += temp 
        
        
#load background
scr_width = 700
scr_height = 500 

window = display.set_mode((scr_width, scr_height))
background = transform.scale(image.load("cave.png"),(scr_width,scr_height))
ball = Ball(350,250,70,70,"rock.png",5)
ball1 = Ball(350,250,70,70,"rock.png",random.randint(1,5))

# player2 = Player2(10, 200, 20, 100, 5, (174, 214, 241))
player2 = Computer(10, 200, 20, 100, 5, (174, 214, 241))
player1 = Player1(scr_width - 50, 200, 20, 100, 5, (241, 148, 138))

font.init()
font1 = font.Font(None, 40)
player1_scr = 0
p1_score = Label(300,20,100,50,(0,0,0))
p1_score.setText(f"Player 1: {player1_scr}", 40, (255,255,255))

player2_scr = 0
p2_score = Label(150,20, 100,50, (0,0,0))
p2_score.setText(f"Player 2: {player2_scr}", 40, (255,255,255))


clock = time.Clock()
run = True
finished = False
count, turn = 0, 0 
while run:
    window.fill((23,67,1))
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                finished, turn, winner = False, 0, 0
                ball.speed_x, ball.speed_y = random.choice([-5,5]), random.choice([-5,5])
                ball1.speed_x, ball1.speed_y = (-1)*ball.speed_x, (-1)*ball.speed_y
                
    if not finished:
        window.blit(background, (0,0))

        if turn > 5:
            ball1.draw()
            ball1.update()
            player2.update(ball1)

        p1_score.draw()
        p2_score.draw()
        
        ball.draw()
        ball.update()

        player1.draw()
        player1.update()

        player2.draw()
        player2.update(ball)

        if sprite.collide_rect(ball, player1) and not player1.rect.contains(ball.rect):
            ball.speed_x *= -1
            turn += 1
        if sprite.collide_rect(ball, player2) and not player2.rect.contains(ball.rect):
            ball.speed_x *= -1
            turn += 1
        
        if sprite.collide_rect(ball1, player1) and not player1.rect.contains(ball1.rect):
            ball1.speed_x *= -1
            turn += 1
        if sprite.collide_rect(ball1, player2) and not player2.rect.contains(ball1.rect):
            ball1.speed_x *= -1
            turn += 1
        
    else:
        winner = ball.checkHit()
        if turn > 5:
            winner += ball1.checkHit()
        window.blit(background, (0,0))
        count += 1
        if winner > 0:
            player1_scr += 1
            p1_score.setText(f"Player 1: {player1_scr}", 40, (255,255,255))
        elif winner < 0:
            player2_scr += 1
            p2_score.setText(f"Player 2: {player2_scr}", 40, (255,255,255))

        p2_score.draw()
        p1_score.draw()

        player1.draw()
        player2.draw()

        ball.speed_x, ball.speed_y = 0, 0
        ball.rect.y, ball.rect.x = scr_height / 2 - 20, scr_width / 2

        ball.draw()
        if turn > 5:
            ball1.speed_x, ball1.speed_y = 0, 0
            ball1.rect.y, ball1.rect.x = scr_height / 2 + 20, scr_width / 2

            ball1.draw()
        
        # p1_score = font1.render(f"Player 1: {player1_scr}", True, (0,0,0))
        # p2_score = font1.render(f"Player 2: {player2_scr}", True, (0,0,0))

        # window.blit(p2_score, (300,20))
        # window.blit(p1_score, (150,20))
    

    clock.tick(40)
    display.update()