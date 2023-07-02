# import pygame

# class Projectile(pygame.sprite.Sprite):
#     def __init__(self, path_imagen: str, size: tuple, midbotton: tuple, speed: int) -> None:
#         super().__init__()
        
#         self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
#         self.rect = self.image.get_rect()
#         self.rect.midbottom = midbotton
        
#         self.speed_y = speed
    
#     def update(self):
#         self.rect.y -= self.speed_y
    
#     def stop(self):
#         self.speed_y = 0
