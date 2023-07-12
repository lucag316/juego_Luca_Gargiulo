import pygame
import sys
import time
from config import *
from sprites import *
from projectile import Projectile

class Player(pygame.sprite.Sprite):
    def __init__(self, posicion_inicial: tuple, speed_walk: int, speed_run: int, gravity: int, potencia_salto: int, frame_rate_ms: int, move_rate_ms: int, jump_height: int, screen: pygame.Surface, interval_time_jump = 100) -> None:
        super().__init__()
        self.screen = screen
        
        self.stay_r = player_quieto_derecha
        self.stay_l = player_quieto_izquierda
        self.walk_r = player_camina_derecha
        self.walk_l = player_camina_izquierda
        self.jump_r = player_salta_derecha
        self.jump_l = player_salta_izquierda
        self.atack_r = player_ataque_derecha
        self.atack_l = player_ataque_izquierda
        self.hit_r = player_golpeado_derecha
        self.hit_l = player_golpeado_izquierda
        
        self.posicion_inicial_x = posicion_inicial[0]
        self.posicion_inicial_y = posicion_inicial[1]
        
        self.move_x = 0
        self.move_y = 0
        self.speed_walk = speed_walk
        self.speed_run = speed_run
        self.speed_y = 0
        
        self.frame = 0
        
        self.lives = 3
        self.score = 0
        self.score_viejo = 0
        self.corazon = pygame.transform.scale( pygame.image.load(PATH_IMAGE_CORAZON).convert_alpha(), (25, 25))
        
        self.animation = self.stay_r
        self.image = self.animation[self.frame]
        self.rect = self.image.get_rect()
        self.rect.x = self.posicion_inicial_x # usar el  start_pos_player
        self.rect.y = self.posicion_inicial_y
        self.crear_rectangulos()
        self.direction = DIRECTION_RIGHT
        
        self.is_jumping = False
        self.is_falling = False
        self.is_shooting = False
        
        self.gravity = gravity
        self.potencia_salto = potencia_salto
        self.limite_velocidad_caida = 15
        
        self.y_start_jump = 0
        self.jump_height = jump_height
        
        self.tiempo_transcurrido = 0 #nose si va
        self.tiempo_last_jump = 0
        self.interval_time_jump = interval_time_jump
        
        self.tiempo_transcurrido_animation = 0
        self.tiempo_transcurrido_move = 0
        self.frame_rate_ms = frame_rate_ms
        self.move_rate_ms = move_rate_ms        # nos permite 
        
        #self.crear_rectangulos()
        self.ground_collition_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.h -10, self.rect.w, 10)   # el rectangulo de los  pies
        
        self.lista_proyectiles = []
        self.sonido_proyectil = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        self.derecha = True
        
        #self.fall_count = 0
        self.hit = False
        self.hit_count = 0
        
        self.retrazo_disparo = 1000
        self.ultimo_disparo = pygame.time.get_ticks()
        
        self.last_shot = 0
        
        self.gano = False
        self.esta_vivo = True
        
        
        

    def make_hit(self):
            self.hit = True
            self.hit_count = 0
# self.loop() #en do movement
    
#     def loop(self):
#         if self.hit:
#             self.hit_count += 1
#         if self.hit_count > FPS *2:
#             self.hit = False
#             self.hit_count = 0
#     # def loop(self, fps):
#     #     self.move_y += min((10, self.fall_count / fps) * self.gravity)
#     #     self.fall_count += 1
    
#     # def landed(self):
#     #     self.fall_count = 0
#     #     self.move_y = 0
    
#     # def hit_head(self):
#     #     self.count = 0
#     #     self.move_y *= -1
# self.morir()
#                 self.make_hit()
#                 self.hitting()

    def crear_rectangulos(self):
        self.rect_right = pygame.Rect(self.rect.right -10, self.rect.top, 10, self.rect.height)
        self.rect_left = pygame.Rect(self.rect.left, self.rect.top,10, self.rect.height)
        self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 10)
        self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -10, self.rect.width, 10)
        self.lados = [self.rect, self.rect_bottom, self.rect_left, self.rect_right, self.rect_top]
    
    def change_x(self, delta_x):
        # mueve todos los rectangulos en x, en esto se alteran las coordenadas de los rectangulos
        self.rect.x += delta_x
        self.ground_collition_rect.x += delta_x
        self.rect_right.x += delta_x
        self.rect_left.x += delta_x
        self.rect_top.x += delta_x
        self.rect_bottom.x += delta_x
        # for lado in self.lados:
        #     lado.x += delta_x
        # puedo hacer uno del cuerpo
    
    def change_y(self, desplazamiento_y):
        # mueve todos los rectangulos en y
        self.rect.y += desplazamiento_y
        self.ground_collition_rect.y += desplazamiento_y
        self.rect_right.y += desplazamiento_y
        self.rect_left.y += desplazamiento_y
        self.rect_top.y += desplazamiento_y
        self.rect_bottom.y += desplazamiento_y
        # for lado in self.lados:
        #     lado.y += delta_y
    
    def disparar(self):
        current_time = time.time()
        elapsed_time = current_time - self.last_shot
        if elapsed_time >= 3:
            proyectil = Projectile(PATH_IMAGE_BOLA_ENERGIA, SIZE_BOLA_ENERGIA, SPEED_PROJECTILE, self.rect.x, self.rect.y, self.direction, self.screen )
            #self.sonido_proyectil.play()
            self.lista_proyectiles.append(proyectil)
            self.last_shot = current_time
            #proyectiles.add(proyectil)
    
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
                self.move_x = self.speed_walk    #speed_walk     o int(self.move_x / 2) 
                self.move_y = -self.potencia_salto
                self.animation = self.jump_r
            else:
                self.move_x = -self.speed_walk   #speed_walk
                self.move_y = -self.potencia_salto
                self.animation = self.jump_l
                
            self.frame = 0
            self.is_jumping = True
        if on_off == False:
            self.is_jumping = False
            self.staying()
        ##----------------------------
        # if on_off and not self.is_jumping and not self.is_falling:
        #     self.y_start_jump = self.rect.y
        #     self.move_y = -self.gravity * 2
        #     self.animation = self.jump_r
        #     self.is_jumping = True
        # if on_off == False:
        #     self.is_jumping = False
        #     self.staying()

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

    def hitting(self):
        if self.hit:
            if self.animation != self.hit_r or self.animation != self.hit_l:
                self.frame = 0
                if self.direction == DIRECTION_RIGHT:
                    self.animation = self.hit_r
                else:
                    self.animation = self.hit_l
                self.frame = 0

    def is_on_platform(self, lista_plataformas):
        retorno = False
        if self.rect.y >= GROUND_LEVEL:
            retorno = True
        else:
            for plataforma in lista_plataformas:
                if self.rect_bottom.colliderect(plataforma.rect_top):
                    #self.rect_bottom = plataforma.rect_top #probe pero no hace nada
                    retorno = True
                    break
        
        return retorno
    
    def aplicar_gravedad(self):
        #salto
        #caida
        #algo mas
        pass
    
    def morir(self):
        self.rect.x = self.posicion_inicial_x
        self.rect.y = self.posicion_inicial_y
        self.crear_rectangulos()
        self.direction = DIRECTION_RIGHT

    def collition(self, lista_plataformas, lista_trampas, lista_enemigos, lista_items):

        for plataforma in lista_plataformas:
            if self.rect_top.colliderect(plataforma.rect_bottom):
                #self.rect_top.y = plataforma.rect_bottom.y
                self.move_y = 0
                #self.change_y(self.move_y) # no se si es lo mismo hacer  esto, funciona igual creo
            if self.rect_left.colliderect(plataforma.rect_right):
                self.move_x = 0
            elif self.rect_right.colliderect(plataforma.rect_left):
                self.move_x = 0
        
        for enemigo in lista_enemigos:
            for proyectil in self.lista_proyectiles:
                if enemigo.lives > 0 and proyectil.rect.colliderect(enemigo.rect):
                    enemigo.lives -= 1 
                    self.score += 3
            if self.rect_left.colliderect(enemigo.rect_right) or self.rect_right.colliderect(enemigo.rect_left):
                self.lives -= 3
                #self.make_hit()
                #print("morir")
        
        for trampa in lista_trampas:
            if trampa.activo and self.rect.colliderect(trampa.rect):
                self.morir()
                self.make_hit()
                self.hitting()
                self.lives -= 1
                #print("sacar una vida")

        for item in lista_items:
            if item.activo and self.rect.colliderect(item.rect):
                pygame.mixer.Sound(PATH_PUNCH_SOUND).play()
                item.activo = False
                self.score += 1
                #print("sumar 1 punto")

    def do_movement(self, delta_ms, lista_plataformas, lista_trampas, lista_enemigos, lista_items):
        self.tiempo_transcurrido_move += delta_ms        # se acumula el tiempo
        
        if self.tiempo_transcurrido_move >= self.move_rate_ms:
            if self.rect.left <= DISPLAY_LEFT:        # funciona mal porque solo el rectangulo principal se queda
                self.move_x = self.speed_walk 
            elif self.rect.right >= DISPLAY_RIGHT:
                self.move_x = -self.speed_walk
            if self.rect.top <= DISPLAY_TOP:
                self.move_y = self.speed_walk
            elif self.rect.bottom >= DISPLAY_BOTTOM:
                self.move_y = -self.speed_walk
            
            if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jumping:    # el abs me da el valor absoluto, le saca el simbolo
                self.move_y = 0
            
            self.tiempo_transcurrido_move = 0
            self.change_x(self.move_x) # self.rect.x += self.move_x
            self.change_y(self.move_y) # self.rect.y += self.move_y
            
            self.collition(lista_plataformas, lista_trampas, lista_enemigos, lista_items)
            #self.loop(fps)

            
            if not self.is_on_platform(lista_plataformas):
                if self.move_y == 0:
                    self.is_falling = True
                    self.change_y(self.gravity)    #self.rect.y += self.gravity # esto iria adentro del if de arriba
            else: 
                if self.is_jumping: #sacar
                    self.jumping(False)
                self.is_falling = False

    def do_animation(self, delta_ms):
        self.tiempo_transcurrido_animation += delta_ms        # se acumula el tiempo
        
        if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
            self.tiempo_transcurrido_animation = 0
            
            if self.frame < len(self.animation)-1:
                self.frame += 1
            else:
                self.frame = 0

    def mostrar_vidas(self):
        if self.lives >= 1:
            self.screen.blit(self.corazon, (0, 0))
        if self.lives >= 2:
            self.screen.blit(self.corazon, (50, 0))
        if self.lives >= 3:
            self.screen.blit(self.corazon, (100, 0))

    # def ganar(self, lista_items):
    #     flag = True
    #     for item in lista_items:
    #         if item.activo:
    #             flag = False
    #     if flag:
    #         self.gano = True
    
    # def verificar_muerte(self):
    #     if self.lives <= 0:
    #         self.esta_vivo = False
    #         self.is_game_over = True
    
    # def actualizar_puntos(self):
    #     pass


    def update(self, delta_ms, lista_plataformas, lista_trampas, lista_enemigos, lista_items):
        if self.esta_vivo:
            self.do_movement(delta_ms, lista_plataformas, lista_trampas, lista_enemigos, lista_items)
            self.do_animation(delta_ms)
            #self.verificar_muerte()
            #self.ganar(lista_items)
            self.mostrar_vidas()
    
    def render(self, screen: pygame.Surface):
        if self.esta_vivo:
            if DEBUG:
                pygame.draw.rect(screen, BLUE, self.rect)
                pygame.draw.rect(screen, RED, self.rect_right, 2)
                pygame.draw.rect(screen, RED, self.rect_left, 2)
                pygame.draw.rect(screen, RED, self.rect_top, 2)
                pygame.draw.rect(screen, RED, self.rect_bottom, 2)

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
    
    def events(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_SPACE:
                    self.disparar()
                
            elif evento.type == pygame.KEYUP:
                if evento.key == pygame.K_SPACE:
                    self.disparar()








# from config import *
# from sprites import *
# from projectile import Projectile

# class Player:
#     def __init__(self, posicion_inicial: tuple, speed_walk: int, speed_run: int, gravity: int, potencia_salto: int, frame_rate_ms: int, move_rate_ms: int, jump_height: int, screen: pygame.Surface, interval_time_jump = 100) -> None:
#         self.screen = screen
        
#         self.stay_r = player_quieto_derecha
#         self.stay_l = player_quieto_izquierda
#         self.walk_r = player_camina_derecha
#         self.walk_l = player_camina_izquierda
#         self.jump_r = player_salta_derecha
#         self.jump_l = player_salta_izquierda
#         self.atack_r = player_ataque_derecha
#         self.atack_l = player_ataque_izquierda
        
#         self.move_x = 0
#         self.move_y = 0
#         self.speed_walk = speed_walk
#         self.speed_run = speed_run
        
#         self.gravity = gravity
#         self.potencia_salto = potencia_salto
        
#         self.frame = 0
#         self.lives = 3
#         self.score = 0
        
#         self.animation = self.stay_r
#         self.image = self.animation[self.frame]
#         self.rect = self.image.get_rect()
#         self.rect.x = posicion_inicial[0] # usar el  start_pos_player
#         self.rect.y = posicion_inicial[1]
#         self.crear_rectangulos()
#         self.direction = DIRECTION_RIGHT
        
#         self.is_jumping = False
#         self.is_falling = False
#         self.is_shooting = False
        
#         self.y_start_jump = 0
#         self.jump_height = jump_height
        
#         self.tiempo_transcurrido_animation = 0
#         self.tiempo_transcurrido_move = 0
#         self.frame_rate_ms = frame_rate_ms
#         self.move_rate_ms = move_rate_ms        # nos permite 
        
#         self.tiempo_transcurrido = 0 #nose si va
#         self.tiempo_last_jump = 0
#         self.interval_time_jump = interval_time_jump
        
#         #self.crear_rectangulos()
#         self.ground_collition_rect = pygame.Rect(self.rect.x, self.rect.y + self.rect.h -10, self.rect.w, 10)   # el rectangulo de los  pies
        
#         self.lista_proyectiles = []
#         self.sonido_proyectil = pygame.mixer.Sound(PATH_PUNCH_SOUND)
#         self.derecha = True
        
#     def crear_rectangulos(self):
#         self.rect_right = pygame.Rect(self.rect.right -6, self.rect.top, 6, self.rect.height)
#         self.rect_left = pygame.Rect(self.rect.left, self.rect.top,6, self.rect.height)
#         self.rect_top = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 6)
#         self.rect_bottom = pygame.Rect(self.rect.left, self.rect.bottom -6, self.rect.width, 6)
#         self.lados = [self.rect, self.rect_bottom, self.rect_left, self.rect_right, self.rect_top]
    
#     #  def disparar(self,slave):
#     #     bala = Disparo(self.rect.x,self.rect.y,slave,r"RECURSOS\bola de fuego.png", self.posicion)
#     #     pygame.mixer.Sound(r"RECURSOS\disparo.wav").play()
#     #     self.lista_proyectiles.append(bala)
    
#     def disparar(self, proyectil):
#         proyectil = Projectile(PATH_IMAGE_BOLA_ENERGIA, SIZE_BOLA_ENERGIA, SPEED_PROJECTILE, self.rect.x, self.rect.y, self.direction, self.screen )
#         #self.sonido_proyectil.play()
#         self.lista_proyectiles.append(proyectil)
    
#     def staying(self):
#         if self.is_shooting:
#             return
        
#         if self.animation != self.stay_r or self.animation != self.stay_l:
        
#             if self.direction == DIRECTION_RIGHT:
#                 self.animation = self.stay_r
#             else:
#                 self.animation = self.stay_l
#             self.move_x = 0
#             self.move_y = 0
#             self.frame = 0

#     def walking(self, direction):
#         if not self.is_jumping and not self.is_falling:
#             if self.direction != direction or (self.animation != self.walk_r and self.animation != self.walk_l):
#                 self.frame = 0
#                 self.direction = direction
                
#                 if direction == DIRECTION_RIGHT:
#                     self.move_x = self.speed_walk
#                     self.animation = self.walk_r
#                 else:
#                     self.move_x = -self.speed_walk
#                     self.animation = self.walk_l
    
#     def jumping(self, on_off = True):       # queda mejor jump walk stay
#         if on_off and not self.is_jumping and not self.is_falling:
#             self.y_start_jump = self.rect.y
            
#             if self.direction == DIRECTION_RIGHT:
#                 self.move_x = self.speed_walk    #speed_walk     o int(self.move_x / 2) 
#                 self.move_y = -self.potencia_salto
#                 self.animation = self.jump_r
#             else:
#                 self.move_x = -self.speed_walk   #speed_walk
#                 self.move_y = -self.potencia_salto
#                 self.animation = self.jump_l
                
#             self.frame = 0
#             self.is_jumping = True
#         if on_off == False:
#             self.is_jumping = False
#             self.staying()

#     def shooting(self, on_off = True):
#         self.is_shooting = on_off
#         if on_off == True and not self.is_jumping and not self.is_falling:
#             if self.animation != self.atack_r and self.animation != self.atack_l:
#                 self.frame = 0
#                 self.is_shooting = True
#                 if self.direction == DIRECTION_RIGHT:
#                     self.animation = self.atack_r
#                 else:
#                     self.animation = self.atack_l  

#     def change_x(self, delta_x):
#         # mueve todos los rectangulos en x, en esto se alteran las coordenadas de los rectangulos
#         self.rect.x += delta_x
#         self.ground_collition_rect.x += delta_x
#         self.rect_right.x += delta_x
#         self.rect_left.x += delta_x
#         self.rect_top.x += delta_x
#         self.rect_bottom.x += delta_x
#         # for lado in self.lados:
#         #     lado.x += delta_x
#         # puedo hacer uno del cuerpo
    
#     def change_y(self, delta_y):
#         # mueve todos los rectangulos en y
#         self.rect.y += delta_y
#         self.ground_collition_rect.y += delta_y
#         self.rect_right.y += delta_y
#         self.rect_left.y += delta_y
#         self.rect_top.y += delta_y
#         self.rect_bottom.y += delta_y
#         # for lado in self.lados:
#         #     lado.y += delta_y
    
#     def do_movement(self, delta_ms, lista_plataformas):
#         self.tiempo_transcurrido_move += delta_ms        # se acumula el tiempo
        
#         if self.tiempo_transcurrido_move >= self.move_rate_ms:
#             # if self.rect.left <= DISPLAY_LEFT:        # funciona mal porque solo el rectangulo principal se queda
#             #     self.rect.left = DISPLAY_LEFT
#             # elif self.rect.right >= DISPLAY_RIGHT:
#             #     self.rect.right = DISPLAY_RIGHT
#             # if self.rect.top <= DISPLAY_TOP:
#             #     self.rect.top = DISPLAY_TOP
#             # elif self.rect.bottom >= DISPLAY_BOTTOM:
#             #     self.rect.bottom = DISPLAY_BOTTOM
            
#             if abs(self.y_start_jump) - abs(self.rect.y) > self.jump_height and self.is_jumping:    # el abs me da el valor absoluto, le saca el simbolo
#                 self.move_y = 0
            
#             self.tiempo_transcurrido_move = 0
#             self.change_x(self.move_x) # self.rect.x += self.move_x
#             self.change_y(self.move_y) # self.rect.y += self.move_y
            
#             if not self.is_on_platform(lista_plataformas):
#                 if self.move_y == 0:
#                     self.is_falling = True
#                     self.change_y(self.gravity)    #self.rect.y += self.gravity # esto iria adentro del if de arriba
#             else: 
#                 if self.is_jumping: #sacar
#                     self.jumping(False)
#                 self.is_falling = False
    
#     def is_on_platform(self, lista_plataformas):
#         retorno = False
#         if self.rect.y >= GROUND_LEVEL:
#             retorno = True
#         else:
#             for plataforma in lista_plataformas:
#                 if self.rect_bottom.colliderect(plataforma.rect_top):
#                     #self.rect_bottom = plataforma.rect_top #probe pero no hace nada
#                     retorno = True
#                     break
        
#         return retorno
    
#     def do_animation(self, delta_ms):
#         self.tiempo_transcurrido_animation += delta_ms        # se acumula el tiempo
        
#         if self.tiempo_transcurrido_animation >= self.frame_rate_ms:
#             self.tiempo_transcurrido_animation = 0
            
#             if self.frame < len(self.animation)-1:
#                 self.frame += 1
#             else:
#                 self.frame = 0

#     def collition(self):
#         pass

#     def update(self, delta_ms, lista_plataformas):
#         self.do_movement(delta_ms, lista_plataformas)
#         self.do_animation(delta_ms)
    
#     def render(self, screen: pygame.Surface):
#         if DEBUG:
#             pygame.draw.rect(screen, BLUE, self.rect)
#             #pygame.draw.rect(screen, GREEN, self.ground_collition_rect)
#             pygame.draw.rect(screen, RED, self.rect_right, 2)
#             pygame.draw.rect(screen, RED, self.rect_left, 2)
#             pygame.draw.rect(screen, RED, self.rect_top, 2)
#             pygame.draw.rect(screen, RED, self.rect_bottom, 2)
            
#             # for lado in self.lados:
#             #     pygame.draw.rect(screen, ORANGE, lado, 2)

#         self.image = self.animation[self.frame]
#         screen.blit(self.image, self.rect)
    
#     def imputs(self, keys, delta_ms):
#         self.tiempo_transcurrido += delta_ms
#         if keys[pygame.K_LEFT] and not keys[pygame.K_RIGHT]:    # esto puede estar en el player si es multiplayer
#             self.walking(DIRECTION_LEFT)
            
#         if keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT]:
#             self.walking(DIRECTION_RIGHT)
            
#         if not keys[pygame.K_RIGHT] and not keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
#             self.staying()
            
#         if keys[pygame.K_RIGHT] and keys[pygame.K_LEFT] and not keys[pygame.K_UP]:
#             self.staying()
            
#         if keys[pygame.K_UP]:
#             if (self.tiempo_transcurrido - self.tiempo_last_jump) > self.interval_time_jump:
#                 self.jumping(True)
#                 self.tiempo_last_jump = self.tiempo_transcurrido
        
#         if not keys[pygame.K_SPACE]:    # aca no se si es not o o pero no se muestra de ninguna forma
#             self.shooting(False)



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


