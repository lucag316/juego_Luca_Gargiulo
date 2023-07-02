import pygame
import sys
import random

from config import *
from player import Player
from enemy import Enemy
from projectile import Projectile


reloj = pygame.time.Clock()
music = pygame.mixer.Sound(PATH_BACKGROUND_MUSIC)
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption(GAME_TITTLE)
icon = pygame.transform.scale(pygame.image.load(PATH_IMAGE_ICON).convert_alpha(), SIZE_ICON)
pygame.display.set_icon(icon)
background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND).convert(), SIZE_SCREEN)
sprites = pygame.sprite.Group()
bombas = pygame.sprite.Group()

player = Player(PATH_IMAGE_PLAYER, SIZE_PLAYER, START_POS_PLAYER)
sprites.add(player) # aparece el sprite en la pantalla, fijarse la forma mejor con mi propio metodo

is_running = False
is_playing = False
is_game_over = False

font = pygame.font.Font(PATH_FONT_DBZ, 48)

score = 0


while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # elif evento.type == pygame.KEYDOWN:
        #     if evento.key == pygame.K_LEFT:
        #         player.speed_x = -SPEED_PLAYER
        #     elif evento.key == pygame.K_RIGHT:
        #         player.speed_x = SPEED_PLAYER
        #     elif evento.key == pygame.K_UP:
        #         player.saltar()
        #     elif evento.key == pygame.K_DOWN:
        #         player.speed_y = SPEED_PLAYER
        #     elif evento.key == pygame.K_SPACE:
        #         player.fire(sprites,bombas)
        #     # elif evento.key == pygame.K_ESCAPE:
        #     #     self.terminar_partida()     # podria poner self.jugando = False, pero es mejor asi con el metodo
            
        # elif evento.type == pygame.KEYUP:
        #     if evento.key == pygame.K_LEFT and player.speed_x < 0:
        #         player.speed_x = 0
        #     elif evento.key == pygame.K_RIGHT and player.speed_x > 0:
        #         player.speed_x = 0
        #     elif evento.key == pygame.K_UP and player.speed_y < 0:
        #         player.speed_y = 0
        #     elif evento.key == pygame.K_DOWN and player.speed_y > 0:
        #         player.speed_y = 0
    keys = pygame.key.get_pressed
    
    player.manejar_eventos()
    player.update()
    player.draw()
    
    
    
    
    
    
    pygame.display.flip()