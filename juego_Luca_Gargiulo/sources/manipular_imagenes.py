# import pygame

# class Manipular_imagenes:
#     def __init__(self, lista_imagenes, tamaño, flip_x, flip_y) -> None:
#         self.lista_imagenes = lista_imagenes
#         self.tamaño = tamaño
#         self.flip_x = flip_x
#         self.flip_y = flip_y
#         self.rect_principal = pygame.Rect(self.lista_imagenes[0].get_rect())
    
#     def reescalar_imagen(self):
#         for i in range(len(self.lista_imagenes)):
#             self.lista_imagenes[i] = pygame.transform.scale(self.lista_imagenes[i], self.tamaño)
    
#     def girar_imagenes(self):
#         lista_girada = []
#         for imagen in self.lista_imagenes:
#             lista_girada.append(pygame.transform.flip(imagen, self.flip_x, self.flip_y))
        
#         return lista_girada

#     def obtener_rectangulos(self) -> dict:
#         diccionario = {}
#         diccionario["main"] = self.rect_principal
#         diccionario["bottom"] = pygame.Rect(self.rect_principal.left, self.rect_principal.bottom -6, self.rect_principal.width, 6)
#         diccionario["right"] = pygame.Rect(self.rect_principal.right -2, self.rect_principal.top, 2, self.rect_principal.height)
#         diccionario["left"] = pygame.Rect(self.rect_principal.left, self.rect_principal.top, 2, self.rect_principal.height)
#         diccionario["top"] = pygame.Rect(self.rect_principal.left, self.rect_principal.top, self.rect_principal.width, 6)
        
#         return diccionario
