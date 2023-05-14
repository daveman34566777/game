# import pygame
# from pygame.locals import *
# pygame.init()
# screen=pygame.display.set_mode((640,480))
# pygame.display.set_caption("Shapes!!")
# red=(255,0,0)
# blue=(0,0,255)
# y1=50
# a1='True1'
# b1='True2'
# a2='True3'
# b2='True4'
# f=True
# c=1
# y2=50
# x=320AAAA
# y=240
# r=30
# xtemp=10
# ytemp=10
# x1=0
# x2=590
# a=0
# b=0
# clock=pygame.time.Clock()
# def show_text(msg, x, y, color, size):
#         fontobj= pygame.font.SysFont("freesans", size)
#         msgobj = fontobj.render(msg,False,color)
#         screen.blit(msgobj,(x, y))
# while True:
#     clock.tick(20)
#     screen.fill(blue)
#     show_text (str(b),320,0,red,100)
#     show_text (str(a),370,0,red,100)
#     pygame.draw.rect(screen,red,(x1,y1,50,150))
#     pygame.draw.rect(screen,red,(x2,y2,50,150))
#     pygame.draw.circle(screen,red,(x,y),r)


#     x=x+xtemp
#     y=y+ytemp
#     #wall bounsing

#     # if y+r>=480:
#     #     ytemp=-ytemp
#     # if y-r<=0:
#     #     ytemp=-ytemp
#     #     # respon
    
        
#     # colison
#     if x>=x2 and y>=y2 and y<=y2+150:
#         print('hit')
#         xtemp=-xtemp
#     if x<=x1+(2*r) and y>=y1 and y<=y1+150:
#         print('hit')
#         xtemp=-xtemp
#     # ball bousing
#     if y==480 or y==0:
#         ytemp=-ytemp

#     # points
#     if x==0:
#         a=a+1
#         x=320
#     if x==590:
#         b=b+1
#         x=320
#     print(a,b)

        
    
#     for event in pygame.event.get():
#         if event.type == QUIT:
#             pygame.quit()
#             exit()
#         if event.type==pygame.KEYDOWN:
#             if event.key==pygame.K_s:
#                 a1='False1'
#             if event.key==pygame.K_w:
#                 b1='False2'
#             if event.key==pygame.K_DOWN:
#                 a2='False3'
#             if event.key==pygame.K_UP:
#                 b2='False4'
        


#         if event.type==pygame.KEYUP:
#             a1='True1'
#             b1='True2'
#             a2='True3'
#             b2='True4'
#     if a1=='False1' and y1<=640-300:
#         y1=y1+10
#     if b1=='False2' and y1>=0:
#         y1=y1-10
#     if a2=='False3' and y2<=640-300:
#         y2=y2+10
#     if b2=='False4' and y2>=0:
#         y2=y2-10
    


#     pygame.display.update()



import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
red=(255,0,0)
blue=(0,0,255)
clock=pygame.time.Clock()
a1=300 #slider x position
a=0
a2=300
x=300
y=300
move='down'


import random 


while True:
    clock.tick(60)
    screen.fill(blue)
    # top pad
    pygame.draw.rect(screen, red, (a1, 550, 200, 50))
    # r=random.randint(1,2)
    pygame.draw.circle(screen, red, (x,y), 50) 
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_d:
                a='False1'
            if event.key==pygame.K_a:
                a='False2'
        if event.type==pygame.KEYUP:
            a=0
    if move=='down':           
        y=y+10
        
        
        
    if x+50>=a1 and x+50>=a1+50 and y+50>=550 and y+50>=550+50:
        if x+50>=a1 and x+50<=a1+100:
            print('g')
            move='left'
        if x+50>a1+100 and x+50<=a1+200 :
            print('d')
            move='right'
    if move=='left':
        x=x-10
        y=y-10
    if move=='right':
        x=x+10
        y=y-10
    if y==0:
        move='down'
    if x==600:
        move='down'
    if x==0:
        move='down'


        
        
        
        

    if move=='up':
        y=y-10
        
        
        
    if y==0:
        move='down'
    
 
    if y==750:
        print('you died')
        exit()




            
    if event.type==pygame.KEYUP:
        a=0
    if a=='False1' and a1<=400:
            a1=a1+10
    if a=='False2' and a1>=10:
        a1=a1-10




        
        

    pygame.display.update()