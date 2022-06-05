from pygame import *
'''Required classes'''
 
#parent class for sprites
class GameSprite(sprite.Sprite):
   #class constructor
   def __init__(self, player_image, player_x, player_y, player_speed):
       super().__init__()
       #every sprite must store the image property
       self.image = transform.scale(image.load(player_image), (65, 65))
       self.speed = player_speed
       #every sprite must have the rect property – the rectangle it is fitted in
       self.rect = self.image.get_rect()
       self.rect.x = player_x
       self.rect.y = player_y
 
   def reset(self):
       window.blit(self.image, (self.rect.x, self.rect.y))
 
#Game scene:
win_width = 700
win_height = 500
window = display.set_mode((win_width, win_height))
display.set_caption("Maze")
background = transform.scale(image.load("background.jpg"), (win_width, win_height))
 
#Game characters:
packman = GameSprite('hero.png', 5, win_height - 80, 4)
monster = GameSprite('cyborg.png', win_width - 80, 280, 2)
final = GameSprite('treasure.png', win_width - 120, win_height - 80, 0)
 
game = True
clock = time.Clock()
FPS = 60
 
#music
mixer.init()
mixer.music.load('jungles.ogg')
mixer.music.play()
 
while game:
   for e in event.get():
       if e.type == QUIT:
           game = False
  
   window.blit(background,(0, 0))
   packman.reset()
   monster.reset()
 
   display.update()
   clock.tick(FPS)
