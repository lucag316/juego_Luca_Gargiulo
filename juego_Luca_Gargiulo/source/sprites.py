import pygame

from manipular_imagenes import Manipular_imagenes

# # ###############################################################################################
# # #puede ser una clase de manipular imagenes

# pygame.init()

################################################################################################

# def get_stay_r():
#     animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_4.png").convert_alpha(), (75, 75))]
#     return animation

# def get_stay_l():
#     animation = Manipular_imagenes(get_stay_r(), (75, 75), True, False).girar_imagenes()
#     return animation

# def get_walk_r():
#     animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_4.png").convert_alpha(), (75, 75))]
#     return animation

# def get_walk_l():
#     animation = Manipular_imagenes(get_walk_r, (75, 75), True, False).girar_imagenes()
#     return animation

# def get_jump_r():
#     animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_5.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_6.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_7.png").convert_alpha(), (75, 75))]
#     return animation

# def get_jump_l():
#     animation = Manipular_imagenes(get_jump_r(), (75, 75), True, False).girar_imagenes()
#     return animation









quieto_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_2.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_3.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_4.png")]

quieto_izquierda = Manipular_imagenes(quieto_derecha, (75, 75), True, False).girar_imagenes()

camina_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_1.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_2.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_3.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_4.png")]

camina_izquierda = Manipular_imagenes(camina_derecha, (75, 75), True, False).girar_imagenes()

salta_derecha = [pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_1.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_2.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_3.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_4.png"),
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_5.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_6.png"), 
                pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_7.png")]

salta_izquierda = Manipular_imagenes(salta_derecha, (75, 75), True, False).girar_imagenes()



lista_animaciones_player = [quieto_derecha, quieto_izquierda, camina_derecha, camina_izquierda, salta_derecha, salta_izquierda]



diccionario_animaciones = {}

diccionario_animaciones["quieto_derecha"] = quieto_derecha
diccionario_animaciones["quieto_izquierda"] = quieto_izquierda
diccionario_animaciones["camina_derecha"] = camina_derecha
diccionario_animaciones["camina_izquierda"] = camina_izquierda
diccionario_animaciones["salta_derecha"] = salta_derecha
diccionario_animaciones["salta_izquierda"] = salta_izquierda











############################################################

def get_animations():
    animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_2.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_3.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_4.png").convert_alpha(), (75, 75)),
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_1.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_2.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_3.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_4.png").convert_alpha(), (75, 75)),
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_1.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_2.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_3.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_4.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_1.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_2.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_3.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_4.png").convert_alpha(), (75, 75)),
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_1.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_2.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_3.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_4.png").convert_alpha(), (75, 75)),
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_5.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_6.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_7.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_1.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_2.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_3.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_4.png").convert_alpha(), (75, 75)),
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_5.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_6.png").convert_alpha(), (75, 75)), 
                pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_7.png").convert_alpha(), (75, 75))]
    return animation