import pygame
from pygame.locals import *
pygame.init()
screen=pygame.display.set_mode((2000,1000))
pygame.display.set_caption("Shapes!!")
sblock=pygame.image.load(r"C:/Users/vigne/Downloads/deserttileset (1)/png/Objects/StoneBlock.png")
backround=pygame.image.load(r"C:/Users/vigne/Downloads/deserttileset (1)/png/BG.png")
backround=pygame.transform.scale(backround,(2000,1000))


walkr=[]
walkl=[]
runr=[]
runl=[]
jumpr=[]
jumpl=[]
walk=0
flag='now'
x=1000
y=500
idler=[]
idlel=[]
uidle=0
direct='r'
def load(): 
    for movewalk in range(1,11,1):
        img=pygame.image.load('png\Walk ('+str(movewalk)+').png')
        img=pygame.transform.scale(img,(300,300))
        walkr.append(img)
        img=pygame.transform.flip(img,True,False)
        walkl.append(img)
    for moverun in range(1,9,1):
        img=pygame.image.load('png\Run ('+str(moverun)+').png')
        img=pygame.transform.scale(img,(300,300))
        runr.append(img)
        img=pygame.transform.flip(img,True,False)
        runl.append(img)
    for movejump in range(1,13,1):
        img=pygame.image.load('png\Jump ('+str(movejump)+').png')
        img=pygame.transform.scale(img,(300,300))
        jumpr.append(img)
        img=pygame.transform.flip(img,True,False)
        jumpl.append(img)
    for idle in range(1,11,1):
        img=pygame.image.load('png\Idle ('+str(idle)+').png')
        img=pygame.transform.scale(img,(300,300))
        idler.append(img)
        img=pygame.transform.flip(img,True,False)
        idlel.append(img)
def walkleft():
    global walk
    screen.blit(walkl[walk],(x,y))
    walk=walk+1
    if walk==10:
        walk=0
def walkright():
    global walk
    screen.blit(walkr[walk],(x,y))
    walk=walk+1
    if walk==10:
        walk=0
def idleright():
    global uidle
    screen.blit(idler[uidle],(x,y))
    uidle=uidle+1
    if uidle==10:
        uidle=0
def idleleft():
    global uidle
    screen.blit(idlel[uidle],(x,y))
    uidle=uidle+1
    if uidle==10:
        uidle=0
load()
    
    
    

    
    
    

    


    

while True:
    screen.blit(backround,(0,0))
    
    screen.blit(sblock,(1000,670))
    
    
    
    

    
    

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()
        if event.type==KEYDOWN:
            if event.key==pygame.K_RIGHT:
                flag=='now'
                direct='r'

            if event.key==pygame.K_LEFT:
                
  
                flag='now'
                direct='l'

            
        
    
        if event.type==KEYUP:
            
            flag='no'
    if flag=='now' and direct=='r':
        walkright()
        print(1)
        x=x+10
    if flag=='no' and direct=='r':
        idleright()
    print(direct,flag)
    if flag=='no' and direct=='l':
        idleleft()
    if flag=='now' and direct=='l':
        walkleft()
        x=x-10
    

            
            

            
                
    pygame.display.update()
