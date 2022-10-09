from pygame import *

#TODO create GameSprite class derived from sprite.Sprite 
class GameSprite(sprite.Sprite):
	def __init__(self, x, y, width, height, speed, filename):
		super().__init__()
		self.images = transform.scale(image.load(filename),(width, height))
		self.rect = self.images.get_rect()
		self.rect.x = x
		self.rect.y = y 

		self.speed = speed 
	
	#TODO defind a draw() method to display the images
	def draw(self):
		window.blit(self.images, (self.rect.x, self.rect.y))

#TODO create Player class derived from GameSprite
class Player(GameSprite):
	def update(self):
		keys = key.get_pressed()
		if keys[K_LEFT]:
			self.rect.x -= self.speed

class Enemy(GameSprite):
	def update(self):
		if self.rect.x <= 470:
			self.side = "right"
		if self.rect.x >= win_width - 85:
			self.side = "left"
		
		if self.side == "left":
			self.rect.x -= self.speed 
		else:
			self.rect.x += self.speed
	
class Wall(sprite.Sprite):
	def __init__(self, x, y, width, height, color):
		super().__init__()
		self.rect = Rect(x, y, width, height)
		self.clr = color 

	def draw(self):
		draw.rect(window, self.clr, self.rect)



win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))

#TODO create treasure from Character class using "treasure.png" file
# x,y, width, height, speed, filename
char1 = GameSprite(100,100,50,50,5,"hero.png")
goal = GameSprite(300,300, 50,50,5,"treasure.png")
enemy = Enemy(100,200,50,50,5,"cyborg.png")
wall1 = Wall(100,100,20,200,(0,0,0))
wall2 = Wall(200,100,20,20,(0,0,0))
wall3 = Wall(300,200,20,50,(0,0,0))

font.init()
font1 = font.Font(None, 40)
lose = font1.render("You lose!", True, (0,0,0))


game = True
finish = False 
while game:
	for e in event.get():
		if e.type == QUIT:
			game = False
	if not finish:
		window.blit(background,(0,0))
		char1.draw()
		char1.update()

		enemy.draw()
		enemy.update()

		wall1.draw()
		wall2.draw()
		wall3.draw()

		if sprite.collide_rect(char1, enemy):
			finish = True
			window.blit(lose, (win_width/2, win_height/2))
		
		if sprite.collide_rect(char1, wall1) or sprite.collide_rect(char1, wall2) or sprite.collide_rect(char1, wall3):
			finish = True
			window.blit(lose, (win_width/2, win_height/2))


	display.update()
	
		
	
	

