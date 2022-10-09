import pygame
from random import *
from time import *

pygame.init()

class Card():
    def __init__(self,x,y,width,height,color):
        self.rect = pygame.Rect(x,y,width,height)
        self.color = color
    def set_color(self,new_color):
        self.color = new_color
    def fill(self):
        pygame.draw.rect(window,self.color, self.rect)
    def draw_outline(self,thickness, border_color):
        pygame.draw.rect(window, border_color, self.rect, thickness)
    def collidepoint(self,x,y):
        return self.rect.collidepoint(x,y)

class label(Card):
    def set_text(self,text,font_size,text_color):
        self.image = pygame.font.SysFont('Times New Roman',font_size).render(text,True,text_color)
    def draw(self,shift_x,shift_y):
        self.fill()
        window.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))

window = pygame.display.set_mode((300,300))
background_color = (119,136,158)
window.fill(background_color)

text_color = (127,255,212)
card_color = (255,234,0)
border_color = (0,0,0)
danger_color = (49,27,146)
good_color = (243,156,18)
clickgood_color = (210,127,37)
clickdanger_color = (21,67,90)
clicknormal_color = (212,172,13)

score = 0
time_text = label(0,0,50,50,background_color)
time_text.set_text("Time:",40,text_color)

timer_text = label(50,55,50,40, background_color)
timer_text.set_text("0",40,text_color)

score_text = label(380,0,50,50,background_color)
score_text.set_text("Score:",40,text_color)

scorecount_text = label(430,55,50,40, background_color)
scorecount_text.set_text("0",40,text_color)
cards = []
x = 20
num_cards = 6
for y in range(num_cards):
    card = Card(x, 160, 85, 130, card_color)
    card.draw_outline(5,border_color)
    cards.append(card)
    x = x + 110

clock = pygame.time.Clock()
while True:
    time_text.draw(0,0)
    timer_text.draw(0,0)
    score_text.draw(0,0)
    scorecount_text.draw(0,0)

    # card.draw_outline(5,border_color)
    danger = randint(1,num_cards)
    good = randint(1,num_cards)
    
    while good == danger:
        good = randint(1,num_cards)
    for i in range(6):
        if (i + 1) == danger:
            cards[i].set_color(danger_color)
        elif (i + 1) == good:
            cards[i].set_color(good_color)
        else:
            cards[i].set_color(card_color)
        cards[i].fill()
    sleep(0.5)
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            x,y = event.pos
            for i in range(num_cards):
                if cards[i].collidepoint(x,y):
                    if (i + 1) == danger:
                        cards[i].set_color(clickdanger_color)
                        score -= 1
                    elif (i + 1) == good:
                        cards[i].set_color(clickgood_color)
                        score += 1
                    else:
                        cards[i].set_color(clicknormal_color)
                        score -= 1
                    cards[i].fill()
                    scorecount_text.set_text(str(score),40,text_color)
                    scorecount_text.draw(0,0)
    if score >= 1:
        win_text = label(200,200,100,20,good_color)
        win_text.set_text('You win!',40,text_color)
        win_text.draw(0,0)
 
    pygame.display.update()
    clock.tick(30)










