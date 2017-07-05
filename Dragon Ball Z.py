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
            
