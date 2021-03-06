from pygame import*
#parent class for other sprites
class GameSprite():
  #class constructor
  def __init__(self, player_image, player_x, player_y, player_speed):
 
      # each sprite should store the image property
      self.image = transform.scale(image.load(player_image), (80, 80))
      self.speed = player_speed
 
      # each sprite should store the rect (rectangle) property in which it is entered
      self.rect = self.image.get_rect()
      self.rect.x = player_x
      self.rect.y = player_y
   #method drawing the character on the window
  def reset(self):
      window.blit(self.image, (self.rect.x, self.rect.y))
#main player class
class Player(GameSprite):
  #method that implements sprite control using the keyboard arrow buttons
  def update(self):
      keys = key.get_pressed()
      if keys[K_LEFT] and self.rect.x > 5:
          self.rect.x -= self.speed
      if keys[K_RIGHT] and self.rect.x < win_width - 80:
          self.rect.x += self.speed
      if keys[K_UP] and self.rect.y > 5:
          self.rect.y -= self.speed
      if keys[K_DOWN] and self.rect.y < win_height - 80:
          self.rect.y += self.speed
#enemy sprite class    
class Enemy(GameSprite):
  side = "left"
   #enemy movement
  def update(self):
      if self.rect.x <= 410:
          self.side = "right"
      if self.rect.x >= win_width - 85:
          self.side = "left"
      if self.side == "left":
          self.rect.x -= self.speed
      else:
          self.rect.x += self.speed
#wall element class
class Wall():
  def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_width, wall_height):
       self.color_1 = color_1
       self.color_2 = color_2
       self.color_3 = color_3
       self.width = wall_width
       self.height = wall_height
 
       # picture of the wall - a rectangle of the desired size and color
       self.image = Surface([self.width, self.height])
       self.image.fill((color_1, color_2, color_3))
 
       # each sprite should store the rect (rectangle) property
       self.rect = self.image.get_rect()
       self.rect = Rect(wall_x, wall_y, wall_width, wall_height)
  def draw_wall(self):
      draw.rect(window, (self.color_1, self.color_2, self.color_3), (self.rect.x, self.rect.y, self.width, self.height))
#Create a window
win_width = 700
win_height = 500
display.set_caption("Labyrinth")
window = display.set_mode((win_width, win_height))
#create walls
w1 = Wall(0, 0, 0, win_width / 2 - win_width / 3, win_height / 2, 300, 10)
w2 = Wall(0, 0, 0, 410, win_height / 2 - win_height / 4, 10, 350)
#create sprites
packman = Player('hero.png', 5, win_height - 80, 5)
monster = Enemy('cyborg.png', win_width - 80, 200, 5)
final_sprite = GameSprite('pac-1.png', win_width - 85, win_height - 100, 0)
 
#game loop
run = True
while run:
   #the loop runs every 0.05 seconds
   time.delay(50)
 
   #sort through all the events that could happen
   for e in event.get():
       #event of clicking the ???close??? button
       if e.type == QUIT:
           run = False
 
   #update the background with every iteration
   window.fill((255, 255, 255))
 
   #draw the walls
   w1.draw_wall()
   w2.draw_wall()
 
   #run the sprite movement
   packman.update()
   monster.update()
 
   #update them in a new location with each iteration of the loop
   packman.reset()
   monster.reset()
   final_sprite.reset()
 
   display.update()
 
 
 
 

