import pygame

from sprites import *
from config import *

class EnemyBase:
    def __init__(self, coordenada_x, coordenada_y, speed, animation) -> None:
        #self.screen = screen
        # self.stay_r = freezer_quieto_derecha
        # self.stay_l = freezer_quieto_izquierda
        # self.walk_r = freezer_camina_derecha
        # self.walk_l = freezer_camina_izquierda
        
        self.frame = 0
        self.animation = animation
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect(x = coordenada_x, y = coordenada_y)
        # self.rect.x = posicion_inicial[0] # usar el  start_pos_player
        # self.rect.y = posicion_inicial[1]

        self.move_x = 0
        self.move_y = 0
        self.speed = speed
        self.direction = DIRECTION_RIGHT
        
        self.vidas = 1
        
    def update(self):
        if self.frame < len(self.animation) -1:
            self.frame += 1
        else:
            self.frame = 0
    
    def render(self, screen:pygame.Surface):
        if self.vidas == 1:
            if DEBUG:
                pygame.draw.rect(screen, PINK, self.rect)
                
                
            self.image = self.animation[self.frame]
            screen.blit(self.image, self.rect)
    
    def colicion(self, pos_xy):
        if self.rect.colliderect(pos_xy):
            self.vidas == 0


class Freezer(EnemyBase):
    def __init__(self, x, y, speed, minimo_x, maximo_x) -> None:
        self.stay_r = freezer_quieto_derecha
        self.stay_l = freezer_quieto_izquierda
        self.walk_r = freezer_camina_derecha
        self.walk_l = freezer_camina_izquierda
        super().__init__(x, y, speed,self.walk_r)  # creo que esto es lo que le pasa a enemigo base
        
        self.minimo_x = minimo_x
        self.maximo_x = maximo_x
        self.retrocediendo = False
    
    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.x > self.minimo_x:
                self.animation = self.walk_l
                self.move_x = -self.speed
            else:
                self.retrocediendo = False
        else:
            if self.rect.x < self.maximo_x:
                self.animation = self.walk_r
                self.move_x = self.speed
            else:
                self.retrocediendo = True
    
    def mover(self):
        self.rect.x += self.move_x


class Cell(EnemyBase):
    def __init__(self, x, y, speed, minimo_x, maximo_x) -> None:
        self.walk_r = cell_camina_derecha
        self.walk_l = cell_camina_izquierda
        super().__init__(x, y, speed,self.walk_r)  # creo que esto es lo que le pasa a enemigo base
        
        self.minimo_x = minimo_x
        self.maximo_x = maximo_x
        self.retrocediendo = False
    
    def controlar_ruta(self):
        if self.retrocediendo:
            if self.rect.x > self.minimo_x:
                self.animation = self.walk_l
                self.move_x = -self.speed
            else:
                self.retrocediendo = False
        else:
            if self.rect.x < self.maximo_x:
                self.animation = self.walk_r
                self.move_x = self.speed
            else:
                self.retrocediendo = True
    
    def mover(self):
        self.rect.x += self.move_x