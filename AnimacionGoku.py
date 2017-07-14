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

    if transparect:
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
        direc=True
    return

#SPRITE#
d
