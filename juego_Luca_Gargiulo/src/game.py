import pygame
import sys
import random

from pygame.locals import *
from config import *
from player import Player
from platforms import Platform
from projectile import Projectile
from enemy import *
from trampa import *
from item import *

class Game:
    def __init__(self):
        pygame.init()
        self.reloj = pygame.time.Clock()
        self.music = pygame.mixer.music.load(PATH_BACKGROUND_MUSIC)
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(0.1)
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        pygame.display.set_caption(GAME_TITTLE)
        self.icon = pygame.transform.scale(pygame.image.load(PATH_IMAGE_ICON).convert_alpha(), SIZE_ICON)
        pygame.display.set_icon(self.icon)
        self.background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND_4).convert(), SIZE_SCREEN)
        self.font = pygame.font.Font(PATH_FONT_DBZ, 48)
        self.score = 0
        self.sonido_item = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        self.flag_item = True
        self.flag_sonido_item = True
        self.player = Player(POS_START_PLAYER, SPEED_PLAYER, SPEED_PLAYER * 2, GRAVITY_PLAYER, JUMP_POWER_PLAYER, FRAME_RATE_MS_PLAYER, MOVE_RATE_MS_PLAYER, JUMP_HEIGHT_PLAYER, self.screen)
        self.freezer = Freezer(POS_START_FREEZER, SPEED_FREEZER, 650, 900, self.screen, self.player.rect)
        self.cell = Cell(POS_START_CELL, SPEED_CELL,  250, 900, self.screen, self.player.rect)
        self.trampa_1 = Trampa_horizontal(POS_START_TRAMPA_1, SPEED_TRAMPA_1, 0, 1175, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_2 = Trampa_vertical(POS_START_TRAMPA_2, SPEED_TRAMPA_2, 325, 500, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_3 = Trampa_horizontal(POS_START_TRAMPA_3, SPEED_TRAMPA_3, 0, 200, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_4 = Trampa_vertical(POS_START_TRAMPA_4, SPEED_TRAMPA_4, 0, 250, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_5 = Trampa_vertical(POS_START_TRAMPA_5, SPEED_TRAMPA_5, 425, 625, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_6 = Trampa_vertical(POS_START_TRAMPA_6, SPEED_TRAMPA_6, 425, 625, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_7 = Trampa_vertical(POS_START_TRAMPA_7, SPEED_TRAMPA_7, 0, 125, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_8 = Trampa_vertical(POS_START_TRAMPA_8, SPEED_TRAMPA_8, 0, 125, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.trampa_9 = Trampa_vertical(POS_START_TRAMPA_9, SPEED_TRAMPA_9, 0, 125, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        self.item_1 = Item(POS_ITEM_1, PATH_IMAGE_BALL_1)
        self.item_2 = Item(POS_ITEM_2, PATH_IMAGE_BALL_1)
        self.item_3 = Item(POS_ITEM_3, PATH_IMAGE_BALL_1)
        self.item_4 = Item(POS_ITEM_4, PATH_IMAGE_BALL_1)
        self.item_5 = Item(POS_ITEM_5, PATH_IMAGE_BALL_1)
        self.item_6 = Item(POS_ITEM_6, PATH_IMAGE_BALL_1)
        self.item_7 = Item(POS_ITEM_7, PATH_IMAGE_BALL_1)
        self.piso = Platform(PATH_IMAGE_PLATAFORMA, POS_PISO, SIZE_PISO)
        self.plataforma_1 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_1, SIZE_PLATAFORMA_1)
        self.plataforma_2 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_2, SIZE_PLATAFORMA_2)
        self.plataforma_3 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_3, SIZE_PLATAFORMA_3)
        self.plataforma_4 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_4, SIZE_PLATAFORMA_4)
        self.plataforma_5 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_5, SIZE_PLATAFORMA_5)
        self.plataforma_6 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_6, SIZE_PLATAFORMA_6)
        self.plataforma_7 = Platform(PATH_IMAGE_PLATAFORMA, POS_PLATAFORMA_7, SIZE_PLATAFORMA_7)
        self.plataforma_8 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_8, SIZE_PLATAFORMA_8)
        self.plataforma_9 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_9, SIZE_PLATAFORMA_9)
        self.plataforma_10 = Platform(PATH_IMAGE_PLATAFORMA, POS_PLATAFORMA_10, SIZE_PLATAFORMA_10)
        self.plataforma_11 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_11, SIZE_PLATAFORMA_11)
        self.plataforma_12 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_12, SIZE_PLATAFORMA_12)
        self.plataforma_13 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_13, SIZE_PLATAFORMA_13)
        self.plataforma_14 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_14, SIZE_PLATAFORMA_14)
        self.plataforma_15 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_15, SIZE_PLATAFORMA_15)
        self.lista_trampas = []
        self.lista_plataformas = []
        self.lista_enemigos = []
        self.lista_items = []
        self.lista_enemigos.append(self.freezer)
        self.lista_enemigos.append(self.cell)
        self.lista_items.append(self.item_1)
        self.lista_items.append(self.item_2)
        self.lista_items.append(self.item_3)
        self.lista_items.append(self.item_4)
        self.lista_items.append(self.item_5)
        self.lista_items.append(self.item_6)
        self.lista_items.append(self.item_7)
        self.lista_trampas.append(self.trampa_1)
        self.lista_trampas.append(self.trampa_2)
        self.lista_trampas.append(self.trampa_3)
        self.lista_trampas.append(self.trampa_4)
        self.lista_trampas.append(self.trampa_5)
        self.lista_trampas.append(self.trampa_6)
        self.lista_trampas.append(self.trampa_7)
        self.lista_trampas.append(self.trampa_8)
        self.lista_trampas.append(self.trampa_9)
        self.lista_plataformas.append(self.piso)
        self.lista_plataformas.append(self.plataforma_1)
        self.lista_plataformas.append(self.plataforma_2)
        self.lista_plataformas.append(self.plataforma_3)
        self.lista_plataformas.append(self.plataforma_4)
        self.lista_plataformas.append(self.plataforma_5)
        self.lista_plataformas.append(self.plataforma_6)
        self.lista_plataformas.append(self.plataforma_7)
        self.lista_plataformas.append(self.plataforma_8)
        self.lista_plataformas.append(self.plataforma_9)
        self.lista_plataformas.append(self.plataforma_10)
        self.lista_plataformas.append(self.plataforma_11)
        self.lista_plataformas.append(self.plataforma_12)
        self.lista_plataformas.append(self.plataforma_13)
        self.lista_plataformas.append(self.plataforma_14)
        self.lista_plataformas.append(self.plataforma_15)
        self.run = True
        self.is_running = False
        self.is_playing = False
        self.is_game_over = False

    def game_over(self):
        self.is_playing = False
        self.is_game_over = True

    def show_start_screen(self):
        flag = True
        while flag:
            self.reloj.tick(FPS)
            for evento in pygame.event.get():
                if evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_s:
                        flag = False
                        break  # Salir del bucle for
            self.screen.fill(BLACK)  # Limpiar la pantalla
            texto = self.font.render("Presione S para comenzar", True, WHITE)
            texto_rect = texto.get_rect()
            texto_rect.center = CENTER
            self.screen.blit(texto, texto_rect)
            pygame.display.flip()

    def show_game_over_screen(self):
        fondo_game_over = pygame.surface.Surface(SIZE_SCREEN)
        fondo_game_over.fill(BLACK)
        texto = self.font.render("Game Over", True, (WHITE))
        texto_rect = texto.get_rect()
        texto_rect.center = CENTER
        self.screen.blit(fondo_game_over, ORIGIN)
        self.screen.blit(texto, texto_rect)
        pygame.display.flip()
        pygame.time.delay(5000)

    def restart_game(self):
        pass

    def play(self):
        self.is_running = True
        self.is_playing = True
        self.is_game_over = False

        while self.run:
            self.reloj.tick(FPS)
            keys = pygame.key.get_pressed()
            delta_ms = self.reloj.tick(FPS)
            self.screen.blit(self.background, ORIGIN)

            if len(self.player.lista_proyectiles) > 0:
                for proyectil in self.player.lista_proyectiles:
                    proyectil.render()
                    proyectil.trayectoria()

                    if proyectil.rect.x <= DISPLAY_LEFT or proyectil.rect.x >= DISPLAY_RIGHT:
                        self.player.lista_proyectiles.remove(proyectil)

            for plataforma in self.lista_plataformas:
                plataforma.render(self.screen)

            self.player.imputs(keys, delta_ms)
            self.player.events()
            self.player.update(delta_ms, self.lista_plataformas, self.lista_trampas, self.lista_enemigos, self.lista_items)
            self.player.render(self.screen)

            self.freezer.update_all()
            self.cell.update_all()

            self.trampa_1.update_all()
            self.trampa_2.update_all()
            self.trampa_3.update_all()
            self.trampa_4.update_all()
            self.trampa_5.update_all()
            self.trampa_6.update_all()
            self.trampa_7.update_all()
            self.trampa_8.update_all()
            self.trampa_9.update_all()

            self.item_1.render(self.screen)
            self.item_2.render(self.screen)
            self.item_3.render(self.screen)
            self.item_4.render(self.screen)
            self.item_5.render(self.screen)
            self.item_6.render(self.screen)
            self.item_7.render(self.screen)

            if self.player.lives <= 0:
                self.is_game_over = True
                self.show_game_over_screen()

            pygame.display.flip()

        self.show_start_screen()

    def render(self):
        if self.is_game_over:
            self.show_game_over_screen()
        elif self.is_playing:
            self.screen.blit(self.background, ORIGIN)
            self.play()  # Movido aquí
        else:
            self.show_start_screen()
        pygame.display.flip()

game = Game()
game.render()









# import pygame
# import sys
# import random

# from pygame.locals import *

# from config import *
# from player import Player
# from platforms import Platform
# from projectile import Projectile

# from enemy import *
# from trampa import *
# from item import *

# #from modo import *
# # from sprites import *
# # from manipular_imagenes import *
# #from button import Button
# #from menu import Menu

# class Game:
#     def __init__(self) -> None:
#         pygame.init()
#         self.reloj = pygame.time.Clock()
#         #music = pygame.mixer.Sound(PATH_BACKGROUND_MUSIC)
#         self.music = pygame.mixer.music.load(PATH_BACKGROUND_MUSIC)
#         pygame.mixer.music.play(-1)# -1 es para que termine y empiece siempre
#         pygame.mixer.music.set_volume(0.1)
#         self.screen = pygame.display.set_mode(SIZE_SCREEN)
#         pygame.display.set_caption(GAME_TITTLE)
#         self.icon = pygame.transform.scale(pygame.image.load(PATH_IMAGE_ICON).convert_alpha(), SIZE_ICON)
#         pygame.display.set_icon(self.icon)
#         self.background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND_4).convert(), SIZE_SCREEN)
#         self.font = pygame.font.Font(PATH_FONT_DBZ, 48)
#         self.sonido_item = pygame.mixer.Sound(PATH_PUNCH_SOUND)

#         self.score = 0
#         self.flag_item = True
#         self.flag_sonido_item = True

#         self.player = Player(POS_START_PLAYER, SPEED_PLAYER, SPEED_PLAYER * 2, GRAVITY_PLAYER, JUMP_POWER_PLAYER, FRAME_RATE_MS_PLAYER, MOVE_RATE_MS_PLAYER, JUMP_HEIGHT_PLAYER, self.screen)
#         self.freezer = Freezer(POS_START_FREEZER, SPEED_FREEZER, 650, 900, self.screen, self.player.rect)
#         self.cell = Cell(POS_START_CELL, SPEED_CELL,  250, 900, self.screen, self.player.rect)
        
#         self.lista_trampas = []      
#         self.lista_plataformas = []
#         self.lista_enemigos = []
#         self.lista_items = []

#         self.lista_enemigos.append(self.freezer)
#         self.lista_enemigos.append(self.cell)
        
#         self.is_running = False
#         self.is_playing = False
#         self.is_game_over = False

#     def generar_trampas(self):
#         trampa_1 = Trampa_horizontal(POS_START_TRAMPA_1, SPEED_TRAMPA_1, 0, 1175, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_2 = Trampa_vertical(POS_START_TRAMPA_2, SPEED_TRAMPA_2, 325, 500, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_3 = Trampa_horizontal(POS_START_TRAMPA_3, SPEED_TRAMPA_3, 0, 200, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_4 = Trampa_vertical(POS_START_TRAMPA_4, SPEED_TRAMPA_4, 0, 250, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_5 = Trampa_vertical(POS_START_TRAMPA_5, SPEED_TRAMPA_5, 425, 625, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_6 = Trampa_vertical(POS_START_TRAMPA_6, SPEED_TRAMPA_6, 425, 625, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_7 = Trampa_vertical(POS_START_TRAMPA_7, SPEED_TRAMPA_7, 0, 125, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_8 = Trampa_vertical(POS_START_TRAMPA_8, SPEED_TRAMPA_8, 0, 125, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
#         trampa_9 = Trampa_vertical(POS_START_TRAMPA_9, SPEED_TRAMPA_9, 0, 125, PATH_IMAGE_TRAMPA_VIOLETA, self.screen)
        
#         self.lista_trampas.append(trampa_1)
#         self.lista_trampas.append(trampa_2)
#         self.lista_trampas.append(trampa_3)
#         self.lista_trampas.append(trampa_4)
#         self.lista_trampas.append(trampa_5)
#         self.lista_trampas.append(trampa_6)
#         self.lista_trampas.append(trampa_7)
#         self.lista_trampas.append(trampa_8)
#         self.lista_trampas.append(trampa_9)
        
#         trampa_1.update_all()
#         trampa_2.update_all()
#         trampa_3.update_all()
#         trampa_4.update_all()
#         trampa_5.update_all()
#         trampa_6.update_all()
#         trampa_7.update_all()
#         trampa_8.update_all()
#         trampa_9.update_all()

#     def generar_items(self):
#         item_1 = Item(POS_ITEM_1, PATH_IMAGE_BALL_1)
#         item_2 = Item(POS_ITEM_2, PATH_IMAGE_BALL_1)
#         item_3 = Item(POS_ITEM_3, PATH_IMAGE_BALL_1)
#         item_4 = Item(POS_ITEM_4, PATH_IMAGE_BALL_1)
#         item_5 = Item(POS_ITEM_5, PATH_IMAGE_BALL_1)
#         item_6 = Item(POS_ITEM_6, PATH_IMAGE_BALL_1)
#         item_7 = Item(POS_ITEM_7, PATH_IMAGE_BALL_1)
        
#         self.lista_items.append(item_1)
#         self.lista_items.append(item_2)
#         self.lista_items.append(item_3)
#         self.lista_items.append(item_4)
#         self.lista_items.append(item_5)
#         self.lista_items.append(item_6)
#         self.lista_items.append(item_7)
        
#         item_1.render(self.screen)
#         item_2.render(self.screen)
#         item_3.render(self.screen)
#         item_4.render(self.screen)
#         item_5.render(self.screen)
#         item_6.render(self.screen)
#         item_7.render(self.screen)
    
#     def generar_plataformas(self):
#         piso = Platform(PATH_IMAGE_PLATAFORMA, POS_PISO, SIZE_PISO)
#         plataforma_1 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_1, SIZE_PLATAFORMA_1)   
#         plataforma_2 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_2, SIZE_PLATAFORMA_2)
#         plataforma_3 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_3, SIZE_PLATAFORMA_3)
#         plataforma_4 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_4, SIZE_PLATAFORMA_4)
#         plataforma_5 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_5, SIZE_PLATAFORMA_5)
#         plataforma_6 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_6, SIZE_PLATAFORMA_6)
#         plataforma_7 = Platform(PATH_IMAGE_PLATAFORMA, POS_PLATAFORMA_7, SIZE_PLATAFORMA_7)
#         plataforma_8 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_8, SIZE_PLATAFORMA_8)
#         plataforma_9 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_9, SIZE_PLATAFORMA_9)
#         plataforma_10 = Platform(PATH_IMAGE_PLATAFORMA, POS_PLATAFORMA_10, SIZE_PLATAFORMA_10)
#         plataforma_11 = Platform(PATH_IMAGE_PLATAFORMA_3, POS_PLATAFORMA_11, SIZE_PLATAFORMA_11)
#         plataforma_12 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_12, SIZE_PLATAFORMA_12)
#         plataforma_13 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_13, SIZE_PLATAFORMA_13)
#         plataforma_14 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_14, SIZE_PLATAFORMA_14)
#         plataforma_15 = Platform(PATH_IMAGE_PLATAFORMA_1, POS_PLATAFORMA_15, SIZE_PLATAFORMA_15)
        
#         self.lista_plataformas.append(piso)
#         self.lista_plataformas.append(plataforma_1)
#         self.lista_plataformas.append(plataforma_2)
#         self.lista_plataformas.append(plataforma_3)
#         self.lista_plataformas.append(plataforma_4)
#         self.lista_plataformas.append(plataforma_5)
#         self.lista_plataformas.append(plataforma_6)
#         self.lista_plataformas.append(plataforma_7)
#         self.lista_plataformas.append(plataforma_8)
#         self.lista_plataformas.append(plataforma_9)
#         self.lista_plataformas.append(plataforma_10)
#         self.lista_plataformas.append(plataforma_11)
#         self.lista_plataformas.append(plataforma_12)
#         self.lista_plataformas.append(plataforma_13)
#         self.lista_plataformas.append(plataforma_14)
#         self.lista_plataformas.append(plataforma_15)
    
#     def generar_enemigos(self):
#         self.freezer.update_all()
#         self.cell.update_all()

#     def game_over(self):
#         # self.stop_elements()       # podria ser un boton de pausa
#         self.is_playing = False
#         self.is_game_over = True

#     def show_start_screen(self):
#         flag = True
            
#         while flag:
#             self.reloj.tick(FPS)
#             for evento in pygame.event.get():
#                 if evento.type == pygame.KEYDOWN:
#                     if evento.key == pygame.K_s:
#                         flag = False
            
#             fondo_game_over = pygame.surface.Surface(SIZE_SCREEN)
#             fondo_game_over.fill(BLACK)
#             texto = self.font.render("Presione S para comenzar", True, (WHITE))
#             texto_rect = texto.get_rect()
#             texto_rect.center = CENTER
            
#             self.screen.blit(fondo_game_over, ORIGIN)
#             self.screen.blit(texto, texto_rect)
#             pygame.display.flip()

#         #self.restart_game()

#     def show_game_over_screen(self):
#         fondo_game_over = pygame.surface.Surface(SIZE_SCREEN)
#         fondo_game_over.fill(BLACK)
#         texto = self.font.render("Game Over", True, (WHITE))
#         texto_rect = texto.get_rect()
#         texto_rect.center = CENTER
        
#         self.screen.blit(fondo_game_over, ORIGIN)
#         self.screen.blit(texto, texto_rect)
        
#         pygame.display.flip()       # esta mal, tiene que estar solo en el render. buscar otra solucion
#         pygame.time.delay(5000) # congela la pantalla por 5 segundos
        
#         #self.restart_game()
#         #self.is_game_over = False
#         self.is_running = False

#     def restart_game(self):

#             # self.score = 0
#             # self.sprites.empty()
#             # self.asteroides.empty()
#             # self.lasers.empty()
#             # self.nave.reset()
#             # self.sprites.add(self.nave)
            
#             # self.play()
#         pass

#     def manejar_eventos(self):
#         pass
    
#     def manejar_imputs(self):
#         keys = pygame.key.get_pressed()
#         self.player.imputs(keys, self.delta_ms)

#     def play(self):
#         self.is_running = True
#         self.is_playing = True
#         self.is_game_over = False

#         while self.is_running:
#             self.reloj.tick(FPS)
#             self.delta_ms = self.reloj.tick(FPS)
#             self.manejar_imputs()
#             self.manejar_eventos()
#             self.update()
#             self.render()
            
#             if len(self.player.lista_proyectiles) > 0:
#                 for proyectil in self.player.lista_proyectiles:
#                     proyectil.render()
#                     proyectil.trayectoria()
                    
#                     if proyectil.rect.x <= DISPLAY_LEFT or proyectil.rect.x >= DISPLAY_RIGHT:
#                         self.player.lista_proyectiles.remove(proyectil)

#             for plataforma in self.lista_plataformas:
#                 plataforma.render(self.screen)
            
#             pygame.display.flip()
            
#         self.show_start_screen()

#     def update(self):
#         self.generar_plataformas()
#         self.generar_items()
#         self.generar_enemigos()
#         self.generar_trampas()
        
#         self.player.events()
#         self.player.update(self.delta_ms, self.lista_plataformas, self.lista_trampas, self.lista_enemigos, self.lista_items) # delta_ms el tiempo que habia transcurrido desde la ultima vez de reloj.tick
#         self.player.render(self.screen)
    
#     def render(self):
#         # juego / inicio / game over
#         if self.is_game_over:
#             self.show_game_over_screen()
#         elif self.is_playing:
#             self.screen.blit(self.background, ORIGIN)
#             self.play()
#         else:
#             self.show_start_screen()
        
#         pygame.display.flip()

# juego = Game()
# juego.play()
