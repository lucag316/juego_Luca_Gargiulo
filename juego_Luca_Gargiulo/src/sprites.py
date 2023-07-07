import pygame

#from manipular_imagenes import Manipular_imagenes

def girar_imagenes(lista_original, flip_x, flip_y):
        lista_girada = []
        for imagen in lista_original:
            lista_girada.append(pygame.transform.flip(imagen, flip_x, flip_y))
        
        return lista_girada

def reescalar_imagenes(lista_animaciones, w, h):
    for lista  in lista_animaciones:
        for i in range(len(lista)):
            imagen = lista[i]
            lista[i] = pygame.transform.scale(imagen, (w, h ))
    
def obtener_rectangulos(principal: pygame.Rect) -> dict:
    diccionario = {}
    diccionario["main"] = principal
    diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom -10, principal.width, 10)
    diccionario["right"] = pygame.Rect(principal.right -2, principal.top, 2, principal.height)
    diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
    diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
    
    return diccionario


player_quieto_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_stay_r_1.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_stay_r_2.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_stay_r_3.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_stay_r_4.png")]

player_camina_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_walk_r_1.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_walk_r_2.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_walk_r_3.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_walk_r_4.png")]

player_salta_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_1.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_2.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_3.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_4.png"),
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_5.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_6.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_jump_r_7.png")]

player_ataque_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_fire_r_0.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_fire_r_1.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_fire_r_2.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_fire_r_3.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_fire_r_4.png")]

player_golpeado_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_1.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_2.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_3.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_4.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_5.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_6.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_7.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_8.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku/goku_hit_r_9.png"),]

player_quieto_izquierda = girar_imagenes(player_quieto_derecha, True, False)
player_camina_izquierda = girar_imagenes(player_camina_derecha, True, False)
player_salta_izquierda = girar_imagenes(player_salta_derecha, True, False)
player_ataque_izquierda = girar_imagenes(player_ataque_derecha, True, False)
player_golpeado_izquierda = girar_imagenes(player_golpeado_derecha, True, False)

lista_animaciones_player = [player_quieto_derecha, player_quieto_izquierda, player_camina_derecha, player_camina_izquierda, 
                            player_salta_derecha, player_salta_izquierda, player_ataque_derecha, player_ataque_izquierda,
                            player_golpeado_derecha, player_golpeado_izquierda]


freezer_quieto_izquierda = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_0.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_1.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_2.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_3.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_4.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_5.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_6.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_7.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_8.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/frieza_9.png"),]

freezer_camina_izquierda = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/0.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/1.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/2.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/3.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/4.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/5.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/6.png"),
                            pygame.image.load("./juego_Luca_Gargiulo/assets/images/freezer/7.png")]

freezer_camina_derecha = girar_imagenes(freezer_camina_izquierda, True, False)
freezer_quieto_derecha = girar_imagenes(freezer_quieto_izquierda, True, False)

lista_animaciones_freezer = [freezer_quieto_izquierda, freezer_quieto_derecha ,freezer_camina_izquierda, freezer_camina_derecha]


cell_camina_izquierda = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/0.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/1.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/2.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/3.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/4.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/5.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/6.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/7.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/8.png"),
                        pygame.image.load("./juego_Luca_Gargiulo/assets/images/cell/9.png"),
                        ]

cell_camina_derecha = girar_imagenes(cell_camina_izquierda, True, False)

lista_animaciones_cell = [cell_camina_izquierda, cell_camina_derecha]


reescalar_imagenes(lista_animaciones_player, 50, 50)
reescalar_imagenes(lista_animaciones_freezer, 75, 75)
reescalar_imagenes(lista_animaciones_cell, 75, 75)

############################################################
