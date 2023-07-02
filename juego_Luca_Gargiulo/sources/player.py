# import pygame

# from config import *
# from projectile import Projectile
# from sprites import *
# from manipular_imagenes import Manipular_imagenes


# pygame.init()

# quieto_derecha = [pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_4.png").convert_alpha(), (75, 75))]

# quieto_izquierda = Manipular_imagenes.girar_imagenes(quieto_derecha, True, False)

# camina_derecha = [pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_4.png").convert_alpha(), (75, 75))]

# camina_izquierda = Manipular_imagenes.girar_imagenes(camina_derecha, True, False)

# salta_derecha = [pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_5.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_6.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_7.png").convert_alpha(), (75, 75))]

# salta_izquierda = Manipular_imagenes.girar_imagenes(salta_derecha, True, False)

# lista_animaciones_player = [quieto_derecha, quieto_izquierda, camina_derecha, camina_izquierda, salta_derecha, salta_izquierda]

# class Player(pygame.sprite.Sprite):
#     def __init__(self, size: tuple, posicion_inicial: tuple, pantalla: pygame.Surface, animaciones) -> None:
#         super().__init__()
#         self.rect = quieto_derecha[0].get_rect()
#         self.rect.x = WIDTH // 2        # ya tengo el start pos player pero por ahora lo hago asi
#         self.rect.y = HEIGHT - 50
#         self.posicion_actual_x = 0
#         self.pantalla = pantalla
#         self.speed_x = 0    
#         self.speed_y = 0
        
#         self.que_hace = "quieto"
#         self.contador_pasos = 0
        
#         self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
#         self.playing = True
        
#         self.saltando = False
#         self.left = True
#         self.salto = 0
        
#     # def aplicar_gravedad(self):
#     #     # SALTO
#     #     # CAIDA
#     #     # ALGO MAS
#     #     pass

#     def mover_personaje(self):
#         self.rect += self.speed_x

#     def animar_personaje(self, accion):
#         largo = len(accion)
#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0
#         self.pantalla.blit(accion[self.contador_pasos], self.rect)
#         self.contador_pasos += 1


#     def actualizar_pantalla(self):
#         if self.que_hace == "quieto_derecha":
#             self.animar_personaje(lista_animaciones_player[0])
#         elif self.que_hace == "quieto_izquierda":
#             self.animar_personaje(lista_animaciones_player[1])
#         elif self.que_hace == "camina_derecha":
#             self.animar_personaje(lista_animaciones_player[2])
#             self.mover_personaje()
#         elif self.que_hace == "camina_izquierda":
#             self.animar_personaje(lista_animaciones_player[4])
#             self.mover_personaje()
            
#     def manejar_eventos(self):      # actualizar pantalla
#         keys = pygame.key.get_pressed()
        
#         if keys[pygame.K_RIGHT]:
#             self.que_hace = "camina_derecha"
#         elif keys[pygame.K_LEFT]:
#             self.que_hace = "camina_izquierda"
#         else:
#             self.que_hace = "quieto_derecha"

#     def update(self):
#         #movimiento horizontal
#         self.rect.x += self.speed_x
        
#         #limites
#         if self.rect.left <= DISPLAY_LEFT:
#             self.rect.left = DISPLAY_LEFT
#         elif self.rect.right >= DISPLAY_RIGHT:
#             self.rect.right = DISPLAY_RIGHT
#         if self.rect.top <= DISPLAY_TOP:
#             self.rect.top = DISPLAY_TOP
#         elif self.rect.bottom >= DISPLAY_BOTTOM:
#             self.rect.bottom = DISPLAY_BOTTOM
#     #     #saltando
#     #     if self.salto != 0:
#     #         self.rect.y += self.speed_y
#     #         self.speed_y += 1
#     #         print(self.speed_y)
            
#     #         if self.rect.bottom >= HEIGHT - 10:
#     #             self.rect.bottom = HEIGHT - 10
#     #             self.saltando = False
#     #             self.salto = 0
        
#     #     # izquierda
#     #     if self.speed_x < 0:    # si el tipo esta yendo a la izquierda
#     #         self.left = True        # y ya esta mirando a la izquierda
#     #         #salta
#     #         if self.saltando:   # si esta saltando
#     #             self.indice = 23    # se carga la imagen de salto a la izquierda
#     #             self.indice += 1
#     #             if self.indice >= 29:
#     #                 self.indice = 23
#     #         #camina
#     #         else:
#     #             self.indice = 11
#     #             self.indice += 1
#     #             if self.indice >= 14:
#     #                 self.indice = 11
#     #     #derecha
#     #     elif self.speed_x > 0:
#     #         self.left = False
#     #         #salta
#     #         if self.saltando:
#     #             self.indice = 15
#     #             self.indice += 1
#     #             if self.indice >= 22:
#     #                 self.indice = 15
#     #         #camina
#     #         else:
#     #             self.indice = 8
#     #             self.indice += 1
#     #             if self.indice >= 11:
#     #                 self.indice = 8
#     #     # esta parado y no salta
#     #     elif self.speed_x == 0 and not self.saltando:
#     #         if self.left:
#     #             self.indice = 4
#     #             self.indice += 1
#     #             if self.indice >= 7:
#     #                 self.indice = 4
#     #         else:
#     #             self.indice = 0
#     #             self.indice += 1
#     #             if self.indice >= 3:
#     #                 self.indice = 0
        
#     #     self.image = self.animations[self.indice]

#     # def saltar(self):
#     #     if self.salto == 0:
#     #         self.speed_y = - 15
#     #         self.salto = 1
#     #     elif self.salto == 1:
#     #         self.speed_y = - 15
#     #         self.salto = 2
#     #     else:
#     #         self.salto = 0
        
#     #     if not self.saltando:
#     #         self.saltando = True

#     def reset(self):
#         self.rect.center = START_POS_PLAYER
#         self.speed_x = 0
#         self.speed_y = 0

#     def fire(self, sprites, bombas):
#         if self.playing:
#             bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
#             self.sound_bomb.play()
#             sprites.add(bomba)
#             bombas.add(bomba)

#     def stop(self):
#         self.playing = False
























# import pygame

# from config import *
# from projectile import Projectile
# from sprites import *

# class Player(pygame.sprite.Sprite):
#     def __init__(self, size: tuple, animaciones, posicion_inicial: tuple) -> None:
#         super().__init__()
#         self.indice = 0
#         # self.stay_r = get_stay_r()
#         # self.stay_l = get_stay_l()
#         # self.walk_r = get_walk_r()
#         # self.walk_l = get_walk_l()
#         # self.jump_r = get_jump_r()
#         # self.jump_l = get_jump_l()
#         self.animations = get_animations()
        
#         self.image = self.animations[self.indice]
        
#         self.rect = self.image.get_rect()
#         self.rect.centerx = WIDTH // 2
#         self.rect.bottom = HEIGHT - 10
        
#         self.speed_x = 0    
#         self.speed_y = 0
        
#         self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
#         self.playing = True
        
#         self.saltando = False
#         self.left = True
#         self.salto = 0
        
#     # def aplicar_gravedad(self):
#     #     # SALTO
#     #     # CAIDA
#     #     # ALGO MAS
#     #     pass

#     def update(self):
#         #movimiento horizontal
#         self.rect.x += self.speed_x
        
#         #limites
#         if self.rect.left <= DISPLAY_LEFT:
#             self.rect.left = DISPLAY_LEFT
#         elif self.rect.right >= DISPLAY_RIGHT:
#             self.rect.right = DISPLAY_RIGHT
#         if self.rect.top <= DISPLAY_TOP:
#             self.rect.top = DISPLAY_TOP
#         elif self.rect.bottom >= DISPLAY_BOTTOM:
#             self.rect.bottom = DISPLAY_BOTTOM

#         #saltando
#         if self.salto != 0:
#             self.rect.y += self.speed_y
#             self.speed_y += 1
#             print(self.speed_y)
            
#             if self.rect.bottom >= HEIGHT - 10:
#                 self.rect.bottom = HEIGHT - 10
#                 self.saltando = False
#                 self.salto = 0
        
#         # izquierda
#         if self.speed_x < 0:    # si el tipo esta yendo a la izquierda
#             self.left = True        # y ya esta mirando a la izquierda
#             #salta
#             if self.saltando:   # si esta saltando
#                 self.indice = 23    # se carga la imagen de salto a la izquierda
#                 self.indice += 1
#                 if self.indice >= 29:
#                     self.indice = 23
#             #camina
#             else:
#                 self.indice = 11
#                 self.indice += 1
#                 if self.indice >= 14:
#                     self.indice = 11
#         #derecha
#         elif self.speed_x > 0:
#             self.left = False
#             #salta
#             if self.saltando:
#                 self.indice = 15
#                 self.indice += 1
#                 if self.indice >= 22:
#                     self.indice = 15
#             #camina
#             else:
#                 self.indice = 8
#                 self.indice += 1
#                 if self.indice >= 11:
#                     self.indice = 8
#         # esta parado y no salta
#         elif self.speed_x == 0 and not self.saltando:
#             if self.left:
#                 self.indice = 4
#                 self.indice += 1
#                 if self.indice >= 7:
#                     self.indice = 4
#             else:
#                 self.indice = 0
#                 self.indice += 1
#                 if self.indice >= 3:
#                     self.indice = 0
        
#         self.image = self.animations[self.indice]

#     def saltar(self):
#         if self.salto == 0:
#             self.speed_y = - 15
#             self.salto = 1
#         elif self.salto == 1:
#             self.speed_y = - 15
#             self.salto = 2
#         else:
#             self.salto = 0
        
#         if not self.saltando:
#             self.saltando = True

#     def reset(self):
#         self.rect.center = START_POS_PLAYER
#         self.speed_x = 0
#         self.speed_y = 0

#     def fire(self, sprites, bombas):
#         if self.playing:
#             bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
#             self.sound_bomb.play()
#             sprites.add(bomba)
#             bombas.add(bomba)

#     def stop(self):
#         self.playing = False

#     def draw(self):
#         pass

#     def walking(self):
#         pass

#     def jumping(self):
#         pass

#     def staying(self):
#         pass

#     def add_x(self):
#         pass

#     def add_y(self):
#         pass

#     def do_movement(self):
#         pass

#     def is_on_platform(self):
#         pass

#     def do_animations(self):
#         pass











































































































































# import pygame

# from config import *
# from projectile import Projectile
# from sprites import *
# from manipular_imagenes import Manipular_imagenes

# class Player(pygame.sprite.Sprite):
#     def __init__(self, size: tuple, posicion_inicial: tuple) -> None:
#         super().__init__()
#         self.indice = 0
#         # self.stay_r = get_stay_r()
#         # self.stay_l = get_stay_l()
#         # self.walk_r = get_walk_r()
#         # self.walk_l = get_walk_l()
#         # self.jump_r = get_jump_r()
#         # self.jump_l = get_jump_l()
#         #self.animations = get_animations()
        
#         #self.image = self.animations[self.indice]
        
#         # self.rect = self.image.get_rect()
#         # self.rect.centerx = WIDTH // 2
#         # self.rect.bottom = HEIGHT - 10
        
#         self.speed_x = 0    
#         self.speed_y = 0
        
#         self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
#         self.playing = True
        
#         self.saltando = False
#         self.left = True
#         self.salto = 0
        
#         #confeccion
#         self.ancho = size[0]
#         self.alto = size[1]
#         #animaciones
#         self.contador_pasos = 0
#         self.que_hace = "quieto"
#         self.animaciones = Manipular_imagenes(diccionario_animaciones, (self.ancho, self.alto), False, False) #pasar por parametro
#         self.animaciones.reescalar_imagen()
#         #rectangulos
#         self.lados = self.animaciones.obtener_rectangulos()
    
#     def animar(self, pantalla, que_animacion: str):
#         animacion = self.animaciones[que_animacion]  # aca del diccionario de animaciones que agrre depende que animacion # fijarse si esta bien
#         largo = len(animacion)
#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0
#         pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
#         self.contador_pasos += 1
    
    
#     def move(self):
#         self.rect.x += self.speed_x
#         #self.rect.y += self.speed_y
    
#     def aplicar_gravedad(self):
#         # SALTO
#         # CAIDA
#         # ALGO MAS
#         pass
    
#     def update_german(self, pantalla):
#         self.do_animation(pantalla, "quieto_derecha")
    
    
    
    
    
#     def update(self):
#         #movimiento horizontal
#         self.rect.x += self.speed_x
        
#         #limites
#         if self.rect.left <= DISPLAY_LEFT:
#             self.rect.left = DISPLAY_LEFT
#         elif self.rect.right >= DISPLAY_RIGHT:
#             self.rect.right = DISPLAY_RIGHT
#         if self.rect.top <= DISPLAY_TOP:
#             self.rect.top = DISPLAY_TOP
#         elif self.rect.bottom >= DISPLAY_BOTTOM:
#             self.rect.bottom = DISPLAY_BOTTOM

#         #saltando
#         if self.salto != 0:
#             self.rect.y += self.speed_y
#             self.speed_y += 1
#             print(self.speed_y)
            
#             if self.rect.bottom >= HEIGHT - 10:
#                 self.rect.bottom = HEIGHT - 10
#                 self.saltando = False
#                 self.salto = 0
        
#         # izquierda
#         if self.speed_x < 0:    # si el tipo esta yendo a la izquierda
#             self.left = True        # y ya esta mirando a la izquierda
#             #salta
#             if self.saltando:   # si esta saltando
#                 self.indice = 23    # se carga la imagen de salto a la izquierda
#                 self.indice += 1
#                 if self.indice >= 29:
#                     self.indice = 23
#             #camina
#             else:
#                 self.indice = 11
#                 self.indice += 1
#                 if self.indice >= 14:
#                     self.indice = 11
#         #derecha
#         elif self.speed_x > 0:
#             self.left = False
#             #salta
#             if self.saltando:
#                 self.indice = 15
#                 self.indice += 1
#                 if self.indice >= 22:
#                     self.indice = 15
#             #camina
#             else:
#                 self.indice = 8
#                 self.indice += 1
#                 if self.indice >= 11:
#                     self.indice = 8
#         # esta parado y no salta
#         elif self.speed_x == 0 and not self.saltando:
#             if self.left:
#                 self.indice = 4
#                 self.indice += 1
#                 if self.indice >= 7:
#                     self.indice = 4
#             else:
#                 self.indice = 0
#                 self.indice += 1
#                 if self.indice >= 3:
#                     self.indice = 0
        
#         self.image = self.animations[self.indice]

#     def saltar(self):
#         if self.salto == 0:
#             self.speed_y = - 15
#             self.salto = 1
#         elif self.salto == 1:
#             self.speed_y = - 15
#             self.salto = 2
#         else:
#             self.salto = 0
        
#         if not self.saltando:
#             self.saltando = True

#     def reset(self):
#         self.rect.center = START_POS_PLAYER
#         self.speed_x = 0
#         self.speed_y = 0
    
#     def fire(self, sprites, bombas):
#         if self.playing:
#             bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
#             self.sound_bomb.play()
#             sprites.add(bomba)
#             bombas.add(bomba)
    
#     def stop(self):
#         self.playing = False
    
#     def draw(self):
#         pass
    
#     def walking(self):
#         pass
    
#     def jumping(self):
#         pass
    
#     def staying(self):
#         pass
    
#     def add_x(self):
#         pass
    
#     def add_y(self):
#         pass
    
#     def do_movement(self):
#         pass
    
#     def is_on_platform(self):
#         pass
    
#     def do_animations(self):
#         pass
    
    
    








    
#########################################################################################








# import pygame

# from config import *
# from projectile import Projectile
# from sprites import *

# class Player(pygame.sprite.Sprite):
#     def __init__(self, path_imagen: str, size: tuple, center: tuple) -> None:
#         super().__init__()
#         self.indice = 0
#         self.stay_r = get_stay_r()
#         self.stay_l = get_stay_l()
#         self.walk_r = get_walk_r()
#         self.walk_l = get_walk_l()
#         self.jump_r = get_jump_r()
#         self.jump_l = get_jump_l()
        
#         self.image = pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png").convert_alpha(), (75, 75))
        
#         self.rect = self.image.get_rect()
#         self.rect.center = center
        
#         self.speed_x = 0    
#         self.speed_y = 0
        
#         self.sound_bomb = pygame.mixer.Sound(PATH_PUNCH_SOUND)
        
#         self.playing = True
        
#         self.salto = 0
        
#         self.que_hace = "stay"
    
    
    
    
#     def move(self):
#         self.rect.x += self.speed_x
#         self.rect.y += self.speed_y
    
    
#     def animation_player(self, screen, rect_player, action):
#         lenght = len(action)
#         if self.indice >= 0:
#             self.indice = 0
#         self.screen.blit(action[self.indice], self.rect)
#         self.indice += 1
    
#     def update_screen(self):
#         if self.que_hace == "derecha":
#             pass
    
    
    
    
#     def update(self):
        
        
#         if self.rect.left <= DISPLAY_LEFT:
#             self.rect.left = DISPLAY_LEFT
#         elif self.rect.right >= DISPLAY_RIGHT:
#             self.rect.right = DISPLAY_RIGHT
#         if self.rect.top <= DISPLAY_TOP:
#             self.rect.top = DISPLAY_TOP
#         elif self.rect.bottom >= DISPLAY_BOTTOM:
#             self.rect.bottom = DISPLAY_BOTTOM
    
#     def reset(self):
#         self.rect.center = START_POS_PLAYER
#         self.speed_x = 0
#         self.speed_y = 0
    
#     def fire(self, sprites, bombas):
#         if self.playing:
#             bomba = Projectile(PATH_IMAGE_PROJECTILE, SIZE_PROJECTILE, self.rect.midtop, SPEED_PROJECTILE)
#             self.sound_bomb.play()
#             sprites.add(bomba)
#             bombas.add(bomba)
    