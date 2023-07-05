import pygame

from config import *
from sprites import *



# class Platform:
#     def __init__(self, pantalla: pygame.Surface, imagen, size, x, y) -> None:
#         self.imagen = pygame.transform.scale(pygame.image.load(imagen), size)
#         self.rect = self.imagen.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.pantalla = pantalla
#         self.lados = obtener_rectangulos(self.rect)
#         # self.rect_right = pygame.Rect(self.rect.right -2, self.rect.top, 2, self.rect.height)
#         # self.rect_left = pygame.Rect(self.rect.left, self.rect.top,2, self.rect.height)
#         # self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 10)
#         # self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -10, self.rect.width, 10)
#         # self.lados = [self.rect,self.rect_bottom,self.rect_left,self.rect_right,self.rect_top]

#     def update(self):
#         self.pantalla.blit(self.imagen, self.rect)




class Platform:
    def __init__(self, path_imagen, x, y, size) -> None:
        self.image = pygame.transform.scale(pygame.image.load(path_imagen), size)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        #self.rect_ground_collition = pygame.Rect(self.rect.x, self.rect.y, self.rect.w, 10)
        
        self.rect_right = pygame.Rect(self.rect.right -2, self.rect.top, 2, self.rect.height)
        self.rect_left = pygame.Rect(self.rect.left, self.rect.top,2, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 10)
        self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -10, self.rect.width, 10)
        self.lados = [self.rect,self.rect_bottom,self.rect_left,self.rect_right,self.rect_top]

    def render(self, screen: pygame.Surface):     # poner en todas render o en todas draw
        
        if DEBUG:
            pygame.draw.rect(screen, RED, self.rect)
            pygame.draw.rect(screen, YELLOW, self.rect_top)
            
            #pygame.draw.rect(screen, GREEN, self.rect_ground_collition)
            # for lado in self.lados:
            #     pygame.draw.rect(screen, ORANGE, lado, 2)

        screen.blit(self.image, self.rect)






# class plataforma():
#     def __init__(self,pantalla, imagen,size, x,y) -> None:
#         self.imagen = pygame.image.load(imagen)
#         self.imagen = pygame.transform.scale(self.imagen, size)
#         self.rect = self.imagen.get_rect()
#         self.rect.x = x
#         self.rect.y = y
#         self.pantalla = pantalla
#         self.rect_right = pygame.Rect(self.rect.right -2, self.rect.top, 2, self.rect.height)
#         self.rect_left = pygame.Rect(self.rect.left, self.rect.top,2, self.rect.height)
#         self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 10)
#         self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -10, self.rect.width, 10)
#         self.rectangulos = [self.rect,self.rect_bottom,self.rect_left,self.rect_right,self.rect_top]

#     def update(self,slave):
#         slave.blit(self.imagen, self.rect)
