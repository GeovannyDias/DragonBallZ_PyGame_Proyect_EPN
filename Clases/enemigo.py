import pygame
import sys
from pygame.locals import *


class Enemigo(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagenArray):
        pygame.sprite.Sprite.__init__(self)

        self.arrayAnim=imagenArray        
        self.anim= 0   
        self.actualizado = pygame.time.get_ticks()
        #print(self.actualizado)
        self.image = self.arrayAnim[self.anim]
        #Aumenta la imagen al doble de su tamaño normal
        #self.image = pygame.transform.scale2x(self.arrayAnim[self.anim])        
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas


    def update(self):
        #self.rect.center = nuevas_coordenadas
        #ventana.blit(self.arrayAnim[self.anim], self.rect)

        if self.actualizado + 1000 < pygame.time.get_ticks():

            self.image = self.arrayAnim[self.anim]
            
            #Aumenta la imagen al doble de su tamaño normal
            #self.image = pygame.transform.scale2x(self.arrayAnim[self.anim])

            #Invierte la imagen de manera horizontal y vertical.
            #self.image = pygame.transform.flip(self.arrayAnim[self.anim], True, False)

            self.anim= self.anim + 1
            #print(self.anim," amin")#Eliminar

            if self.anim > len(self.arrayAnim)-1:
                self.anim= 0
            
            self.actualizado= pygame.time.get_ticks()
            #print(self.actualizado, " act")

    def mover(self, movX,movY):
        self.rect.move_ip(movX,movY)



    