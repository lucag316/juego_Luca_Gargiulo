import pygame

from config import *
from sprites import *
from projectile import Projectile

class Player:
    def __init__(self, posicion_inicial: tuple, speed_walk: int, speed_run: int, gravity: int, potencia_salto: int, frame_rate_ms: int, move_rate_ms: int, jump_height: int, screen: pygame.Surface, interval_time_jump = 100) -> None:
        self.screen = screen
        
        self.stay_r = player_quieto_derecha
        self.stay_l = player_quieto_izquierda
        self.walk_r = player_camina_derecha
        self.walk_l = player_camina_izquierda
        self.jump_r = player_salta_derecha
        self.jump_l = player_salta_izquierda
        self.atack_r = player_ataque_derecha
        self.atack_l = player_ataque_izquierda
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        
        self.gravity = gravity
        self.potencia_salto = potencia_salto
        
        self.frame = 0
        self.lives = 3
        self.score = 0
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = posicion_inicial[0] # usar el  start_pos_player
        self.rect.y = posicion_inicial[1]
        
        self.direction = DIRECTION_RIGHT
        
        self.is_jumping = False
        self.is_falling = False
        self.is_shooting = False
        
        self.y_start_jump = 0
        self.jump_height = jump_height
        
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms        # nos permite 
        
        self.tiempo_transcurrido = 0 #nose si va
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump
        
        #self.crear_rectangulos()
        self.ground_collition_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.h -10, self.rect.w, 10)   # el rectangulo de los  pies
        
        self.lista_proyectiles = []
        self.sonido_proyectil = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        self.derecha = True
        
    # def crear_rectangulos(self):
    #     self.rect_right = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
    #     self.rect_left = pygame.Rect(self.rect.left, self.rect.top,6, self.rect.height)
    #     self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
    #     self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)
    #     self.lados = [self.rect, self.rect_bottom, self.rect_left, self.rect_right, self.rect_top]
    
    #  def disparar(self,slave):
    #     bala = Disparo(self.rect.x,self.rect.y,slave,r"RECURSOS\bola de fuego.png", self.posicion)
    #     pygame.mixer.Sound(r"RECURSOS\disparo.wav").play()
    #     self.lista_proyectiles.append(bala)
    
    def disparar(self, proyectil):
        proyectil = Projectile(PATH_IMAGE_BOLA_ENERGIA, SIZE_BOLA_ENERGIA, SPEED_PROJECTILE, self.rect.x, self.rect.y, self.direction, self.screen )
        #self.sonido_proyectil.play()
        self.lista_proyectiles.append(proyectil)
    
    def staying(self):
        if self.is_shooting:
            return
        
        if self.animation != self.stay_r or self.animation != self.stay_l:
        
            if self.direction == DIRECTION_RIGHT:
                self.animation = self.stay_r
            else:
                self.animation = self.stay_l
            self.move_x = 0
            self.move_y = 0
            self.frame = 0

    def walking(self, direction):
        if not self.is_jumping and not self.is_falling:
            if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
                self.frame = 0
                self.direction = direction
                
                if direction == DIRECTION_RIGHT:
                    self.move_x = self.speed_walk
                    self.animation = self.walk_r
                else:
                    self.move_x = -self.speed_walk
                    self.animation = self.walk_l
    
    def jumping(self, on_off = True):       # queda mejor jump walk stay
        if on_off and not self.is_jumping and not self.is_falling:
            self.y_start_jump = self.rect.y
            
            if self.direction == DIRECTION_RIGHT:
                self.move_x = self.speed_run    #speed_walk     o int(self.move_x / 2) 
                self.move_y = -self.potencia_salto
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_run   #speed_walk
                self.move_y = -self.potencia_salto
                self.animation = self.jump_l
                
            self.frame = 0
            self.is_jumping = True
        if on_off == False:
            self.is_jumping = False
            self.staying()

    def shooting(self, on_off = True):
        self.is_shooting = on_off
        if on_off == True and not self.is_jumping and not self.is_falling:
            if self.animation != self.atack_r and self.animation != self.atack_l:
                self.frame = 0
                self.is_shooting = True
                if self.direction == DIRECTION_RIGHT:
                    self.animation = self.atack_r
                else:
                    self.animation = self.atack_l  

    def change_x(self, delta_x):
        # mueve todos los rectangulos en x, en esto se alteran las coordenadas de los rectangulos
        self.rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        # for lado in self.lados:
        #     lado.x += delta_x
        # puedo hacer uno del cuerpo
    
    def change_y(self, delta_y):
        # mueve todos los rectangulos en y
        self.rect.y += delta_y
        self.ground_collition_rect.y += delta_y
        # for lado in self.lados:
        #     lado.y += delta_y
    
    def do_movement(self, delta_ms, lista_plataformas):
        self.tiempo_transcurrido_move += delta_ms        # se acumula el tiempo
        
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            # if self.rect.left <= DISPLAY_LEFT:        # funciona mal porque solo el rectangulo principal se queda
            #     self.rect.left = DISPLAY_LEFT
            # elif self.rect.right >= DISPLAY_RIGHT:
            #     self.rect.right = DISPLAY_RIGHT
            # if self.rect.top <= DISPLAY_TOP:
            #     self.rect.top = DISPLAY_TOP
            # elif self.rect.bottom >= DISPLAY_BOTTOM:
            #     self.rect.bottom = DISPLAY_BOTTOM
            
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jumping:    # el abs me da el valor absoluto, le saca el simbolo
                self.move_y = 0
            
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x) # self.rect.x += self.move_x
            self.change_y(self.move_y) # self.rect.y += self.move_y
            
            if not self.is_on_platform(lista_plataformas):
                if self.move_y == 0:
                    self.is_falling = True
                    self.change_y(self.gravity)    #self.rect.y += self.gravity # esto iria adentro del if de arriba
            else: 
                if self.is_jumping: #sacar
                    self.jumping(False)
                self.is_falling = False
    
    def is_on_platform(self, lista_plataformas):
        retorno = False
        if self.rect.y >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if self.ground_collition_rect.colliderect(plataforma.rect_top):
                    retorno = True
                    break
        
        return retorno
    
    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms        # se acumula el tiempo
        
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            
            if self.frame < len(self.animation)-1:
                self.frame += 1
            else:
                self.frame = 0

    def update(self, delta_ms, lista_plataformas):
        self.do_movement(delta_ms, lista_plataformas)
        self.do_animation(delta_ms)
    
    def render(self, screen: pygame.Surface):
        if DEBUG:
            pygame.draw.rect(screen, BLUE, self.rect)
            pygame.draw.rect(screen, GREEN, self.ground_collition_rect)
            
            # for lado in self.lados:
            #     pygame.draw.rect(screen, ORANGE, lado, 2)

        self.image = self.animation[self.frame]
        screen.blit(self.image, self.rect)
    
    def imputs(self, keys, delta_ms):
        self.tiempo_transcurrido += delta_ms
        if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:    # esto puede estar en el player si es multiplayer
            self.walking(DIRECTION_LEFT)
            
        if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
            self.walking(DIRECTION_RIGHT)
            
        if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
            self.staying()
            
        if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
            self.staying()
            
        if keys[pygame.K_UP]:
            if (self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump:
                self.jumping(True)
                self.tiempo_last_jump = self.tiempo_transcurrido
        
        if not keys[pygame.K_SPACE]:    # aca no se si es not o o pero no se muestra de ninguna forma
            self.shooting(False)






# import pygame

# from config import *
# from sprites import *
# from projectile import Projectile
# #from modo import *

# class Player(pygame.sprite.Sprite):
#     def __init__(self, velocidad, pantalla: pygame.Surface, gravedad, potencia_salto) -> None:
#         super().__init__()
#         reescalar_imagenes(lista_animaciones_player, 75, 85)
#         self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
#         self.speed_x = velocidad
#         self.speed_y = velocidad
#         x_inicial = START_POS_PLAYER[0]
#         y_inicial = START_POS_PLAYER[1]
        
#         self.rect = player_quieto_derecha[0].get_rect()
#         self.rect.x = x_inicial
#         self.rect.y = y_inicial
#         #self.crear_rectangulos()
#         self.lados = obtener_rectangulos(self.rect)
        
#         self.que_hace = "quieto_derecha"
#         self.contador_pasos = 0
        
#         self.posicion_actual_x = 0
#         self.pantalla = pantalla
#         self.izquierda = False
        
#         # SALTO
#         self.gravedad = gravedad
#         self.potencia_salto = potencia_salto
#         self.limite_velocidad_caida = 15
#         self.esta_saltando = False
#         self.desplazamiento_y = 0
        
#         self.lista_disparos = []
#         self.vida = True
        
#         self.playing = True
        
    
#     # def crear_rectangulos(self):
#     #     self.rect_right = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
#     #     self.rect_left = pygame.Rect(self.rect.left, self.rect.top,6, self.rect.height)
#     #     self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
#     #     self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)
#     #     self.lados = [self.rect, self.rect_bottom, self.rect_left, self.rect_right, self.rect_top]
    
#     def disparar(self, x, y, proyectil):
#         if self.playing:
#             self.lista_disparos.append(proyectil)
#             # bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
#             # self.sound_bomb.play()
#             # sprites.add(bomba)
#             # bombas.add(bomba)
    
#     def aplicar_gravedad(self, pisos: list, animacion):
#         # salto
#         if self.esta_saltando:
#             self.animar(animacion)
        
#             for lado in self.lados:
#                 self.lados[lado].y += self.desplazamiento_y
            
#             if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
#                 self.desplazamiento_y += self.gravedad
#         # verificacion colision plataformas
#         for plataforma in pisos:
#             if self.lados["bottom"].colliderect(plataforma["top"]):
#                 self.esta_saltando = False
#                 self.desplazamiento_y = 0
#                 self.lados["main"].bottom = plataforma["main"].top + 5 # el +5 hay que hacerlo con todos los lados para que no se desfacen     # no entendi bien, ver explicacion en algun lugar
#                 break
#             #----codear que pasaria si alguna parte el personaje hace colision con una parte de la plataforma
#             else:
#                 self.esta_saltando = True # podemos ponerle, esta cayendo
    
#     def mover_personaje(self, speed_x):
#         if self.vida == True:
#             for lado in self.lados:
#                 self.lados[lado].x += speed_x
    
#     def animar(self, accion):
#         largo = len(accion)
#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0
#         #self.image = accion[self.contador_pasos]
#         self.pantalla.blit(accion[self.contador_pasos], self.lados["main"])
#         self.contador_pasos += 1
    
#     def update(self, pisos):
#         #limites
#         if self.rect.left <= DISPLAY_LEFT:  # modificar por los rectangulos principales(lados)
#             self.rect.left = DISPLAY_LEFT
#         elif self.rect.right >= DISPLAY_RIGHT:
#             self.rect.right = DISPLAY_RIGHT
#         if self.rect.top <= DISPLAY_TOP:
#             self.rect.top = DISPLAY_TOP
#         elif self.rect.bottom >= DISPLAY_BOTTOM:
#             self.rect.bottom = DISPLAY_BOTTOM
        
        
#         if self.que_hace == "camina_izquierda": # AGREGAR UNA BANDERA PARA QUE CU8ANDO SE QUEDE QUIETO MIRE A LA IZQUIERDA SI ESTABA YENDO A LA IZQUIERDA
#             if not self.esta_saltando:
#                 self.animar(player_camina_izquierda)
#             self.mover_personaje(-self.speed_x)
#         elif self.que_hace == "camina_derecha":
#             if not self.esta_saltando:
#                 self.animar(player_camina_derecha)
#             self.mover_personaje(self.speed_x)
#         elif self.que_hace == "quieto_derecha":
#             if not self.esta_saltando:
#                 self.animar(player_quieto_derecha)
#         elif self.que_hace == "quieto_izquierda":
#             if not self.esta_saltando:
#                 self.animar(player_quieto_izquierda)
#         elif self.que_hace == "salta":
#             if not self.esta_saltando:
#                 self.esta_saltando = True
#                 self.desplazamiento_y = self.potencia_salto
#             self.animar(player_salta_derecha)
#         elif self.que_hace == "salta_derecha":
#             self.animar(player_salta_derecha)
#             self.mover_personaje(self.speed_x)
#         elif self.que_hace == "salta_izquierda":
#             self.animar(player_salta_izquierda)
#             self.mover_personaje(-self.speed_x)
        
#         #self.crear_rectangulos()
#         self.aplicar_gravedad(pisos, player_salta_derecha)

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    # def update(self):
        # #movimiento horizontal
        
        # self.rect.x += self.speed_x
        
        # #limites
        # if self.rect.left <= DISPLAY_LEFT:
        #     self.rect.left = DISPLAY_LEFT
        # elif self.rect.right >= DISPLAY_RIGHT:
        #     self.rect.right = DISPLAY_RIGHT
        # if self.rect.top <= DISPLAY_TOP:
        #     self.rect.top = DISPLAY_TOP
        # elif self.rect.bottom >= DISPLAY_BOTTOM:
        #     self.rect.bottom = DISPLAY_BOTTOM
        
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
    







    # def saltar(self):
    #     if self.salto == 0:
    #         self.speed_y = - 15
    #         self.salto = 1
    #     elif self.salto == 1:
    #         self.speed_y = - 15
    #         self.salto = 2
    #     else:
    #         self.salto = 0
        
    #     if not self.saltando:
    #         self.saltando = True

    # def reset(self):
    #     self.rect.center = START_POS_PLAYER
    #     self.speed_x = 0
    #     self.speed_y = 0

    # def fire(self, sprites, bombas):
    #     if self.playing:
    #         bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
    #         self.sound_bomb.play()
    #         sprites.add(bomba)
    #         bombas.add(bomba)

    # def stop(self):
    #     self.playing = False


