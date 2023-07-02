# diccionario_animaciones = {}
# diccionario_animaciones["quieto_derecha"] = get_stay_r()
# diccionario_animaciones["quieto_izquierda"] = get_stay_l()
# diccionario_animaciones["camina_derecha"] = get_walk_r()
# diccionario_animaciones["camina_izquierda"] = camina_izquierda


# def actualizar_pantalla(pantalla, un_personaje: Player, fondo):
#     pantalla.blit(fondo, (ORIGIN))
#     # plataformas
#     un_personaje.update_german(pantalla)
    
#         #confeccion
#         self.ancho = size[0]
#         self.alto = size[1]
#         #animaciones
#         self.contador_pasos = 0
#         self.que_hace = "quieto"
#         self.animaciones = animaciones #pasar por parametro
#         self.reescalar_animaciones()
#         #rectangulos
#         rectangulo = self.animaciones["quieto_derecha"][0].get_rect()  # pygame rect es solo para que despues lo vea vs code
#         rectangulo.x = posicion_inicial[0]
#         rectangulo.y = posicion_inicial[1]
#         self.lados = obtener_rectangulos(rectangulo)
        
    
#     # def reescalar_animaciones(self):
#     #     for clave in self.animaciones:
#     #         reescalar_imagen(self.animaciones[clave], (self.ancho, self.alto)) # va reescalando quieto izquierda, derecha, camina iz...
    
#     # def animar(self, pantalla, que_animacion: str):
#     #     animacion = self.animaciones[que_animacion]  # poner bien la animacion
#     #     largo = len(animacion)
#     #     if self.contador_pasos >= largo:
#     #         self.contador_pasos = 0
#     #     pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
#     #     self.contador_pasos += 1
    
    
#     # def move(self):
#     #     self.rect.x += self.speed_x
#     #     #self.rect.y += self.speed_y
    
#     # def aplicar_gravedad(self):
#     #     # SALTO
#     #     # CAIDA
#     #     # ALGO MAS
#     #     pass
    
#     # def update_german(self, pantalla):
#     #     self.do_animation(pantalla, "quieto_derecha")
    