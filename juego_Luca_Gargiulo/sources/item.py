# import pygame


# class Item(pygame.sprite.Sprite):
#     def __init__(self, path_imagen: str, size: tuple, center: tuple, speed: int) -> None:
#         super().__init__()
        
#         self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
#         self.rect = self.image.get_rect()
#         self.rect.center = center
#         self.velocidad_y = speed

#     def update(self):
#         self.rect.y += self.velocidad_y 
    
#     def stop(self):
#         self.velocidad_y = 0
    
#     def colition(self):
#         pass
    
    