#import module
from pygame import *
from random import *


class GameSprite(sprite.Sprite):
	def __init__(self, imgFile, x, y, width, height, speed):
		super().__init__()
		self.image = transform.scale(image.load(imgFile),(width,height))
		
		self.rect = self.image.get_rect()
		self.rect.x = x
		self.rect.y = y
		
		self.speed = speed
		
		self.width = width
		self.height = height
	
	def draw(self):
		window.blit(self.image,(self.rect.x,self.rect.y))
	
class Player(GameSprite):
	def update(self):
		keys = key.get_pressed()
		
		if keys[K_LEFT] and self.rect.x > self.width:
			self.rect.x -= self.speed
		if keys[K_RIGHT] and self.rect.x < win_width - self.width:
			self.rect.x += self.speed
		if keys[K_UP] and self.rect.y > self.height:
			self.rect.y -= self.speed
		if keys[K_DOWN] and self.rect.y < win_height - self.height:
			self.rect.y += self.speed
	
	def fire(self):
		#create a bullet
		bullet = Bullet("bullet.png",self.rect.centerx, self.rect.top, 15, 20, 5)
		#add the bullet to a group
		bullets.add(bullet)

class Enemy(GameSprite):
	def update(self):
		self.rect.y += self.speed
		global miss #TODO 
		if self.rect.y > win_height:
			self.rect.y = randint(-5,0)
			self.rect.x = randint(0,win_width)
			miss += 1
miss = 0 #TODO global variable 

#create a Bullet class inheritance GameSprite
class Bullet(GameSprite):
	def update(self):
		self.rect.y -= self.speed
		if self.rect.y < 0:
			self.kill()

#create window
win_height = 800
win_width = 1000
window = display.set_mode((win_width, win_height))
#display background images
background = transform.scale(image.load("galaxy.jpg"),(win_width, win_height))

player = Player("rocket.png",100,100,50,50,5)

enemies = sprite.Group()
bullets = sprite.Group()
for i in range(10): #create 10 enemies 
	enemy = Enemy("ufo.png",randint(0,win_width),randint(-5,0),80,100,randint(1,10))
	enemies.add(enemy) ## add enemy to group

score = 0
font.init()
font1 = font.Font(None, 40) #font size = 40
lose = font1.render("YOU LOSE!", True, (255,255,255))
win = font1.render("YOU WIN!!!", True, (255,255,255))
score_txt = font1.render(f"Score: {score}", True, (255,255,255))
#TODO enemy missed
miss_txt = font1.render(f"Missed: {miss}", True, (255,255,255))

run = True # programming running?
finish = False # losing the game?

#TODO add background music
mixer.init()
mixer.music.load("space.ogg")
mixer.music.play()
mixer.music.set_volume(0.1)
#TODO add sound effect
fire_sound = mixer.Sound("fire.ogg")


#create game loop
while run:
	#add in QUIT event
	for e in event.get():
		if e.type == QUIT:
			run = False
		if e.type == KEYDOWN:
			if e.key == K_SPACE:
				if not finish:
					player.fire()
					fire_sound.play()
				else:
					finish = False
	if not finish:
		window.blit(background, (0,0))

		score_txt = font1.render(f"Score: {score}", True, (255,255,255))
		window.blit(score_txt, (10,20))

		miss_txt = font1.render(f"Missed: {miss}", True, (255,255,255))
		window.blit(miss_txt, (10,50))
	
		player.update()
		player.draw()
	
		enemies.draw(window)
		enemies.update()
		
		bullets.draw(window)
		bullets.update()

		collides = sprite.groupcollide(bullets, enemies, True, True)
		for c in collides:
			#create an enemy
			enemy = Enemy("ufo.png",randint(0,win_width),randint(-5,0),80,100,randint(1,10))
			enemies.add(enemy) ## add enemy to group		
			#increase score
			score += 1


	
		if sprite.spritecollide(player, enemies, True):
			finish = True
			window.blit(lose, (100,100))

		# TODO wininig condition 
		if (score >= 10):
			finish = True 
			# TODO display winning text on the screen
			window.blit(win,(win_width/2,win_height/2))


			
	display.update()
	
	
	
	
	
	