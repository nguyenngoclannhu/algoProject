from pygame import *
import os
import time as t
from random import randint

win_width = 1000
win_height = 800

window = display.set_mode((win_width, win_height))
background = transform.scale(image.load("jungle.png"),(win_width, win_height))
# window.fill((0,0,0))

class GameSprite(sprite.Sprite):
	def __init__(self, img, x, y, width, height, speed):
		super().__init__()
		self.image = transform.scale(image.load(img), (width,height))
		self.rect = self.image.get_rect()
		self.rect.x = x 
		self.rect.y = y
		
		self.width = width
		self.height = height
		
		self.speed = speed
	def draw(self):
		window.blit(self.image, (self.rect.x, self.rect.y))

class Dino(GameSprite):
	def __init__(self, img, x, y, width, height, speed):
		super().__init__(img, x, y, width, height, speed)
		self.jumping = False
		self.falling = False
		self.onground = True
		self.jumpHeight = 200
		self.gravity = 2
	
	def update(self,loop):			
		if self.jumping:
			self.rect.y -= self.jumpHeight
			if self.rect.y <= win_height - 500:
				self.setFalling()
			self.set_texture("jump/",(loop%7))
		elif self.falling:
			self.rect.y += self.gravity * self.speed
			if self.rect.y >= win_height - 300:
				self.stopFalling()
		elif self.onground:
			self.set_texture("",(loop+1) % 7)
	
	def set_texture(self,filepath,num):
		path = os.path.join(filepath,f"dino{num}.png")
		self.image = transform.scale(image.load(path),(self.width,self.height))
		
	def setJumping(self):
		global loop
		loop = 0
		self.jumping = True
		self.onground = False
		
	def setFalling(self):
		self.jumping = False 
		self.falling = True
	
	def stopFalling(self):
		global loop
		loop = 0
		self.onground = True
		self.falling = False 
class Cactus(GameSprite):
	def update(self):
		self.rect.x -= self.speed
		if self.rect.x < 0:
			self.rect.x = randint(500, win_width + 100)
		
clock = time.Clock()

dino = Dino("dino0.png",100,win_height-300,200,200,5)

cactuses = sprite.Group()
for i in range(10):
	cactuses.add(Cactus("cactus.png", 900, win_height - 300, 100, 100, 5))

font.init()
font1 = font.Font(None, 40)
lose = font1.render("YOU LOSE!", True, (0,0,0))
window.blit(background,(0,0))
run = True
finished = False
start = False
loop = 0
while run:
	for e in event.get():
		if e.type == QUIT:
			run = False
		if e.type == KEYDOWN:
			if e.key == K_SPACE:
				if start != True:
					start = True
					cactuses = sprite.Group()
					for i in range(10):
						cactuses.add(Cactus("cactus.png", 900, win_height - 200, 100, 100, 30))
				if dino.onground:
					dino.setJumping()
	
	if start:
		window.blit(background,(0,0))

		dino.update(loop)
		dino.draw()
		
		cactuses.update()
		cactuses.draw(window)
		
		if sprite.spritecollide(dino, cactuses, True):
			window.blit(lose, (win_width / 2, win_height / 2))
			cactuses = sprite.Group()
			for i in range(10):
				cactuses.add(Cactus("cactus.png", 900, win_height - 200, 100, 100, 30))
# 			start = False
			
		
	loop += 1
	
	clock.tick(20)
	display.update()
				
			
			
			
			
			
			
			
			
			