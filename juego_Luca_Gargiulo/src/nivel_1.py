import pygame

from config import *
from nivel import Nivel

class NivelUno(Nivel):
    def __init__(self) -> None:
        
        self.background = pygame.transform.scale(pygame.image.load(PATH_IMAGE_BACKGROUND_4).convert(), SIZE_SCREEN)
        super().__init__()
    
    