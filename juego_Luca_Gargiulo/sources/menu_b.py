# import pygame,sys

# from config import *
# #from game import Game
# from button import Button

# class Menu():
#     def __init__(self, screen: pygame.surface.Surface, background, game) -> None:
#         pygame.init()
#         self.screen = screen
#         self.background = background
#         self.background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND).convert(), SIZE_SCREEN)
#         self.game = game
    
    
    
    
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
    
    
#     def play(self):
#         pygame.display.set_caption("Play")
#         while True:
#             PLAY_MOUSE_POS = pygame.mouse.get_pos()

#             self.screen.fill(BLACK)

#             PLAY_TEXT = pygame.font.Font(PATH_FONT_DBZ, 48).render("This is the PLAY screen.", True, WHITE)
#             PLAY_RECT = PLAY_TEXT.get_rect(center = (640, 260))
#             self.screen.blit(PLAY_TEXT, PLAY_RECT)

#             PLAY_BACK = Button((640, 460), pygame.font.Font(PATH_FONT_DBZ, 48), "back", WHITE, GREEN)
            
#             PLAY_BACK.change_color(PLAY_MOUSE_POS)
#             PLAY_BACK.update(self.screen)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if PLAY_BACK.check_for_input(PLAY_MOUSE_POS):
#                         self.main_menu()

#             pygame.display.flip()
    
#     def options(self):
#         while True:
#             OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#             self.screen.fill(BLACK)

#             OPTIONS_TEXT = pygame.font.Font(PATH_FONT_DBZ, 48).render("This is the OPTIONS screen.", True, WHITE)
#             OPTIONS_RECT = OPTIONS_TEXT.get_rect(center = (640, 260))
#             self.screen.blit(OPTIONS_TEXT, OPTIONS_RECT)

#             OPTIONS_BACK = Button((640, 460), pygame.font.Font(PATH_FONT_DBZ, 48), "back", WHITE, GREEN)

#             OPTIONS_BACK.change_color(OPTIONS_MOUSE_POS)
#             OPTIONS_BACK.update(self.screen)

#             for event in pygame.event.get():
#                 if event.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
#                 if event.type == pygame.MOUSEBUTTONDOWN:
#                     if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
#                         self.main_menu()
                        
#             pygame.display.flip()
    
#     def main_menu(self):
#         while True:
#             self.screen.blit(self.background, ORIGIN)
            
#             MENU_MOUSE_POS = pygame.mouse.get_pos()
            
#             MENU_TEXT = pygame.font.Font(PATH_FONT_DBZ, 48).render("MENU", True, WHITE)
#             MENU_RECT = MENU_TEXT.get_rect(center = (640, 100))
            
#             PLAY_BUTTON = Button((640, 250), pygame.font.Font(PATH_FONT_DBZ, 48), "Play", WHITE, GREEN)
            
#             OPTIONS_BUTTON = Button((640, 400), pygame.font.Font(PATH_FONT_DBZ, 48), "Options", WHITE, GREEN)
            
#             QUIT_BUTTON = Button((640, 550), pygame.font.Font(PATH_FONT_DBZ, 48), "Quit", WHITE, GREEN)
            
#             self.screen.blit(MENU_TEXT, MENU_RECT)
            
#             for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
#                 button.change_color(MENU_MOUSE_POS)
#                 button.update(self.screen)
            
#             for evento in pygame.event.get():
#                 if evento.type == pygame.QUIT:
#                     pygame.quit()
#                     sys.exit()
                
#                 if evento.type == pygame.MOUSEBUTTONDOWN:
#                     if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
#                         self.game.play()         # poner el play del juego, si lo cambio a como queda mejor
#                     if OPTIONS_BUTTON.check_for_input(MENU_MOUSE_POS):
#                         self.options()
#                     if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
#                         pygame.quit()
#                         sys.exit()
                        
#             pygame.display.flip()

# game = Game()
# menu = Menu(pygame.display.set_mode(SIZE_SCREEN), PATH_IMAGE_BACKGROUND, game)

# menu.main_menu()




# # funciona bien este 
