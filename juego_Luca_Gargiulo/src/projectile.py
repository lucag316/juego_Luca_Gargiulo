import pygame
import time

from config import *
from sprites import *
FIRE_RATE_INTERVAL = 3
class Projectile(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, speed: int, posx, posy, direction, screen: pygame.Surface) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        self.rect = self.image.get_rect()
        #self.rect.midbottom = midbotton
        self.origen_rect_x = posx
        self.origen_rect_y = posy
        
        self.rect.x = self.origen_rect_x
        self.rect.y = self.origen_rect_y
        
        self.direction = direction
        self.speed = speed
        
        self.activo = True
        #self.last_shot_time = time.time() -FIRE_RATE_INTERVAL
        
    def trayectoria(self):
        if self.activo:
            if self.direction == "derecha":
                self.rect.x += self.speed
                if self.rect.x > self.origen_rect_x + 200:
                    self.activo = False
            elif self.direction == "izquierda":
                self.rect.x -= self.speed
                if self.rect.x < self.origen_rect_x - 200:
                    self.activo = False
            else:
                self.activo = False
    
    def render(self):
        if self.activo:
            if DEBUG:
                pygame.draw.rect(self.screen, YELLOW, self.rect)
            
            self.screen.blit(self.image, self.rect)
    
    
    
    
    
    
    
    # def can_shoot(self):
    #     current_time = time.time()
    #     elapsed_time = current_time - self.last_shot_time
    #     return elapsed_time >= FIRE_RATE_INTERVAL

    # def shoot(self):
    #     if self.can_shoot():
    #         self.last_shot_time = time.time()





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
