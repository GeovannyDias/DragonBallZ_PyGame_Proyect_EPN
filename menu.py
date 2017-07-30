# -*- coding: utf-8 -*-
#
# autor: Hugo Ruscitti
# web: www.losersjuegos.com.ar
# licencia: GPL 2

from pygame import * 
from pygame.locals import *
#import pruebaPyGame as i

class Menu:
    "Representa un menú con opciones para un juego" 
    def __init__(self, opciones):
        self.opciones = opciones
        self.font=font.SysFont("Showcard Gothic",40)
        self.seleccionado = 0
        self.total = len(self.opciones)
        self.mantiene_pulsado = False

    def actualizar(self):
        """Altera el valor de 'self.seleccionado' con los direccionales."""
        k = key.get_pressed()
        if not self.mantiene_pulsado:
            if k[K_UP]:
                self.seleccionado -= 1
            elif k[K_DOWN]:
                self.seleccionado += 1
            elif k[K_RETURN]:

                # Invoca a la función asociada a la opción.
                titulo, funcion = self.opciones[self.seleccionado]
                print ("Selecciona la opción '%s'." %(titulo))
                funcion()

        # procura que el cursor esté entre las opciones permitidas
        if self.seleccionado < 0:
            self.seleccionado = 0
        elif self.seleccionado > self.total - 1:
            self.seleccionado = self.total - 1

        # indica si el usuario mantiene pulsada alguna tecla.
        self.mantiene_pulsado = k[K_UP] or k[K_DOWN] or k[K_RETURN]

    def imprimir(self, screen):
        """Imprime sobre 'screen' el texto de cada opción del menú."""

        total = self.total
        indice = 0
        altura_de_opcion = 50
        x = 30
        y = 250
        
        for (titulo, funcion) in self.opciones:
            if indice == self.seleccionado:
                color = (0, 255, 0)
            else:
                color = (255,255,255)

            imagen = self.font.render(titulo, 1, color)
            posicion = (x, y + altura_de_opcion * indice)
            indice += 1
            screen.blit(imagen, posicion)

def comenzar_nuevo_juego():
    print (" Función que muestra un nuevo juego.")
    #i.inicio()


def mostrar_opciones():
    print (" Función que muestra otro menú de opciones.")

def creditos():
    print (" Función que muestra los creditos del programa.")

def salir_del_programa():
    import sys
    print (" Gracias por utilizar este programa.")
    sys.exit(0)


if __name__ == '__main__':
    
    salir = False
    opciones = [
        ("JUGAR", comenzar_nuevo_juego),
        ("Opciones", mostrar_opciones),
        ("Creditos", creditos),
        ("Salir", salir_del_programa)
        ]

    font.init()
    screen = display.set_mode((700, 400))
    fondo = image.load("g2.jpg").convert()
    #menup = image.load("m.png").convert()
    menu = Menu(opciones)
    #mixer.music.load("Dragon_Ball_Z.")

    while not salir:
        for e in event.get():
            if e.type == QUIT:
                salir = True

        screen.blit(fondo, (0, 0))
        #screen.blit(menup, (105, 80))
        menu.actualizar()
        menu.imprimir(screen)
        display.flip()
        time.delay(10)
