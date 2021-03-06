import pygame
 
class Serge(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('g4.png')
#Utilizamos el m�todo set_clip () para mostrar s�lo el fotograma 1 de nuestra hoja sprite.
        self.sheet.set_clip(pygame.Rect(350,0,60,100))
#Asignamos nuestra imagen actual al �rea cortada.
        self.image = self.sheet.subsurface(self.sheet.get_clip())
#Cree un objeto rect para que corresponda a nuestra imagen.
        self.rect = self.image.get_rect()
#Asigne la posici�n de forma que corresponda al p�xel superior izquierdo de nuestro rect.
        self.rect.topleft = position
#Asigne nuestro marco actual a 0; Esta variable se utilizar� m�s tarde para recorrer los marcos.
        self.frame = 0
#Cree 4 diccionarios para almacenar las coordenadas de p�xeles de nuestros marcos de animaci�n. 
        self.left_states = { 0: (350,0,60,100), 1: (410,0,55,100), 2: (464,0,60,100) }
        self.right_states = { 0: (530,0,75,95), 1: (605,0,60,90), 2: (670,0,75,90) }
        self.up_states = { 0: (120,65,45,90), 1: (165,60,55,90), 2: (220,65,45,90) }
        self.down_states = { 0: (265,100,65,90), 1: (330,90,47,90), 2: (377,90,70,90) }
#Para animar a nuestro personaje, necesitamos repetidamente recorrer tres cuadros
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
#Creamos un m�todo para recortar el �rea de cada trama.
#Primero tenemos que comprobar si estamos tratando con m�ltiples marcos (movimiento) o un solo marco (de pie).
#Si el personaje se est� moviendo, los marcos son manejados por el m�todo get_frame (). Si el personaje est� simplemente de pie,
#el marco es manejado directamente por las funciones incorporadas de Pygame.
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect

#A continuaci�n, Update () se basa en los dos m�todos anteriores pas�ndoles los diccionarios (en el caso de movimiento)
#o solo marcos y moviendo el sprite en la direcci�n correcta usando los valores de pygame.sprite.Sprite rect.x y rect.y incorporados .
#A continuaci�n, establece la imagen actual en el �rea cortada apropiada.
    def update(self, direction):
        if direction == 'left':
            self.clip(self.left_states)
            self.rect.x -= 5
        if direction == 'right':
            self.clip(self.right_states)
            self.rect.x += 5
        if direction == 'up':
            self.clip(self.up_states)
            #self.rect.y -= 5
        if direction == 'down':
            self.clip(self.down_states)
            #self.rect.y += 5
 
        if direction == 'stand_left':
            self.clip(self.left_states[0])
        if direction == 'stand_right':
            self.clip(self.right_states[0])
        if direction == 'stand_up':
            self.clip(self.up_states[0])
        if direction == 'stand_down':
            self.clip(self.down_states[0])
 
        self.image = self.sheet.subsurface(self.sheet.get_clip())

#Por �ltimo, creamos el m�todo handle_event () para manejar pulsaciones de teclas 
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
 
        if event.type == pygame.KEYDOWN:
           
            if event.key == pygame.K_LEFT:
                self.update('left')
            if event.key == pygame.K_RIGHT:
                self.update('right')
            if event.key == pygame.K_UP:
                self.update('up')
            if event.key == pygame.K_DOWN:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_LEFT:
                self.update('stand_left')            
            if event.key == pygame.K_RIGHT:
                self.update('stand_right')
            if event.key == pygame.K_UP:
                self.update('stand_up')
            if event.key == pygame.K_DOWN:
                self.update('stand_down')