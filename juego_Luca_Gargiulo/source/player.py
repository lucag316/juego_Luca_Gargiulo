import pygame

from config import *
from projectile import Projectile
from sprites import *

class Player(pygame.sprite.Sprite):
    def __init__(self, size: tuple, posicion_inicial: tuple, animaciones, velocidad) -> None:
        super().__init__()
        self.indice = 0
        # self.stay_r = quieto_derecha #get_stay_r()
        # self.stay_l = quieto_izquierda #get_stay_l()
        # self.walk_r = camina_derecha #get_walk_r()
        # self.walk_l = camina_izquierda #get_walk_l()
        # self.jump_r = salta_derecha #get_jump_r()
        # self.jump_l = salta_izquierda #get_jump_l()
        
        self.speed_x = velocidad
        #self.speed_y = 0

        self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
        self.playing = True
        
        self.saltando = False
        self.left = True
        self.salto = 0

        self.que_hace = "quieto_derecha"
        self.contador_pasos = 0
        
        self.animaciones = animaciones
        self.image = self.animaciones[self.que_hace][self.contador_pasos]
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2        # ya tengo el start pos player pero por ahora lo hago asi
        self.rect.y = HEIGHT - 50
        self.posicion_actual_x = 0
        
        # self.animations = get_animations()
        
        # self.image = self.animations[self.indice]
        
        # self.rect = self.image.get_rect()
        # self.rect.centerx = WIDTH // 2
        # self.rect.bottom = HEIGHT - 10

        
    # def aplicar_gravedad(self):
    #     # SALTO
    #     # CAIDA
    #     # ALGO MAS
    #     pass

    def mover_personaje(self, speed):
        self.rect.x += speed

    def animar(self, accion, pantalla: pygame.Surface):
        largo = len(accion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        pantalla.blit(accion[self.contador_pasos], self.rect)
        self.contador_pasos += 1

    def update(self, pantalla):
        #movimiento horizontal
        #self.rect.x += self.speed_x
        
        #limites
        
        # poner movimientos y animaciones 
        if self.que_hace == "quieto_derecha":
            self.animar(quieto_derecha, pantalla)
        elif self.que_hace == "quieto_izquierda":
            self.animar(quieto_izquierda, pantalla)
        elif self.que_hace == "camina_derecha":
            self.animar(camina_derecha, pantalla)
            self.mover_personaje(self.speed_x)
        elif self.que_hace == "camina_izquierda":
            self.animar(camina_izquierda, pantalla)
            self.mover_personaje(-self.speed_x)
        elif self.que_hace == "salta_derecha":
            self.animar(salta_derecha, pantalla)
            self.mover_personaje(self.speed_x)
        elif self.que_hace == "salta_izquierda":
            self.animar(salta_izquierda, pantalla)
            self.mover_personaje(-self.speed_x)
        
        if self.rect.left <= DISPLAY_LEFT:
            self.rect.left = DISPLAY_LEFT
        elif self.rect.right >= DISPLAY_RIGHT:
            self.rect.right = DISPLAY_RIGHT
        if self.rect.top <= DISPLAY_TOP:
            self.rect.top = DISPLAY_TOP
        elif self.rect.bottom >= DISPLAY_BOTTOM:
            self.rect.bottom = DISPLAY_BOTTOM
        
        # # saltando
        # if self.salto != 0:
        #     self.rect.y += self.speed_y
        #     self.speed_y += 1
        #     print(self.speed_y)
            
        #     if self.rect.bottom >= HEIGHT - 10:
        #         self.rect.bottom = HEIGHT - 10
        #         self.saltando = False
        #         self.salto = 0
        
        # # izquierda
        # if self.speed_x < 0:    # si el tipo esta yendo a la izquierda
        #     self.left = True        # y ya esta mirando a la izquierda
        #     #salta
        #     if self.saltando:   # si esta saltando
        #         self.indice = 23    # se carga la imagen de salto a la izquierda
        #         self.indice += 1
        #         if self.indice >= 29:
        #             self.indice = 23
        #     #camina
        #     else:
        #         self.indice = 11
        #         self.indice += 1
        #         if self.indice >= 14:
        #             self.indice = 11
        # #derecha
        # elif self.speed_x > 0:
        #     self.left = False
        #     #salta
        #     if self.saltando:
        #         self.indice = 15
        #         self.indice += 1
        #         if self.indice >= 22:
        #             self.indice = 15
        #     #camina
        #     else:
        #         self.indice = 8
        #         self.indice += 1
        #         if self.indice >= 11:
        #             self.indice = 8
        # # esta parado y no salta
        # elif self.speed_x == 0 and not self.saltando:
        #     if self.left:
        #         self.indice = 4
        #         self.indice += 1
        #         if self.indice >= 7:
        #             self.indice = 4
        #     else:
        #         self.indice = 0
        #         self.indice += 1
        #         if self.indice >= 3:
        #             self.indice = 0
        
        # self.image = self.animations[self.indice]
    
    
    def saltar(self):
        if self.salto == 0:
            self.speed_y = - 15
            self.salto = 1
        elif self.salto == 1:
            self.speed_y = - 15
            self.salto = 2
        else:
            self.salto = 0
        
        if not self.saltando:
            self.saltando = True

    def reset(self):
        self.rect.center = START_POS_PLAYER
        self.speed_x = 0
        self.speed_y = 0

    def fire(self, sprites, bombas):
        if self.playing:
            bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
            self.sound_bomb.play()
            sprites.add(bomba)
            bombas.add(bomba)

    def stop(self):
        self.playing = False


    def draw(self, screen):
        pass















    # def staying(self):
    #     if self.animation != self.stay_r and self.animation != self.stay_l:
    #         if self.direction == DIRECTION_RIGHT:
    #             self.animation = self.stay_r
    #         else:
    #             self.animation = self.stay_l
    #         self.move_x = 0
    #         self.move_y = 0
    #         self.frame = 0
    
    # def walking(self, direction):
    #     if self.is_jump == False and self.is_fall == False:
    #         if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
    #             self.frame = 0
    #             self.direction = direction
                
    #         if direction == DIRECTION_RIGHT:
    #             self.move_x = self.speed_walk
    #             self.animation = self.walk_r
    #         else:
    #             self.move_x = -self.speed_walk
    #             self.animation = self.walk_l
    
    # def jumping(self, on_off = True):
    #     if on_off and self.is_jump == False and self.is_fall == False:
    #         self.start_jump_y = self.rect.y
            
    #         if self.direction == DIRECTION_RIGHT:
    #             self.move_x = int(self.move_x / 2)
    #             self.move_y = -self.jump
    #             self.animation = self.jump_r
    #         else:
    #             self.move_x = int(self.move_x / 2)
    #             self.move_y = -self.jump
    #             self.animation = self.jump_l
                
    #         self.frame = 0
    #         self.is_jump = True
    #     if on_off == False:
    #         self.is_jump = False
    #         self.staying()
    
    