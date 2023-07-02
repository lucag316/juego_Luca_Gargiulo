# import pygame,sys

# from config import *
# from button import Button

# pygame.init()
# SCREEN = pygame.display.set_mode((1280, 720))
# pygame.display.set_caption("Menu")

# fondo = pygame.image.load(PATH_IMAGE_BACKGROUND)


# def play():
#     pygame.display.set_caption("Play")
#     while True:
#         PLAY_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill(BLACK)

#         PLAY_TEXT = pygame.font.Font(PATH_FONT_DBZ, 48).render("This is the PLAY screen.", True, WHITE)
#         PLAY_RECT = PLAY_TEXT.get_rect(center = (640, 260))
#         SCREEN.blit(PLAY_TEXT, PLAY_RECT)

#         PLAY_BACK = Button((640, 460), pygame.font.Font(PATH_FONT_DBZ, 48), "back", WHITE, GREEN)
        
#         PLAY_BACK.change_color(PLAY_MOUSE_POS)
#         PLAY_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BACK.check_for_input(PLAY_MOUSE_POS):
#                     main_menu()

#         pygame.display.flip()

# def options():
#     while True:
#         OPTIONS_MOUSE_POS = pygame.mouse.get_pos()

#         SCREEN.fill(BLACK)

#         OPTIONS_TEXT = pygame.font.Font(PATH_FONT_DBZ, 48).render("This is the OPTIONS screen.", True, WHITE)
#         OPTIONS_RECT = OPTIONS_TEXT.get_rect(center = (640, 260))
#         SCREEN.blit(OPTIONS_TEXT, OPTIONS_RECT)

#         OPTIONS_BACK = Button((640, 460), pygame.font.Font(PATH_FONT_DBZ, 48), "back", WHITE, GREEN)

#         OPTIONS_BACK.change_color(OPTIONS_MOUSE_POS)
#         OPTIONS_BACK.update(SCREEN)

#         for event in pygame.event.get():
#             if event.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
#             if event.type == pygame.MOUSEBUTTONDOWN:
#                 if OPTIONS_BACK.check_for_input(OPTIONS_MOUSE_POS):
#                     main_menu()
                    
#         pygame.display.flip()

# def main_menu():
#     while True:
#         SCREEN.blit(fondo, ORIGIN)
        
#         MENU_MOUSE_POS = pygame.mouse.get_pos()
        
#         MENU_TEXT = pygame.font.Font(PATH_FONT_DBZ, 48).render("MENU", True, WHITE)
#         MENU_RECT = MENU_TEXT.get_rect(center = (640, 100))
        
#         PLAY_BUTTON = Button((640, 250), pygame.font.Font(PATH_FONT_DBZ, 48), "Play", WHITE, GREEN)
        
#         OPTIONS_BUTTON = Button((640, 400), pygame.font.Font(PATH_FONT_DBZ, 48), "Options", WHITE, GREEN)
        
#         QUIT_BUTTON = Button((640, 550), pygame.font.Font(PATH_FONT_DBZ, 48), "Quit", WHITE, GREEN)
        
#         SCREEN.blit(MENU_TEXT, MENU_RECT)
        
#         for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
#             button.change_color(MENU_MOUSE_POS)
#             button.update(SCREEN)
        
#         for evento in pygame.event.get():
#             if evento.type == pygame.QUIT:
#                 pygame.quit()
#                 sys.exit()
            
#             if evento.type == pygame.MOUSEBUTTONDOWN:
#                 if PLAY_BUTTON.check_for_input(MENU_MOUSE_POS):
#                     play()
#                 if OPTIONS_BUTTON.check_for_input(MENU_MOUSE_POS):
#                     options()
#                 if QUIT_BUTTON.check_for_input(MENU_MOUSE_POS):
#                     pygame.quit()
#                     sys.exit()
                    
#         pygame.display.flip()

# main_menu()


# # funciona bien pero hacerlo con una clase
