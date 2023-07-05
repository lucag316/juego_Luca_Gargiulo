import pygame

from config import *
from sprites import *

class Projectile(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, speed: int, posx, posy, direction, screen: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        #self.rect.midbottom = midbotton
        self.rect.y = posy
        self.rect.x = posx
        self.direction = direction
        self.speed = speed
        
    def trayectoria(self):
        if self.direction == "derecha":
            self.rect.x += self.speed
        elif self.direction == "izquierda":
            self.rect.x -= self.speed
    
    def render(self):
        if DEBUG:
            pygame.draw.rect(self.screen, YELLOW, self.rect)
        
        self.screen.blit(self.image, self.rect)
    
    
    





# class Projectile(pygame.sprite.Sprite):
#     def __init__(self, path_imagen: str, size: tuple, speed: int, posx, posy, pantalla: pygame.Surface) -> None:
#         super().__init__()  # nose si aca tiene que ir, creo
        
#         self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
#         self.rect = self.image.get_rect()
#         #self.rect.midbottom = midbotton
        
#         self.speed = speed
        
#         self.rect.top = posy
#         self.rect.left = posx
#         self.pantalla = pantalla
        
#         self.lados = obtener_rectangulos(self.rect)
    
    
    
#     def update(self):
#         self.rect.top += self.speed
#         self.pantalla.blit(self.image, self.rect)
#         self.lados = obtener_rectangulos(self.rect) # me lo dijo chatgpt no se si esta bien, pero funciona(los lados siguen al proyectil)
        
    
#     def stop(self):
#         self.speed_x = 0
