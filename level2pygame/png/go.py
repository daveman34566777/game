import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
red=[250,0,0]
green=[0,250,0]
x=300
y=300
f=1
clock=pygame.time.Clock()
while True:
    screen.fill(green)
    clock.tick(0.01)
    
    pygame.draw.circle(screen, red, (x, y), 50)
    if x>=600 and y>=600:
        f=1
    if f==1:
        x=x-10
        y=y-10
    if x<=0 and y<=0:
        f=2
    if f==2:
        x=x+10
        y=y+10
    


    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()
