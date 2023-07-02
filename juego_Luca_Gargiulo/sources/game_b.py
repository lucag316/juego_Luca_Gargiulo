# import pygame
# import sys
# import random

# from config import *
# from player import Player
# from enemy import Enemy
# from projectile import Projectile

# from button import Button
# from menu import Menu
# from sprites import *

# def actualizar_pantalla(pantalla, un_personaje: Player, fondo):
#     pantalla.blit(fondo, (ORIGIN))
#     # plataformas
#     un_personaje.update_german(pantalla)
    



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
#         self.balls = pygame.sprite.Group()
        
#         self.player = Player(SIZE_PLAYER, diccionario_animaciones, START_POS_PLAYER)
#         self.sprites.add(self.player) # aparece el sprite en la pantalla, fijarse la forma mejor con mi propio metodo
        
#         self.is_running = False
#         self.is_playing = False
#         self.is_game_over = False
#         self.font = pygame.font.Font(PATH_FONT_DBZ, 48)
#         self.score = 0
#         #self.flag_score = False
#         self.menu = Menu(self.screen, self.background)
    
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
#                     #self.player.speed_y = -SPEED_PLAYER
#                     self.player.saltar()
#                 elif evento.key == pygame.K_DOWN:
#                     self.player.speed_y = SPEED_PLAYER
#                 elif evento.key == pygame.K_SPACE:
#                     self.player.fire(self.sprites, self.bombas)
#                 # elif evento.key == pygame.K_ESCAPE:
#                 #     self.terminar_partida()     # podria poner self.jugando = False, pero es mejor asi con el metodo
                
#             elif evento.type == pygame.KEYUP:
#                 if evento.key == pygame.K_LEFT and self.player.speed_x < 0:
#                     self.player.speed_x = 0
#                 elif evento.key == pygame.K_RIGHT and self.player.speed_x > 0:
#                     self.player.speed_x = 0
#                 elif evento.key == pygame.K_UP and self.player.speed_y < 0:
#                     self.player.speed_y = 0
#                 elif evento.key == pygame.K_DOWN and self.player.speed_y > 0:
#                     self.player.speed_y = 0
    
#     def update(self):
#         self.kill_elements_out_screen()
        
#         self.collide_detection()
        
#         self.generate_balls()
        
#         self.sprites.update()
        
#         self.render()
#         #actualizar_pantalla(self.screen, self.player, self.background)
    
#     def render(self):
#         if self.is_game_over:
#             self.show_game_over_screen()
#         elif self.is_playing:
#             self.screen.blit(self.background, ORIGIN)
#             self.sprites.draw(self.screen)
#             self.display_score()
#         else:
#             self.show_start_screen()            #self.menu.main_menu()      
        
#         pygame.display.flip()

#     def generate_balls(self):
#         if len(self.balls) == 0:            # probar si for i range(MAX BALLS) es lo mismo
#             for i in range(MAX_BALLS):
#                 x = random.randrange(25, WIDTH - 25)
#                 y = random.randrange(-1000, HEIGHT - HEIGHT)
#                 ball = Enemy(PATH_IMAGE_BALL_1, SIZE_BALL, (x, y), SPEED_BALL) 
#                 self.balls.add(ball)
#                 self.sprites.add(ball)

#     def stop_elemets(self):
#         for sprite in self.sprites:
#             sprite.stop()
    
#     def collide_detection(self):
#         for bomba in self.bombas:
#             ball_hit_list = pygame.sprite.spritecollide(bomba, self.balls, True)        # ballas que fuero golpeadas balls_hit_list
#             if len(ball_hit_list) != 0:
#                 self.score += 1         # el score aca me anduvo bien
#                 print(self.score)
#                 bomba.kill()
        
#         lista = pygame.sprite.spritecollide(self.player, self.balls, False)
#         if len(lista) != 0:
#             self.game_over()

#     def display_score(self):
#         text = self.font.render("Score: " + str(self.score), True, BLACK)
#         self.screen.blit(text, (10, 10))
    
#     def kill_elements_out_screen(self):
#         for ball in self.balls:
#             if ball.rect.top >= DISPLAY_BOTTOM:
#                 ball.kill()
        
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
#         self.balls.empty()
#         self.bombas.empty()
#         self.player.reset()
#         self.sprites.add(self.player)
        
#         self.play()
    
#     def salir(self):    # cerrar la ventana
#         pygame.quit()
#         sys.exit()


# game = Game()
# game.play()






