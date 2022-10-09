from pygame import*
from random import*

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, x, y, size_x, size_y, speed):
        super().__init__()
 
        self.image = transform.scale(image.load(player_image), (55, 55))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.sizex = size_x
        self.sizey = size_y
        self.speed = speed


    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_LEFT] and self.rect.x > 5:
            self.rect.x -= self.speed
        if keys[K_RIGHT] and self.rect.x < win_width - 80:
            self.rect.x += self.speed
    def shoot(self):
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top , 1, 2, 5)
        bullets.add(bullet)

class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > win_height:
            self.rect.y = 0
            self.rect.x = randint(0,800)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

win_width = 800
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Shooter")
background = transform.scale(image.load("galaxy.jpg"), (win_width, win_height))

rocket = Player('rocket.png', 5, win_height - 80, 10, 10,4)
score = 0

mixer.init()
mixer.music.load('space.ogg')
mixer.music.play()

fire = mixer.Sound('fire.ogg')

enemies = sprite.Group()
bullets = sprite.Group()
for i in range(10):
    ufo = Enemy('ufo.png', randint(0, win_width), -5, 80, 100, randint(1, 5))
    enemies.add(ufo)

font.init()
font1 = font.Font(None, 40)

finish = False
run = True
score = 0

while run:
    window.blit(background, (0, 0))
    text = font1.render("Score:" + str(score), True, (255, 255, 255))
    window.blit(text, (10, 20))
    for e in event.get():
        if e.type == QUIT:
            run = False
        if e.type == KEYDOWN:
            if e.key == K_SPACE:
                rocket.shoot()
                fire.play()
    collides = sprite.groupcollide(bullets, enemies, False, True)
    if sprite.spritecollide(rocket, enemies, True):
        run = False
    for c in collides:
        ufo = Enemy('ufo.png', randint(0, win_width), -5, 80, 100, randint(1, 5))
        enemies.add(ufo)
        score += 1
    if finish != True:
        window.blit(background,(0, 0))
        rocket.draw()
        enemies.draw(window)
        bullets.draw(window)

        rocket.update()
        enemies.update()
        bullets.update()
        if score >= 10 :
            finish = True
    display.update()