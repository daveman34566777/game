import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((900,600))
pygame.display.set_caption("Shapes!!")
import random
yellow=(255,255,0)
blue=(0,0,255)
def show_text(msg, x, y, color, size):
        fontobj= pygame.font.SysFont("freesans", size)
        msgobj = fontobj.render(msg,False,color)
        screen.blit(msgobj,(x, y))
def game():
    blue=(0,0,255)
    x=300
    y=300
    ychange=50
    clock=pygame.time.Clock()
    m=900
    h=50
    while True:
        clock.tick(40)
        y=y+3
        m=m-5
        if h==600 and m<=0:
            h=0
        if m<=0:
            m=900
            h=random.randint(0,450)


        screen.fill(blue)
        pygame.draw.circle(screen,yellow,(x,y),20)
        pygame.draw.rect(screen,yellow,(m,0,50,h))
        pygame.draw.rect(screen,yellow,(m,h+100,50,600))
        for event in pygame.event.get():
            if event.type==KEYDOWN:      
                if event.key==K_SPACE:
                    y=y-ychange
            if event.type == QUIT:
                pygame.quit()
                exit()
            if m>=230 and m<=320:
                if y>=0 and y<=h+20 or  y>=h+100-20:
                    print('you die')
                    return()


        

        pygame.display.update()
def meue():
    while True:
        pygame.draw.rect(screen,yellow,(450,300,200,50))
        show_text('play',450,300,blue,40)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type==QUIT:
                exit()
            if event.type==pygame.MOUSEBUTTONDOWN:
                if event.button==1 and event.pos[0]>=450 and event.pos[0]<=550 and event.pos[1]>=300 and event.pos[1]<=350:
                    
                    game()
                    
meue()
                



