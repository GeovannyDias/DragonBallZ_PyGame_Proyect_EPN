import pygame
import juego
               
pygame.init()
 
pantalla = pygame.display.set_mode((600, 300))
pygame.display.set_caption("DRAGON BALL Z")
clock = pygame.time.Clock()
player = juego.Serge((150, 150))
fondo = pygame.image.load("fondo4.jpg")

game_over = False
 
while game_over == False:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    player.handle_event(event)                 
    pantalla.blit(fondo, (0,0)) 
    pantalla.blit(player.image, player.rect) 
    pygame.display.flip()              
    clock.tick(10)
 
pygame.quit ()



#Clear Data

"""
pygame.init()
 
pantalla = pygame.display.set_mode((600, 300))
pygame.display.set_caption("DRAGON BALL Z")
clock = pygame.time.Clock()
player = juego.Serge((150, 150))
fondo = pygame.image.load("fondo4.jpg")

game_over = False
 
while game_over == False:
 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
 
    player.handle_event(event)                 
    pantalla.blit(fondo, (0,0)) 
    pantalla.blit(player.image, player.rect) 
    pygame.display.flip()              
    clock.tick(10)
 
pygame.quit ()

"""
