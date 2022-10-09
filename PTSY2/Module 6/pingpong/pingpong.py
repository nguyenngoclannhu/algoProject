from pygame import*

class GameSprite(sprite.Sprite): #class GameSprite ke thua Sprite co san trong pygame
    def __init__(self, player_image, player_x, player_y, play_speed):#nhan vat, toa do x, y, speed
        super().__init__()#chinh
        self.image = transform.scale(image.load(player_image), (xx, yy))#tao hinh anh nhan vat, kick co
        self.speed = play_speed
        self.rect = self.image.get_rect() #luu toa do vao bien rect
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed_x = play_speed
        self.speed_y = play_speed

    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))#ve nhan vat len man hinh
        draw.rect(window, (0,0,0), self.rect)
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()

        if keys[K_UP] and self.rect.y > 5:
            self.rect.y -= self.speed
 
        if keys[K_DOWN] and self.rect.y < win_height - 80:
            self.rect.y += self.speed
   
class Computer(GameSprite):

    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 5:
            self.rect.y -= self.speed
    
        if keys[K_s] and self.rect.y < win_height - 80:
            self.rect.y += self.speed            

class Ball(GameSprite): #inheritance gamesprite
    def update(self):
        global player_score
        self.rect.y += self.speed_y
        self.rect.x += self.speed_x
        
        if self.rect.y < 0 or self.rect.y > win_height - self.rect.height:
            self.speed_y *=-1 
            

        if self.rect.x < 0 or self.rect.x > win_width - self.rect.width:
            self.speed_x *=-1 
        #if self.rect == player.rect:
        #    player_score +=1 
    

#Size
win_width = 1000
win_height = 700

#Window
window = display.set_mode((win_width, win_height))#dat kick co
display.set_caption("Ping Pong")#ten game
background = transform.scale(image.load("back.jpg"), (win_width, win_height))#set background

#Sprites
xx = 120
yy = 120
player = Player("paddle.png", 5, win_height - 300, 20)#tao nhan vat, x, y, toc do
com = Computer("paddle2.png", 850, win_height - 300, 20)
xx = 50
yy = 50

#ball1 = play.new_circle(color="light blue", x=-350, y=120, radius=25)
ball = Ball("ball.png", 500, win_height - 250, 3)
clock = time.Clock()

#Font
font.init()
font1 = font.Font(None, 50) 


#Run

player_score = 0
score_txt = font1.render(f"Score: {player_score}", True, (87, 17, 17))

com_score = 0
cscore_txt = font1.render(f"Score: {com_score}", True, (87, 17, 17))
run = True

ball_mask = mask.from_surface(ball.image)
player_mask = mask.from_surface(player.image)
com_mask = mask.from_surface(com.image)

while run:
    for e in event.get():
        if e.type == QUIT:
            run = False

    if run:
        window.blit(background, (0,0)) #set background
        ball.draw()
        ball.update()

        player.draw()
        player.update()

        com.draw()
        com.update()

        # score_txt = font.render(f"A Score: {player_score}", True, (87, 17, 17))
        window.blit(score_txt, (150, 5))

        # cscore_txt = font.render(f"B Score: {com_score}", True, (87, 17, 17))
        window.blit(cscore_txt, (600, 5))

        
        if sprite.collide_rect(ball, player):
            if ball_mask.overlap(player_mask,(1,1)):
                ball.rect.x = max(0, ball.rect.x - ball_mask.overlap(player_mask, (1,1))[0])
                ball.rect.y = ball.rect.y - ball_mask.overlap(player_mask, (1,1))[1] 
            ball.speed_x *=-1
            player_score += 1 
            #print(player_score)
        
        if sprite.collide_rect(ball, com):
            if ball_mask.overlap(com_mask,(1,1)):
                ball.rect.x = min(ball.rect.x + ball_mask.overlap(com_mask, (1,1))[0], win_width - 50)
                ball.rect.y = ball.rect.y - ball_mask.overlap(com_mask,(1,1))[1]
            ball.speed_x *=-1
            com_score += 1
            #com_score = com_score +1 - com_score
            

        
        

        clock.tick(200)

    display.update()