import pygame
 
class Serge(pygame.sprite.Sprite):
    def __init__(self, position):
        self.sheet = pygame.image.load('v3.png')
#Utilizamos el método set_clip () para mostrar sólo el fotograma 1 de nuestra hoja sprite.
        self.sheet.set_clip(pygame.Rect(583,0,48,80))
#Asignamos nuestra imagen actual al área cortada.
        self.image = self.sheet.subsurface(self.sheet.get_clip())
#Cree un objeto rect para que corresponda a nuestra imagen.
        self.rect = self.image.get_rect()
#Asigne la posición de forma que corresponda al píxel superior izquierdo de nuestro rect.
        self.rect.topleft = position
#Asigne nuestro marco actual a 0; Esta variable se utilizará más tarde para recorrer los marcos.
        self.frame = 0
#Cree 4 diccionarios para almacenar las coordenadas de píxeles de nuestros marcos de animación. 
        self.left_states = { 0: (583,0,48,80), 1: (422,0,50,80), 2: (312,0,50,80)}
        self.right_states = { 0: (110,256,48,80), 1: (159,256,50,80), 2: (10,272,48,80)}
        self.up_states = { 0: (625,459,48,80), 1: (579,457,48,80), 2: (288,456,48,80)}
        self.down_states = { 0: (211,0,48,80), 1: (164,0,50,80), 2: (116,0,55,80)}
#golpe
        self.knock_states= { 0: (139,191,80,40)}
        
#Para animar a nuestro personaje, necesitamos repetidamente recorrer tres cuadros
    def get_frame(self, frame_set):
        self.frame += 1
        if self.frame > (len(frame_set) - 1):
            self.frame = 0
        return frame_set[self.frame]
#Creamos un método para recortar el área de cada trama.
#Primero tenemos que comprobar si estamos tratando con múltiples marcos (movimiento) o un solo marco (de pie).
#Si el personaje se está moviendo, los marcos son manejados por el método get_frame (). Si el personaje está simplemente de pie,
#el marco es manejado directamente por las funciones incorporadas de Pygame.
    def clip(self, clipped_rect):
        if type(clipped_rect) is dict:
            self.sheet.set_clip(pygame.Rect(self.get_frame(clipped_rect)))
        else:
            self.sheet.set_clip(pygame.Rect(clipped_rect))
        return clipped_rect
#A continuación, Update () se basa en los dos métodos anteriores pasándoles los diccionarios (en el caso de movimiento)
#o solo marcos y moviendo el sprite en la dirección correcta usando los valores de pygame.sprite.Sprite rect.x y rect.y incorporados .
#A continuación, establece la imagen actual en el área cortada apropiada.
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
        
#Por último, creamos el método handle_event () para manejar pulsaciones de teclas 
    def handle_event(self, event):
        if event.type == pygame.QUIT:
            game_over = True
 
        if event.type == pygame.KEYDOWN:
        
            if event.key == pygame.K_a:
                self.update('left')
            if event.key == pygame.K_d:
                self.update('right')
            if event.key == pygame.K_w:
                self.update('up')
            if event.key == pygame.K_s:
                self.update('down')
 
        if event.type == pygame.KEYUP:  
 
            if event.key == pygame.K_a:
                self.update('stand_left')            
            if event.key == pygame.K_d:
                self.update('stand_right')
            if event.key == pygame.K_w:
                self.update('stand_up')
            if event.key == pygame.K_s:
                self.update('stand_down')
