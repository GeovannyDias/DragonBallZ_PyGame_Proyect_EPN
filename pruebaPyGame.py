#https://gist.github.com/bluenex/0af2f41fda9954df73a8
#Advertencia linpng
#http://razonartificial.com/tutoriales-pygame/
#Tutoriales Pygame


def inicio():
    "RInicio juego"

    from pygame import *  # Importa el modulo pygame
    # import pygame.sys
    from pygame.locals import *  # carga las constantes del modulo pygame ej:  K_ESCAPE
    ancho = 600
    alto = 500

    #def __init__(self,):
    init()
    screen = display.set_mode((ancho,alto))
    display.set_caption("Prueba Pygame - Dragon Ball - Geo")
    fondo = image.load("Imagenes/fondo3.jpg")
    img = image.load("Imagenes/goku5.PNG")
    txtFuente = font.SysFont("Chiller", 50)
    texto = txtFuente.render("Ups..!!!",0,(255,255,255))
    posX = 200
    posY = 100
    speed = 10
    edge = True
    teclaLiberada = True
    txtGolpe = False
    while True:
        screen.blit(fondo, (0, 0))
        screen.blit(img, (posX, posY))
        for ev in event.get():
            print("Evento ",ev)
            if ev.type == QUIT:
                quit()
                exit()
            #print("1")
            elif ev.type == KEYDOWN:
                print("PRECIONADA")
                if ev.key == K_LEFT:
                    if posX > 1:
                        posX -= speed
                    txtGolpe = False
                elif ev.key == K_RIGHT:
                    if posX < 400:
                        posX += speed
                    txtGolpe = False
                elif ev.key == K_UP:
                    if posY > 1:
                        posY -= speed
                    txtGolpe = False
                elif ev.key == K_DOWN:
                    if posY < 270:
                        posY += speed
                    txtGolpe = False
                elif ev.key == K_RETURN:#para la tecla Enter usar K_RETURN
                    if posX < 400:
                        for i in range (400):
                            print(i)
                            if posX < 400:
                                posX += speed
                            else:
                                txtGolpe = True
                                #screen.blit(texto,(posX,0))
                                break
                elif ev.key == K_SPACE:
                    if posX > 1:
                        for i in range (400):
                            print(i)
                            if posX > 1:
                                posX -= speed
                            else:
                                txtGolpe = True
                                #screen.blit(texto, (posX, 0))
                                break

            elif ev.type == KEYUP:
                print("LIBERA")
                if ev.key == K_LEFT:
                    pass
                elif ev.key == K_RIGHT:
                    pass
                elif ev.key == K_UP:
                    pass
                elif ev.key == K_DOWN:
                    pass
        # if edge == True:
        #     if posX < 400:
        #         posX += speed
        #     else:
        #         edge = False
        # else:
        #     if posX > 1:
        #         posX -= speed
        #     else:
        #         edge = True
        if txtGolpe:
            screen.blit(texto, (posX, 0))
        display.update()

inicio()



#Proceso inverso

"""
  #def __init__(self,):
    init()
    screen = display.set_mode((ancho,alto))
    display.set_caption("Prueba Pygame - Dragon Ball - Geo")
    fondo = image.load("Imagenes/fondo3.jpg")
    img = image.load("Imagenes/goku5.PNG")
    txtFuente = font.SysFont("Chiller", 50)
    texto = txtFuente.render("Ups..!!!",0,(255,255,255))
    posX = 200
    posY = 100
    speed = 10
    edge = True
    teclaLiberada = True
    txtGolpe = False
    while True:
        screen.blit(fondo, (0, 0))
        screen.blit(img, (posX, posY))
        for ev in event.get():
            print("Evento ",ev)
            if ev.type == QUIT:
                quit()
                exit()
            #print("1")
            elif ev.type == KEYDOWN:
                print("PRECIONADA")
                if ev.key == K_LEFT:
                    if posX > 1:
                        posX -= speed
                    txtGolpe = False
                elif ev.key == K_RIGHT:
                    if posX < 400:
                        posX += speed
                    txtGolpe = False
                elif ev.key == K_UP:
                    if posY > 1:
                        posY -= speed
                    txtGolpe = False
                elif ev.key == K_DOWN:
                    if posY < 270:
                        posY += speed
                    txtGolpe = False
                elif ev.key == K_RETURN:#para la tecla Enter usar K_RETURN
                    if posX < 400:
                        for i in range (400):
                            print(i)
                            if posX < 400:
                                posX += speed
                            else:
                                txtGolpe = True
                                #screen.blit(texto,(posX,0))
                                break
                elif ev.key == K_SPACE:
                    if posX > 1:
                        for i in range (400):
                            print(i)
                            if posX > 1:
                                posX -= speed
                            else:
                                txtGolpe = True
                                #screen.blit(texto, (posX, 0))
                                break

            elif ev.type == KEYUP:
                print("LIBERA")
                if ev.key == K_LEFT:
                    pass
                elif ev.key == K_RIGHT:
                    pass
                elif ev.key == K_UP:
                    pass
                elif ev.key == K_DOWN:
                    pass
        # if edge == True:
        #     if posX < 400:
        #         posX += speed
        #     else:
        #         edge = False
        # else:
        #     if posX > 1:
        #         posX -= speed
        #     else:
        #         edge = True
        if txtGolpe:
            screen.blit(texto, (posX, 0))
        display.update()


"""
