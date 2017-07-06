import pygame, sys
from pygame.locals import*

pygame.init()

vtn= pygame.display.set_mode((300,300))
pygame.display.set_caption("DRAGON BALL Z")

while True:
    for evento in pygame.event.get():
        if evento.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
            
############## Pantalla de presentacion########
# rojo, verde, azul
from pygame import *

init()
v = display.set_mode((700, 400))
display.set_caption("DRAGON BALL Z")
salir = False
imagen = image.load("g2.jpg")
font = font.SysFont("Showcard Gothic", 15)
######## texto botones ##########
txtb1 = font.render("Jugar", True, (0, 0, 0))
txtb2 = font.render("Instruciones", True, (0, 0, 0))
txtb3 = font.render("Puntaje", True, (0, 0, 0))
velo = 5
posy = 200


def botones():
    draw.rect(v, (100, 90, 255), (80, 200, 100, 30))
    v.blit(txtb1, (100, 210))

    draw.rect(v, (0, 255, 50), (50, 250, 150, 30))
    v.blit(txtb2, (70, 257))

    draw.rect(v, (100, 90, 255), (80, 300, 100, 30))
    v.blit(txtb3, (100, 310))


while salir == False:
    for evento in event.get():
        if evento.type == QUIT:
            salir = True
            quit()
            raise SystemExit
        elif evento.type == KEYDOWN:
            if evento.key == K_UP:
                posy = velo
            elif evento.key == K_DOWN:
                posy = velo
        elif evento.type == KEYUP:
            if evento.key == K_UP:
                print("tecla arriba")
            elif evento.key == K_DOWN:
                print("tecla abajo")
    v.fill((255, 255, 255))
    v.blit(imagen, (0, 0))
    botones()
    display.update()
