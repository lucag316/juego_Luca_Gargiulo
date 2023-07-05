import pygame
import sys
import random
# from pygame.locals import *
from config import *
from modo import *
from player import Player
from platforms import Platform
from projectile import Projectile

from enemy import *
# from sprites import *
# from manipular_imagenes import *
#from button import Button
#from menu import Menu

pygame.init()
reloj = pygame.time.Clock()
#music = pygame.mixer.Sound(PATH_BACKGROUND_MUSIC)
music = pygame.mixer.music.load(PATH_BACKGROUND_MUSIC)
pygame.mixer.music.play(-1)# -1 es para que termine y empiece siempre
pygame.mixer.music.set_volume(0.1)
screen = pygame.display.set_mode(SIZE_SCREEN)
pygame.display.set_caption(GAME_TITTLE)
icon = pygame.transform.scale(pygame.image.load(PATH_IMAGE_ICON).convert_alpha(), SIZE_ICON)
pygame.display.set_icon(icon)
background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND).convert(), SIZE_SCREEN)
font = pygame.font.Font(PATH_FONT_DBZ, 48)


player = Player(START_POS_PLAYER, SPEED_PLAYER, SPEED_PLAYER * 2, GRAVITY_PLAYER, JUMP_POWER_PLAYER, FRAME_RATE_MS_PLAYER, MOVE_RATE_MS_PLAYER, JUMP_HEIGHT_PLAYER, screen)
freezer = Freezer(100, 75, 5, 100, 800)
cell = Cell(200, 225, 5, 200, 1000)

piso = Platform(PATH_IMAGE_PLATAFORMA, 0, 650, (1200, 100))
plataforma = Platform(PATH_IMAGE_PLATAFORMA_1, 100, 450, (100, 25))
plataforma_1 = Platform(PATH_IMAGE_PLATAFORMA_3, 0, 150, (1000, 25))
plataforma_2 = Platform(PATH_IMAGE_PLATAFORMA_1, 1100, 225, (100, 25))
plataforma_3 = Platform(PATH_IMAGE_PLATAFORMA_3, 225, 300, (1000, 25))
plataforma_4 = Platform(PATH_IMAGE_PLATAFORMA_1, 0, 375, (100, 25))
plataforma_5 = Platform(PATH_IMAGE_PLATAFORMA_1, 0, 550, (100, 25))
plataforma_6 = Platform(PATH_IMAGE_PLATAFORMA, 200, 300, (25, 300))
plataforma_7 = Platform(PATH_IMAGE_PLATAFORMA_3, 225, 400, (800, 25))
plataforma_8 = Platform(PATH_IMAGE_PLATAFORMA_1, 1100, 475, (100, 25))
plataforma_9 = Platform(PATH_IMAGE_PLATAFORMA, 1000, 425, (25, 150))
plataforma_10 = Platform(PATH_IMAGE_PLATAFORMA_3, 500, 500, (400, 25))
plataforma_11 = Platform(PATH_IMAGE_PLATAFORMA_1, 1025, 550, (50, 25))
plataforma_12 = Platform(PATH_IMAGE_PLATAFORMA_1, 350, 550, (100, 25))


lista_plataformas = []

lista_plataformas.append(piso)
lista_plataformas.append(plataforma)
lista_plataformas.append(plataforma_1)
lista_plataformas.append(plataforma_2)
lista_plataformas.append(plataforma_3)
lista_plataformas.append(plataforma_4)
lista_plataformas.append(plataforma_5)
lista_plataformas.append(plataforma_6)
lista_plataformas.append(plataforma_7)
lista_plataformas.append(plataforma_8)
lista_plataformas.append(plataforma_9)
lista_plataformas.append(plataforma_10)
lista_plataformas.append(plataforma_11)
lista_plataformas.append(plataforma_12)
#podria hacer lo de la lista de las plataformas afuera, para que quede mas vacio el main

proyectiles = pygame.sprite.Group()

run = True

while run:
    reloj.tick(FPS)
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_f:
                player.disparar(proyectiles)
            
        elif evento.type == pygame.KEYUP:
            if evento.key == pygame.K_f:
                player.disparar(proyectiles)
    
    keys = pygame.key.get_pressed()
    
    delta_ms = reloj.tick(FPS)
    screen.blit(background, ORIGIN)
    
    if len(player.lista_proyectiles) > 0:
        for proyectil in player.lista_proyectiles:
            proyectil.render()
            proyectil.trayectoria()
            
            if proyectil.rect.x <= DISPLAY_LEFT or proyectil.rect.x >= DISPLAY_RIGHT:
                player.lista_proyectiles.remove(proyectil)
            
    # proyectil.trayectoria()
    # proyectil.render(screen)
    
    for plataforma in lista_plataformas:
        plataforma.render(screen)
    
    player.imputs(keys, delta_ms)
    player.update(delta_ms, lista_plataformas) # delta_ms el tiempo que habia transcurrido desde la ultima vez de reloj.tick
    player.render(screen)
    
    freezer.controlar_ruta()
    freezer.update()
    freezer.mover()
    freezer.render(screen)
    freezer.colicion(player.rect)
    
    cell.controlar_ruta()
    cell.update()
    cell.mover()
    cell.render(screen)
    cell.colicion(player.rect)

    pygame.display.flip()











# import pygame
# import sys
# import random

# from config import *
# from modo import *
# from player import Player
# from platforms import Platform
# from projectile import Projectile

# # from enemy import Enemy
# # from sprites import *
# # from manipular_imagenes import *
# #from button import Button
# #from menu import Menu

# pygame.init()
# reloj = pygame.time.Clock()
# #music = pygame.mixer.Sound(PATH_BACKGROUND_MUSIC)
# music = pygame.mixer.music.load(PATH_BACKGROUND_MUSIC)
# pygame.mixer.music.play(-1)# -1 es para que termine y empiece siempre
# #pygame.mixer.music.set_volume(0.5)
# screen = pygame.display.set_mode(SIZE_SCREEN)
# pygame.display.set_caption(GAME_TITTLE)
# icon = pygame.transform.scale(pygame.image.load(PATH_IMAGE_ICON).convert_alpha(), SIZE_ICON)
# pygame.display.set_icon(icon)
# background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND).convert(), SIZE_SCREEN)
# font = pygame.font.Font(PATH_FONT_DBZ, 48)
# score = 0
# izquierda = False

# player = Player(SPEED_PLAYER, screen, 1, -15)

# ground = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_GROUND, 0, 685)
# platform = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA, 0, 600)
# plataforma_1 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_1, 650, 575)
# plataforma_2 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_2, 200, 500)
# plataforma_3 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_3, 0, 200)
# plataforma_4 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_4, 300, 200)
# plataforma_5 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_5, 800, 450)
# plataforma_6 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_6, 1000, 350)
# plataforma_7 = Platform(screen, PATH_IMAGE_PLATAFORMA, SIZE_PLATAFORMA_7, 1150, 300)

# piso = pygame.Rect(0, 0, WIDTH, 10)
# piso.top = player.rect.bottom       # relativo al personaje sino lo pongo a ojo directo

# # plataforma_1 = pygame.transform.scale(pygame.image.load(PATH_IMAGE_PLATAFORMA).convert(), (SIZE_PLATAFORMA_1))
# # rect_plataforma_1 = plataforma_1.get_rect()
# # rect_plataforma_1.x = 500
# # rect_plataforma_1.y = 650
# lista_plataformas = [ground.lados, platform.lados, plataforma_1.lados, plataforma_2.lados, plataforma_3.lados, plataforma_4.lados, plataforma_5.lados, plataforma_6.lados, plataforma_7.lados]


# proyectil = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, SPEED_PROJECTILE, WIDTH/2, HEIGHT/2, screen)

# # grupos de sprties, instanciacion del objeto jugador

# sprites = pygame.sprite.Group()

# # bombas = pygame.sprite.Group()
# sprites.add(player) # aparece el sprite en la pantalla, fijarse la forma mejor con mi propio metodo
# sprites.add(proyectil)

# # sprites.add(ground) 
# # sprites.add(platform) 
# # sprites.add(plataforma_1) 
# # sprites.add(plataforma_2) 
# # sprites.add(plataforma_3) 
# # sprites.add(plataforma_4) 


# def update_screen(plataformas):
#     screen.blit(background, ORIGIN)
#     #screen.blit(plataforma_1, (rect_plataforma_1.x, rect_plataforma_1.y))
#     platform.update()
#     plataforma_1.update()
#     plataforma_2.update()
#     plataforma_3.update()
#     plataforma_4.update()
#     plataforma_5.update()
#     plataforma_6.update()
#     plataforma_7.update()
#     ground.update()
#     player.update(plataformas)
#     if len(player.lista_disparos) > 0:
#         for bala in player.lista_disparos:
#             bala.update()
#         if bala.rect.top < 100:
#             player.lista_disparos.remove(bala)
#         proyectil.update()


# ejecutando = True

# while ejecutando:
#     reloj.tick(FPS)
#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit()
#         elif evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_TAB:
#                 cambiar_modo()
    
#     keys = pygame.key.get_pressed()
        
#     if keys[pygame.K_LEFT]:
#         player.que_hace = "camina_izquierda"
#         izquierda = True

#     elif keys[pygame.K_RIGHT]:
#         player.que_hace = "camina_derecha"
#         izquierda = False

#     # elif keys[pygame.K_UP] and keys[pygame.K_RIGHT]:
#     #     player.que_hace = "salta_derecha"
#     #     izquierda = False

#     # elif keys[pygame.K_UP] and keys[pygame.K_LEFT]:
#     #     player.que_hace = "salta_izquierda"
#     #     izquierda = True
#     elif keys[pygame.K_UP]:
#         player.que_hace = "salta"
#     #     pass # solo que salte
#     else:
#         if izquierda:
#             player.que_hace = "quieto_izquierda"
#         else:
#             player.que_hace = "quieto_derecha"
            
#     if keys[pygame.K_SPACE]:
#         player_pos = player.rect.center
#         player.disparar(player_pos[0], player_pos[1], proyectil)
    
#     update_screen(lista_plataformas)
    
#     # baja el volumen
#     if keys[pygame.K_u] and pygame.mixer.music.get_volume() > 0.0:
#         pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() - 0.01)
#         texto_volumen = font.render("bajando volumen", True, BLACK)
#         screen.blit(texto_volumen, (10, 10))
#         #screen.blit("sonido_abajo", (25, 25))
#     elif keys[pygame.K_u] and pygame.mixer.music.get_volume() == 0.0:
#         texto_volumen = font.render("mute", True, BLACK)
#         screen.blit(texto_volumen, (10, 10))
#     # sube el volumen
#     if keys[pygame.K_i] and pygame.mixer.music.get_volume() < 1.0:
#         pygame.mixer.music.set_volume(pygame.mixer.music.get_volume() + 0.01)
#         texto_volumen = font.render("subiendo volumen", True, BLACK)
#         screen.blit(texto_volumen, (10, 10))
#     elif keys[pygame.K_i] and pygame.mixer.music.get_volume() == 1.0:
#         texto_volumen = font.render("max volumen", True, BLACK)
#         screen.blit(texto_volumen, (10, 10))
#     # text = font.render("Score: " + str(score), True, BLACK)
# #         self.screen.blit(text, (10, 10))
    
            


    
#     if get_mode():
#         pygame.draw.rect(screen, RED, player.rect, 2) # puede estar en un metodo, esta asi porque por ahora solo tengo al personaje
#         #pygame.draw.rect(screen, GREEN, piso, 2)
#         # pygame.draw.rect(screen, GREEN, platform.rect, 2)
#         # pygame.draw.rect(screen, GREEN, ground.rect, 2)
#         for lado in player.lados:
#             pygame.draw.rect(screen, RED, player.lados[lado], 2)
#         for lado in ground.lados:
#             pygame.draw.rect(screen, GREEN, ground.lados[lado], 2)
#         for lado in platform.lados:
#             pygame.draw.rect(screen, GREEN, platform.lados[lado], 2)
#         for lado in plataforma_1.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_1.lados[lado], 2)
#         for lado in plataforma_2.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_2.lados[lado], 2)
#         for lado in plataforma_3.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_3.lados[lado], 2)
#         for lado in plataforma_4.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_4.lados[lado], 2)
#         for lado in plataforma_5.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_5.lados[lado], 2)
#         for lado in plataforma_6.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_6.lados[lado], 2)
#         for lado in plataforma_7.lados:
#             pygame.draw.rect(screen, GREEN, plataforma_7.lados[lado], 2)
        
#         for lado in proyectil.lados:
#             pygame.draw.rect(screen, GREEN, proyectil.lados[lado], 2)
        

#     pygame.display.flip()










# class Game():
#     def __init__(self) -> None:
#         pygame.init()
        
#         self.reloj = pygame.time.Clock()
#         self.music = pygame.mixer.Sound(PATH_BACKGROUND_MUSIC)
#         self.screen = pygame.display.set_mode(SIZE_SCREEN)
#         pygame.display.set_caption(GAME_TITTLE)
#         self.icon = pygame.transform.scale(pygame.image.load(PATH_IMAGE_ICON).convert_alpha(), SIZE_ICON)
#         pygame.display.set_icon(self.icon)
#         self.background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND).convert(), SIZE_SCREEN)
        
#         self.sprites = pygame.sprite.Group()
#         self.bombas = pygame.sprite.Group()
        
        
#         self.player = Player((75, 75), START_POS_PLAYER, SPEED_PLAYER)
#         self.sprites.add(self.player) # aparece el sprite en la pantalla, fijarse la forma mejor con mi propio metodo
        
#         self.is_running = False
#         self.is_playing = False
#         self.is_game_over = False
        
#         self.font = pygame.font.Font(PATH_FONT_DBZ, 48)
        
#         self.score = 0
        

#     def play(self):    # start
#         self.is_running = True
#         self.is_playing = True
#         self.is_game_over = False

#         while self.is_running:
#             self.reloj.tick(FPS)
#             self.handler_events()
#             self.update()
#             self.render()
            
#         self.show_start_screen()
    
#     def handler_events(self):
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 self.salir()
                
#             elif evento.type == pygame.KEYDOWN:
#                 if evento.key == pygame.K_LEFT:
#                     self.player.speed_x = -SPEED_PLAYER
#                 elif evento.key == pygame.K_RIGHT:
#                     self.player.speed_x = SPEED_PLAYER
#                 elif evento.key == pygame.K_UP:
#                     self.player.saltar()
#                 elif evento.key == pygame.K_DOWN:
#                     self.player.speed_y = SPEED_PLAYER
#                 elif evento.key == pygame.K_SPACE:
#                     self.player.fire(self.sprites, self.bombas)
#                 # elif evento.key == pygame.K_ESCAPE:
#                 #     self.terminar_partida()     # podria poner self.jugando = False, pero es mejor asi con el metodo
#                 # elif evento.key == pygame.K_TAB:
#                 #     cambiar_modo()
                
#             elif evento.type == pygame.KEYUP:
#                 if evento.key == pygame.K_LEFT and self.player.speed_x < 0:
#                     self.player.speed_x = 0
#                 elif evento.key == pygame.K_RIGHT and self.player.speed_x > 0:
#                     self.player.speed_x = 0
#                 elif evento.key == pygame.K_UP and self.player.speed_y < 0:
#                     self.player.speed_y = 0
#                 elif evento.key == pygame.K_DOWN and self.player.speed_y > 0:
#                     self.player.speed_y = 0
            

    
#     def display_score(self):
#         text = self.font.render("Score: " + str(self.score), True, BLACK)
#         self.screen.blit(text, (10, 10))
    
#     def kill_elements_out_screen(self):
        
#         for bomba in self.bombas:
#             if bomba.rect.bottom <= DISPLAY_TOP:
#                 bomba.kill()
    
#     def game_over(self):
#         self.is_playing = False
#         self.is_game_over = True
    
#     def exit(self):
#         self.is_running = False
    
#     def show_game_over_screen(self):
#         game_over_background = pygame.surface.Surface(SIZE_SCREEN)
#         game_over_background.fill(BLACK)
        
#         text = self.font.render("Game over", True, (WHITE))
#         text_rect = text.get_rect()
#         text_rect.center = CENTER
        
#         self.screen.blit(game_over_background, ORIGIN)
#         self.screen.blit(text, text_rect)
        
#         pygame.display.flip()
#         pygame.time.delay(3500)
        
#         self.is_running = False
    
#     def show_start_screen(self):
#         flag = True
        
#         while flag:
#             self.reloj.tick(FPS)
#             for event in pygame.event.get():
#                 if event.type == pygame.KEYDOWN:
#                     if event.key == pygame.K_s:
#                         flag = False
#             #self.music.play()
#             start_background = pygame.surface.Surface(SIZE_SCREEN)
#             start_background.fill(BLACK)
#             text = self.font.render("Presione 'S' para comenzar", True, WHITE)
#             text_rect = text.get_rect()
#             text_rect.center = CENTER
            
#             self.screen.blit(start_background, ORIGIN)
#             self.screen.blit(text, text_rect)
#             pygame.display.flip()

#         self.restart_game()
    
#     def restart_game(self):
#         self.score = 0
#         self.sprites.empty()
#         self.bombas.empty()
#         self.player.reset()
#         self.sprites.add(self.player)
        
#         self.play()
    
#     def salir(self):    # cerrar la ventana
#         pygame.quit()
#         sys.exit()


#     def update(self):
        
#         self.kill_elements_out_screen()

#         self.handler_events()
#         self.sprites.update()
    
#     def render(self):
#         if DEBUG:
#             for sprite in self.sprites:
#                 pygame.draw.rect(self.screen, RED, sprite.rect)
#         if self.is_game_over:
#             self.show_game_over_screen()
#         elif self.is_playing:
#             self.screen.blit(self.background, ORIGIN)
#             self.sprites.draw(self.screen)
#             self.display_score()
#         else:
#             self.show_start_screen()            #self.menu.main_menu()      
        
#         pygame.display.flip()
        
        
        
        