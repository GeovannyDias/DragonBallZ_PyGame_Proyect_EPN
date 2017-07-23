import pygame
 
class Serge(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('g4.png')
#Utilizamos el método set_clip () para mostrar sólo el fotograma 1 de nuestra hoja sprite.
        self.sheet.set_clip(pygame.Rect(350,0,60,100))
#Asignamos nuestra imagen actual al área cortada.
        self.image = self.sheet.subsurface(self.sheet.get_clip())
#Cree un objeto rect para que corresponda a nuestra imagen.
        self.rect = self.image.get_rect()
#Asigne la posición de forma que corresponda al píxel superior izquierdo de nuestro rect.
        self.rect.topleft = position
#Asigne nuestro marco actual a 0; Esta variable se utilizará más tarde para recorrer los marcos.
        self.frame = 0
#Cree 4 diccionarios para almacenar las coordenadas de píxeles de nuestros marcos de animación. 
        self.left_states = { 0: (350,0,60,100), 1: (410,0,55,100), 2: (464,0,60,100) }
        self.right_states = { 0: (530,0,75,95), 1: (605,0,60,90), 2: (670,0,75,90) }
        self.up_states = { 0: (120,65,45,90), 1: (165,60,55,90), 2: (220,65,45,90) }
        self.down_states = { 0: (265,100,65,90), 1: (330,90,47,90), 2: (377,90,70,90) }