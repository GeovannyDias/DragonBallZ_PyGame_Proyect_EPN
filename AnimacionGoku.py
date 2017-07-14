import sys, pygame
from pygame.locals import*
WIDTH=900
HEIGHT=500
MposX=100

cont=0
direc=True
i=0
xixf={}
Rxixf={}
#IMAGEN#
def imagen(filename, transparent=False):
    image=pygame.image.load(filename)
    image=image.convert()

    if transparent:
        color=image.get_at((0,0))
        image.set_colorkey(color,RLEACCEL)
    return image
#TECLADO#
def teclado():
    teclado=pygame.key.get_pressed()
    global MposX
    global cont, direc

    if teclado[K_RIGHT]:
        MposX+=2
        cont+=1
        direc=True
    elif teclado[K_LEFT]:
        MposX-=2
        cont+=1
        direc=False
    return

#SPRITE#
def sprite():
    global cont
    xixf[0]=(0,0,65,100)
    xixf[1]=(66,0,60,65)
    xixf[2]=(120,0,60,65)
    xixf[3]=(185,0,55,65)
    xixf[4]=(240,0,53,65)
    xixf[5]=(293,0,60,100)
    xixf[6]=(350,0,60,100)

    p=7
    global i
    
    if cont==p:
        i=0
        
    if cont==p*2:
        i=1
   
    if cont==p*3:
        i=2
   
    if cont==p*4:
        i=3
   
    if cont==p*5:
        i=4
   
    if cont==p*6:
       i=5
    if cont==p*7:
        i=6
    cont=0
    
    return

def main():
    pygame.init()
    vtn=pygame.display.set_mode((WIDTH,HEIGHT))
    pygame.display.set_caption("DRAGON BALL Z")
    fondo=imagen("fondov.jpg")
    goku=imagen("gok.png",True)
    goku_inv=pygame.transform.flip(goku,True,False)
    clock=pygame.time.Clock()

    #Bucle Ventana#
    while True:
        time=clock.tick(60)
        sprite()
        teclado()
        fondo=pygame.transform.scale(fondo,(1000,500))
        vtn.blit(fondo,(0,0))
        if direc==True:
            vtn.blit(goku,(MposX,318),(xixf[i]))
            print(MposX,318)
            print(xixf[i])
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                sys.exit()
    return 0

if __name__=='__main__':
    main()
