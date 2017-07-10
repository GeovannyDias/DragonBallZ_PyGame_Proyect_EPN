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
imagen = image.load("Imagenes/g2.jpg")
font = font.SysFont("Showcard Gothic", 15)
######## texto botones ##########
txtb1 = font.render("Jugar", True, (0, 0, 0))
txtb2 = font.render("Instruciones", True, (0, 0, 0))
txtb3 = font.render("Puntaje", True, (0, 0, 0))
########## Colores #########
morado= Color(100,90,255)
verde=Color(0,255,50)
morado1=Color(100,90,255)
plomo= Color(232,224,224)
blanco=Color(255,255,255)
negro=Color(0,0,0)
#### datos de boton ###
boton1,tamb1,colorb1=[80,200],[100,30],[plomo,morado]
boton2,tamb2,colorb2=[50,250],[150,30],[plomo,verde]
boton3,tamb3,colorb3=[80,300],[100,30],[plomo,morado1]
######### nombre de los botones ######
def mensaje_boton(msg,color,bx,by,anchb,altb,tamaño="pequeño"):
    textoSuperficie,textoRect=objetotexto(msg,color,tamaño)
    textoRect.center=(bx+(anchb/2),by+(altb/2))
    v.blit(textoSuperficie,textoRect)

def objetotexto(texto,color,tamaño):
    if tamaño=="pequeño":
        textoSuperficie=font.render(texto,True,color)
    return textoSuperficie, textoSuperficie.get_rect()
########### DIBUJAR BOTONES ############
def botones(texto,superficie,estado,posicionamiento,tam):
    cursor=mouse.get_pos()
    if posicionamiento[0]+tam[0]>cursor[0]>tam[0] and posicionamiento[1]+tam[1]>cursor[1]>tam[1] and posicionamiento[1]+tam[1]<cursor[1]+tam[1]:
         boton=draw.rect(superficie,estado[1],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
         mensaje_boton(texto,negro,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
    else:
         boton=draw.rect(superficie, estado[0],(posicionamiento[0],posicionamiento[1],tam[0],tam[1]))
         mensaje_boton(texto,negro,posicionamiento[0],posicionamiento[1],tam[0],tam[1])
    return boton

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
