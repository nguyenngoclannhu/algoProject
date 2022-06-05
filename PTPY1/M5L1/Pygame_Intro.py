from pygame import*
window = display.set_mode((700, 500))
display.set_caption("The first project")
# background = transform.scale(image.load("background.png"), (700, 500))
# parameters of the first sprite (square)
height = 60
width = 40
x = 5
y = 500 - height - 5
speed = 5
#parameters of the picture sprite
x2 = 100
y2 = 395
#character's image
img1 = transform.scale(image.load('1-2.png'), (100, 100))
#game loop
run = True
while run:
  #the loop is executed each 0.05 sec
  time.delay(50)
  #in each iteration, paint the screen in the initial color and redraw the object in a new place
  #window.fill((0,0,0)) #black background
  window.blit(background,(0, 0))
   #search through all events that might occur
  for e in event.get():
      #window's "x" button press event
      if e.type == QUIT:
          run = False
   #----------------------------------------------------------------------------
   #managing and updating the square sprite picture
   #a simple management method - does not work if a key is held
      if e.type == KEYDOWN: #check if it is a keypress event
          if e.key == K_LEFT: #Check which button is pressed
              x -= speed
          elif e.key == K_RIGHT:
              x += speed
          elif e.key == K_UP:
              y -= speed
          elif e.key == K_DOWN:
              y += speed
  draw.rect(window, (0, 0, 255), (x, y, width, height))
 
  #----------------------------------------------------------------------------
  #managing and updating the image sprite picture
  #a more complex solution - stop when a key is released, the character stays within screen borders.
  window.blit(img1, (x2, y2))
  keys = key.get_pressed()
  if keys[K_LEFT] and x2 > 5:
      x2 -= speed
  if keys[K_RIGHT] and x2 < 595:
      x2 += speed
  if keys[K_UP] and y2 > 5:
      y2 -= speed
  if keys[K_DOWN] and y2 < 395:
      y2 += speed
  display.update()
