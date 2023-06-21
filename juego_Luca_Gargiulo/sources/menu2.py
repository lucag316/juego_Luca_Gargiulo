import pygame, sys

from config import *
from button import Button
from game import Game

class Menu():
    def __init__(self) -> None:
        pygame.init()
        self.screen = pygame.display.set_mode(SIZE_SCREEN)
        pygame.display.set_caption("Menu")
        self.background = pygame.transform.scale(pygame.image.load(PATH_IMAGEN_FONDO).convert(), SIZE_SCREEN)
        self.menu_font = pygame.font.Font(PATH_FONT_DBZ, 48)
        self.menu_mouse_pos = pygame.mouse.get_pos()
        self.is_running = False
    
    def run(self):
        self.is_running = True
        self.show_menu()
        
        pygame.display.set_caption("Play")
        while self.is_running:
            self.handle_menu_events()


    def show_menu(self):
        while self.is_running:
            self.screen.blit(self.background, (0, 0))
            
            menu_text = self.menu_font.render("MENU_TEXT", True, (255, 255, 255))
            menu_rect = menu_text.get_rect(center=(WIDTH/2, HEIGHT/2))
            self.screen.blit(menu_text, menu_rect.topleft)
            self.render_menu()
            
            pygame.display.flip()

    def render_menu(self):
        menu_text = self.menu_font.render("Menu", True, WHITE)
        menu_rect = menu_text.get_rect(center = (640, 100))
        
        play_button = Button((640, 250), self.menu_font, "Play", WHITE, GREEN)
        options_button = Button((640, 400), self.menu_font, "Options", WHITE, GREEN)
        quit_button = Button((640, 550), self.menu_font, "Quit", WHITE, GREEN)
        
        self.screen.blit(menu_text, menu_rect)
        
        for button in [play_button, options_button, quit_button]:
            button.change_color(self.menu_mouse_pos)
            button.update(self.screen)
    
    def handle_menu_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if Button((640, 250), self.menu_font, "Play", WHITE, GREEN).check_for_input(self.menu_mouse_pos):
                    self.is_running = False
                    game = Game()
                    game.play()
                if Button((640, 460), self.menu_font, "Options", WHITE, GREEN).check_for_input(self.menu_mouse_pos):
                    return  # Regresar al menú principal
    
    def exit(self):
        pygame.quit()
        sys.exit()
    
    # def options(self):
    #     self.options_mouse_pos = None

    #     while True:
    #         self.options_mouse_pos = pygame.mouse.get_pos()
    #         self.screen.blit(self.background, ORIGIN)
    #         self.render_options()
    #         self.handle_options_events()
    #         pygame.display.flip()

    # def render_options(self):
    #     options_text = self.menu_font.render("This is the OPTIONS screen.", True, WHITE)
    #     options_rect = options_text.get_rect(center=(640, 260))

    #     options_back = Button((640, 460), self.menu_font, "back", WHITE, GREEN)

    #     self.screen.blit(options_text, options_rect)
    #     options_back.change_color(self.options_mouse_pos)
    #     options_back.update(self.screen)

    # def handle_options_events(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             pygame.quit()
    #             sys.exit()

    #         if event.type == pygame.MOUSEBUTTONDOWN:
    #             if Button((640, 460), self.menu_font).check_for_input(self.options_mouse_pos):
    #                 return  # Regresar al menú principal



menu = Menu()
menu.run()

