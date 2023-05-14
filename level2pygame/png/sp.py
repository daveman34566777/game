import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((1000,1000))
pygame.display.set_caption("Shapes!!")
import random

x=300
y=300
u=[]
move=[]
still=[]
count=0
red=[255,0,0]
dead=[]
p=0
e=0
x1=300
y1=350
bulit=[]
tx=800
ty=500
m='u'
clock=pygame.time.Clock()
for i in (0,7,1):
    
    rr=pygame.image.load("png\Run ("+str(i+1)+").png")
    rl=pygame.transform.flip(rr,True,False)
    # move.append(rr)
    # u.append(rl)
# for l in (0,8,1):
i=pygame.image.load("png\gun1.png")
i=pygame.transform.scale(i,(500,250))

#     still.append(i)
# for d in (0,7,1):
d=pygame.image.load("png\progectile.png")
d=pygame.transform.scale(d,(50,100))
d=pygame.transform.rotate(d,-90)
f=pygame.image.load('png\Walk (1).png')
f=pygame.transform.scale(f,(500,400))





#      dead.append(dd)




while True:
    screen.fill(red)
    screen.blit(f,(tx,ty))
    
    
    clock.tick(60)
    
    


    
    
    
    

    # count+=1
    # if count==len(move):
    #     count=0
    # if count==len(u):
    #      count=0



    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        
        if event.type==KEYDOWN:
            if event.key==pygame.K_UP:
                p=True
            if event.key==pygame.K_SPACE:
                 
                bulit.append([x,y])
                 
                



                

            if event.key==pygame.K_DOWN:
                p=False
                

        
        if event.type==KEYUP:
            p=9

             
    if p==True:
            
            screen.blit(i,(x,y))
            y=y-10
    if p==False:
            
            screen.blit(i,(x,y))
            y=y+10
    if p==9:
         
         screen.blit(i,(x,y))

    # if e=='t':
    if len(bulit)>0:
        # this is for swaning bulits
        for shoot in range(0,len(bulit),1):
            c=bulit[shoot]
            screen.blit(d,(c[0],c[1]))
            
            
            
            bulit[shoot][0]=bulit[shoot][0] +10
        # this is for deliting bulits
        for gone in bulit:
                if gone[0]>=1000:
                  bulit.remove(gone)
                if gone[0]>=tx and gone[1]>=ty and gone[1]<=ty+400:
                     r=random.randint(0,800)
                     ty=r
                    
             
                
              


    

        

            
    pygame.display.update()