import pygame

# from manipular_imagenes import Manipular_imagenes

# # ###############################################################################################
# # #puede ser una clase de manipular imagenes

# pygame.init()

# # ################################################################################################

# def get_stay_r():
#     animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_4.png").convert_alpha(), (75, 75))]
#     return animation

# def get_stay_l():
#     animation = Manipular_imagenes(get_stay_r(), (75, 75), True, False)
#     return animation

# def get_walk_r():
#     animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_4.png").convert_alpha(), (75, 75))]
#     return animation

# def get_walk_l():
#     animation = Manipular_imagenes(get_walk_r(), (75, 75), True, False)
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
#     animation = Manipular_imagenes(get_jump_r(), (75, 75), True, False)
#     return animation


# # diccionario_animaciones = {}

# # diccionario_animaciones["quieto_derecha"] = get_stay_r()
# # diccionario_animaciones["quieto_izquierda"] = get_stay_l()
# # diccionario_animaciones["camina_derecha"] = get_walk_r()
# # diccionario_animaciones["camina_izquierda"] = get_walk_l()
# # diccionario_animaciones["salta_derecha"] = get_jump_r()
# # diccionario_animaciones["salta_izquierda"] = get_jump_l()









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












############################################################

# def get_animations():
#     animation =[pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_r_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_stay_l_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_r_4.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_walk_l_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_5.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_6.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_r_7.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_1.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_2.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_3.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_4.png").convert_alpha(), (75, 75)),
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_5.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_6.png").convert_alpha(), (75, 75)), 
#                 pygame.transform.scale(pygame.image.load("./juego_Luca_Gargiulo/assets/images/goku_jump_l_7.png").convert_alpha(), (75, 75))]
#     return animation