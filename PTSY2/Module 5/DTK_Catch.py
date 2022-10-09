from pygame import *

window = display.set_mode((700,500))
display.set_caption("Catch")

background = image.load("background.png")
background = transform.scale(background, (700,500))
window.blit(background,(0,0))

player1 = image.load("sprite1.png")
player1 = transform.scale(player1, (50,50))
window.blit(player1, (50,50))

player2 = image.load("sprite2.png")
player2 = transform.scale(player2, (50,50))
window.blit(player2, (150,150))

x1, y1 = 50, 350
x2, y2 = 490, 350

#game loop
game = True
while game:
	
	for e in event.get():
		if e.type == QUIT:
			game = False
	
	key_pressed = key.get_pressed()
	
	if key_pressed[K_LEFT] and x1 > 5:
		x1 -= 10
	

	window.blit(background,(0,0))
	window.blit(player1, (x1, y1))
	window.blit(player2, (x2, y2))
	display.update()
	
	
	
	
	
	
	