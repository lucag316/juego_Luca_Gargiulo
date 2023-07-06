import pygame

from config import *

class TrampaBase(pygame.sprite.Sprite):
    def __init__(self, posicion_inicial: tuple, speed: int, path_imagen: pygame.Surface) -> None:
        
        self.coordenada_x = posicion_inicial[0]
        self.coordenada_y = posicion_inicial[1]
        self.speed = speed
        self.image = path_imagen
        self.rect = self.image.get_rect(x = posicion_inicial[0], y = posicion_inicial[1]) # lo de adentro del parentesis me puso bien la ubicacion
        
        self.move_x = 0
        self.move_y = 0
        self.direction = DIRECTION_RIGHT
        
    
    def render(self, screen: pygame.Surface):
        if DEBUG:
            pygame.draw.rect(screen, BLACK, self.rect)
        
        screen.blit(self.image, self.rect)
    
    def collition(self):
        pass

class Trampa_horizontal(TrampaBase):
    def __init__(self, posicion_inicial: tuple, speed: int, minimo_x: int, maximo_x: int, path_imagen: pygame.Surface) -> None:
        self.image = pygame.transform.scale(pygame.image.load(path_imagen), (25, 25))
        super().__init__(posicion_inicial, speed, self.image)

        self.minimo_x = minimo_x
        self.maximo_x = maximo_x
        self.retrocediendo = False
    
    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.x > self.minimo_x:
                self.move_x = -self.speed
            else:
                self.retrocediendo = False
        else:
            if self.rect.x < self.maximo_x:
                self.move_x = self.speed
            else:
                self.retrocediendo = True
    
    def mover(self):
        self.rect.x += self.move_x

class Trampa_vertical(TrampaBase):
    def __init__(self, posicion_inicial: tuple, speed: int, minimo_y: int, maximo_y: int, path_imagen: pygame.Surface) -> None:
        self.image = pygame.transform.scale(pygame.image.load(path_imagen), (25, 25))
        super().__init__(posicion_inicial, speed, self.image)

        self.minimo_y = minimo_y
        self.maximo_y = maximo_y
        self.retrocediendo = False
    
    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.y > self.minimo_y:
                self.move_y = -self.speed
            else:
                self.retrocediendo = False
        else:
            if self.rect.y < self.maximo_y:
                self.move_y = self.speed
            else:
                self.retrocediendo = True
    
    def mover(self):
        self.rect.y += self.move_y
