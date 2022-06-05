#Connect the required modules
import pygame
from random import randint
pygame.init()
#create a game window
clock = pygame.time.Clock()
back = (255, 255, 255) #background color
mw = pygame.display.set_mode((500, 500)) #main window
mw.fill(back)
#colors
BLACK = (0, 0, 0)
LIGHT_BLUE = (200, 200, 255)
class TextArea():
  def __init__(self, x=0, y=0, width=10, height=10, color=None):
      self.rect = pygame.Rect(x, y, width, height)
      self.fill_color = color
      #possible labels
      self.titles = list()
 
  #add text to the list of possible labels
  def add_text(self, text):
      self.titles.append(text)
 
  #place text
  def set_text(self, number=0, fsize=12, text_color=BLACK):
      self.text = self.titles[number]
      self.image = pygame.font.Font(None, fsize).render(self.text, True, text_color)
    
  #draw a rectangle with text
  def draw(self, shift_x=0, shift_y=0):
      pygame.draw.rect(mw, self.fill_color, self.rect)
      mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))  
#create cards
quest_card = TextArea(120, 100, 290, 70, LIGHT_BLUE)
quest_card.add_text('Question')
quest_card.add_text('What do you study at Algorithmics?')
quest_card.add_text('What language is spoken in France?')
quest_card.add_text('What grows on an apple tree?')
quest_card.add_text('What falls from the sky when it rains?')
quest_card.add_text('What are they eating for dinner?')
quest_card.set_text(0, 75)
ans_card = TextArea(120, 240, 290, 70, LIGHT_BLUE)
ans_card.add_text('Answer')
ans_card.add_text('Python')
ans_card.add_text('French')
ans_card.add_text('Apples')
ans_card.add_text('Raindrops')
ans_card.add_text('A roast with mushrooms')
ans_card.set_text(0, 75)
quest_card.draw(10,10)
ans_card.draw(10,10)
 
while 1:
  pygame.display.update()
  for event in pygame.event.get():
      if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_q:
              num = randint(1, len(quest_card.titles)-1)   
              quest_card.set_text(num, 25)
 
              quest_card.draw(10,25)
          if event.key == pygame.K_a:
              num = randint(1, len(ans_card.titles)-1) 
              ans_card.set_text(num, 25)
 
              ans_card.draw(10, 25)
  clock.tick(40)
