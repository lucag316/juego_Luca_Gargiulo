import pygame

from config import *

class Item(pygame.sprite.Sprite):
    def __init__(self, posicion: tuple, path_imagen: str) -> None:
        
        self.image = pygame.transform.scale(pygame.image.load(path_imagen), (25, 25))
        self.coordenada_x = posicion[0]
        self.coordenada_y = posicion[1]
        self.rect = self.image.get_rect()
        self.rect.x = posicion[0]
        self.rect.y = posicion[1]
        
        self.move_x = 0
        self.move_y = 0
        self.direction = DIRECTION_RIGHT
        
        self.activo = True
        
    
    def render(self, screen: pygame.Surface):
        if self.activo:
            if DEBUG:
                pygame.draw.rect(screen, WHITE, self.rect)
        
            screen.blit(self.image, self.rect)
    
    def collition(self):
        pass