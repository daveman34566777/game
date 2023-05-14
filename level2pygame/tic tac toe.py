import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((600,600))
pygame.display.set_caption("Shapes!!")
import random
red=[250,0,0]
blue=[0,0,250]
f=320

dic={1:' ',2:' ',3:' ',4:' ',5:' ',6:' ',7:' ',8:' ',9:' '}
r=random.randint(1,9)

def x1(x,y):
    pygame.draw.line(screen,blue,(x-50,y-50),(x+50,y+50),10)
    pygame.draw.line(screen,blue,(x+50,y-50),(x-50,y+50),10)
def ci(x,y):
    pygame.draw.circle(screen,blue,(x,y),50)

t=True    
while True:
    r=random.randint(1,9)
    pygame.draw.line(screen,red,(0,0),(0,600),50)
    pygame.draw.line(screen,red,(600,0),(600,600),50)
    pygame.draw.line(screen,red,(0,200),(600,200),20)
    pygame.draw.line(screen,red,(0,600),(600,600),50)
    pygame.draw.line(screen,red,(0,0),(600,0),50)
    pygame.draw.line(screen,red,(0,400),(600,400),20)
    pygame.draw.line(screen,red,(200,0),(200,600),20)
    pygame.draw.line(screen,red,(400,0),(400,600),20)
    x=600
    y=600

    
    
    for event in pygame.event.get():
        if t==False:
            if dic[5]==' ' and r==5:
                x=300
                y=300
                ci(x,y)
                dic[5]='o'
                t=True
            if dic[1]==' ' and r==1:
                x=100
                y=100
                ci(x,y)
                dic[1]='o'
                t=True
            if dic[9]==' ' and r==9:
                x=500
                y=500
                ci(x,y)
                dic[9]='o'
                t=True
            if dic[2]==' ' and r==2:
                x=300
                y=100
                ci(x,y)
                dic[2]='o'
                t=True
            if dic[3]==' ' and r==3:
                x=500
                y=100

                ci(x,y)
                dic[3]='o'
                t=True
            if dic[4]==' ' and r==4:
                x=100
                y=300
                ci(x,y)
                dic[4]='o'
                t=True
            if dic[6]==' 'and r==6:
                x=500
                y=300
                ci(x,y)
                dic[6]='o'
                t=True
            if dic[7]==' ' and r==7:
                x=100
                y=500
                ci(x,y)
                dic[7]='o'
                t=True
            if dic[8]==' 'and r==8:
                x=300
                y=500
                ci(x,y)
                dic[8]='o'
                t=True
        if event.type==pygame.MOUSEBUTTONDOWN:

            if event.button==1:

                f=event.pos
                x,y=event.pos

                
                if x>=200 and x<=400 and y>=200 and y<=400:
                    x=300
                    y=300


                    if dic[5]==' 'and t==True:                 
                        x1(x,y)
                        dic[5]='x'
                        t=False



                    
                if x>=50 and x<=200 and y>=50 and y<=200:
                    x=100
                    y=100

                    if dic[1]==' 'and t==True:                 
                        x1(x,y)
                        dic[1]='x'
                        t=False

                if x>=400 and x<=600 and y>=400 and y<=600:
                    x=500
                    y=500

                    if dic[9]==' 'and t==True:                 
                        x1(x,y)
                        dic[9]='x'
                        t=False

                if x>=200 and x<=400 and y>=0 and y<=200:
                    x=300
                    y=100

                    if dic[2]==' 'and t==True:                 
                        x1(x,y)
                        dic[2]='x'
                        t=False

                if x>=400 and x<=600 and y>=0 and y<=200:
                    x=500
                    y=100

                    if dic[3]==' 'and t==True:                 
                        x1(x,y)
                        dic[3]='x'
                        t=False
 
                if x>=50 and x<=200 and y>=200 and y<=400:
                    x=100
                    y=300

                    if dic[4]==' 'and t==True:                 
                        x1(x,y)
                        dic[4]='x'
                        t=False

                if x>=400 and x<=600 and y>=200 and y<=400:
                    x=500
                    y=300

                    if dic[6]==' 'and t==True:                 
                        x1(x,y)
                        dic[6]='x'
                        t=False

                if x>=0 and x<=200 and y>=400 and y<=600:
                    x=100
                    y=500

                    if dic[7]==' 'and t==True:                 
                        x1(x,y)
                        dic[7]='x'
                        t=False

                if x>=200 and x<=400 and y>=400 and y<=600:
                    x=300
                    y=500

                    if dic[8]==' 'and t==True:                 
                        x1(x,y)
                        dic[8]='x'
                        t=False

                if dic[1]==dic[2]==dic[3]!=' ':
                    print(dic[1],'you won')
                    exit()
                if dic[4]==dic[5]==dic[6]!=' ':
                    print(dic[4],'you won')
                    exit()
                if dic[7]==dic[8]==dic[9]!=' ':
                    print(dic[7],'you won')
                    exit()
                if dic[1]==dic[4]==dic[7]!=' ':
                    print(dic[1],'you won')
                    exit()
                if dic[2]==dic[5]==dic[8]!=' ':
                    print(dic[2],'you won')
                    exit()
                if dic[3]==dic[6]==dic[9]!=' ':
                    print(dic[3],'you won')
                    exit()
                if dic[1]==dic[5]==dic[9]!=' ':
                    print(dic[1],'you won')
                    exit()
                if dic[3]==dic[5]==dic[7]!=' ':
                    print(dic[3],'you won')
                    exit()
                
                
                
        if event.type==pygame.MOUSEMOTION:
            f=event.pos 
        if event.type == QUIT:
            pygame.quit()
            exit()
    pygame.display.update()

