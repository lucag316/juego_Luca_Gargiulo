import pygame

from config import *
from bomba import Bomba

class Player(pygame.sprite.Sprite):
    def __init__(self, path_imagen: str, size: tuple, center: tuple) -> None:
        super().__init__()
        
        self.image = pygame.transform.scale(pygame.image.load(path_imagen).convert_alpha(), size)
        
        self.rect = self.image.get_rect()
        self.rect.center = center
        
        self.speed_x = 0    
        self.speed_y = 0
        
        self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
        self.playing = True
    
    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        
        if self.rect.left <= DISPLAY_LEFT:
            self.rect.left = DISPLAY_LEFT
        elif self.rect.right >= DISPLAY_RIGHT:
            self.rect.right = DISPLAY_RIGHT
        if self.rect.top <= DISPLAY_TOP:
            self.rect.top = DISPLAY_TOP
        elif self.rect.bottom >= DISPLAY_BOTTOM:
            self.rect.bottom = DISPLAY_BOTTOM
    
    def reset(self):
        self.rect.center = START_POS_GOKU
        self.speed_x = 0
        self.speed_y = 0
    
    def fire(self, sprites, bombas):
        if self.playing:
            bomba = Bomba(PATH_IMAGEN_BOMBA, SIZE_BOMBA, self.rect.midtop, SPEED_BOMBA)
            self.sound_bomb.play()
            sprites.add(bomba)
            bombas.add(bomba)
    
    def stop(self):
        self.playing = False
    
