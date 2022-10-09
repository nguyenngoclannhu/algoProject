from pygame import *

class GameSprite(sprite.Sprite):
	def __init__(self, img, x, y, size_x, size_y, speed):
		super().__init__()
		self.image = transform.scale(image.load(img), (size_x, size_y))
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
		if keys[K_LEFT] and self.rect.x > self.sizex:
			self.rect.x -= self.speed
		if keys[K_RIGHT] and self.rect.x <= win_width - self.sizex
			self.rect.x += self.speed

class Enemy(GameSprite):
	def update(self):
		self.rect.y += self.speed
		if self.rect.y > win_height:
			self.rect.y = 0
			self.rect.x = #ngẫu nhiên trong khoảng từ 0 -> win_width

win_width = 800
win_height = 500

window = display.set_mode((win_width, win_height))
window.set_caption("Shooter")

background = transform.scale(image.load("galaxy.png"),(win_width, win_height))

run = True
while run:
	#event handling
	for e in event.get():
		if e.type == QUIT:
			run = False
	
	
	window.blit(background, (0,0))
	display.update()
