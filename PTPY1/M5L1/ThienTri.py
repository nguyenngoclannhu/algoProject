from pygame import *
window = display.set_mode((800,500))
display.set_caption("Pygame")
window.fill((15,194,192))

background = transform.scale(image.load("fantasyforest.png"),(500,500))
img1 = transform.scale(image.load("shutterstock_777735517-[Converted]-2.png"),(50,50))
x = 100
y = 100
run = True
while run:
	time.delay(5000)
	#create a character
	draw.rect(window, (255,255,255), (200,100,60,40))
	window.blit(background, (0,0))
	window.blit(img1, (100,100))
	
	for e in event.get():
		if e.type == QUIT:
			run = False
		
		if e.type == KEY_DOWN:
			if e.key == K_LEFT:
				
	
	
	
	display.update()
	
