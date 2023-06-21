import pygame, sys

from config import *


pygame.init()
reloj = pygame.time.Clock()
musica_fondo = pygame.mixer.Sound(PATH_MUSICA_FONDO)

screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption("Dragon Ball Z")

icono = pygame.image.load("./juego_Luca_Gargiulo/assets/images/icon.png").convert_alpha()
icono = pygame.transform.scale(icono, SIZE_ICON)

pygame.display.set_icon(icono)

fondo = pygame.image.load("./juego_Luca_Gargiulo/assets/images/fondo1.png").convert()
fondo = pygame.transform.scale(fondo, SIZE_SCREEN)

# sonido_fondo = pygame.mixer.Sound("")
# pygame.mixer.music.load("")


while True:
    
    reloj.tick(FPS)
    
    for evento in pygame.event.get():    
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            
    musica_fondo.play()
    screen.blit(fondo, ORIGIN)
    
    pygame.display.flip()
