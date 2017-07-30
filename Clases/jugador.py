"""
http://www.losersjuegos.com.ar/traducciones/pygame/transform
Módulo de pygame para transformar superficies.
flip = Invierte la imagen de manera horizontal y vertical.
pygame.transform.flip(imagen, xbool=True, ybool=False)
scale = Altera el tamaño.
pygame.transform.scale(imagen, (width=121, height=50))
rotate = Aplica rotación a una imagen.
pygame.transform.rotate(imagen, angle=190)
scale2x = Duplica el tamaño de la imagen de manera especial.
pygame.transform.scale2x(imagen)

"""
#==========================================
import pygame
import sys
from pygame.locals import *

class Jugador(pygame.sprite.Sprite):

    def __init__(self, coordenadas, imagenArray):
        pygame.sprite.Sprite.__init__(self)

        self.arrayAnim=imagenArray
        self.animA= 0
        self.animB= 0
        self.actualizado = pygame.time.get_ticks()
        self.image = self.arrayAnim[self.animA][self.animB]
        #Aumenta la imagen al doble de su tamaño normal
        #self.image = pygame.transform.scale2x(self.arrayAnim[self.anim])        
        self.rect = self.image.get_rect()
        self.rect.center = coordenadas

        self.accionAtaque = True


    def update(self):
        #self.rect.center = nuevas_coordenadas
        #ventana.blit(self.arrayAnim[self.anim], self.rect)

        if self.actualizado + 100 < pygame.time.get_ticks():

            if self.accionAtaque == True:

	            self.image = self.arrayAnim[self.animA][self.animB]

	            #Aumenta la imagen al doble de su tamaño normal
	            #self.image = pygame.transform.scale2x(self.arrayAnim[self.anim])

	            #Invierte la imagen de manera horizontal y vertical.
	            #self.image = pygame.transform.flip(self.arrayAnim[self.anim], True, False)

	            self.animB= self.animB + 1
	            #print(self.anim," amin")#Eliminar
	            #print(len(self.arrayAnim[0]))
	            if self.animB > len(self.arrayAnim[self.animA])-1:
	                self.animB= 0
	            
	            self.actualizado= pygame.time.get_ticks()
	            #print(self.actualizado, " act")
            else:
            	#pass
                self.__ataque1()



    def __ataque1(self):
        #self.rect.center = nuevas_coordenadas
        #ventana.blit(self.arrayAnim[self.anim], self.rect)

        #if self.actualizado + 100 < pygame.time.get_ticks():

            if self.animB > len(self.arrayAnim[3])-1:
            	self.animB = 0
            	print("Se Evalua IndexArray")


            self.image = self.arrayAnim[3][self.animB]

            #Aumenta la imagen al doble de su tamaño normal
            #self.image = pygame.transform.scale2x(self.arrayAnim[self.anim])

            #Invierte la imagen de manera horizontal y vertical.
            #self.image = pygame.transform.flip(self.arrayAnim[self.anim], True, False)

            self.animB= self.animB + 1
            #print(self.anim," amin")#Eliminar
            #print(self.image)
            if self.animB > len(self.arrayAnim[3])-1:
                self.animB= 0
                self.accionAtaque = True
            
            self.actualizado= pygame.time.get_ticks()
            #print(self.actualizado, " act")



    def ImagenInvertida(self, invertir):
        imagenArrayOriginal = self.arrayAnim
        if invertir:
            imagenArray_Inv = self.__invertirListaArray(self.arrayAnim)
            self.arrayAnim = imagenArray_Inv
        else:
            self.arrayAnim = imagenArrayOriginal



    def __invertirListaArray(self, imagenArray_Org):
        invertirArray = []
        imagenArrayInvertida = []
        size = len(imagenArray_Org)

        for i in range(size):
            print(" i : ", i)
            for j in range (len(imagenArray_Org[i])):
                print(" j : ",j)
                # ---Invierte la imagen de manera horizontal y vertical.---
                Imagen_Inv = pygame.transform.flip(imagenArray_Org[i][j], True, False)
                invertirArray.append(Imagen_Inv)

            imagenArrayInvertida.append(invertirArray)
            invertirArray = []
        return imagenArrayInvertida







