# import pygame, sys
# from config import *

# class Button():
#     def __init__(self, pos, font, text_input, base_color, hovering_color) -> None:
#         self.x_pos = pos[0]
#         self.y_pos = pos[1]
#         self.font = font
#         self.base_color = base_color
#         self.hovering_color = hovering_color
#         self.text_input = text_input
#         self.text = self.font.render(self.text_input, True, self.base_color)
#         self.text_rect = self.text.get_rect(center = (self.x_pos, self.y_pos))

#     def update(self, screen):
#         screen.blit(self.text, self.text_rect)
    
#     def check_for_input(self, position):
#         if position[0] in range(self.text_rect.left, self.text_rect.right) and position[1] in range(self.text_rect.top, self.text_rect.bottom):
#             #print("presionado")     # si hago click en el rectangulo del texto se imprime esto
#             return True
#         return False
    
#     def change_color(self, position):
#         if position[0] in range(self.text_rect.left, self.text_rect.right) and position[1] in range(self.text_rect.top, self.text_rect.bottom):
#             self.text = self.font.render(self.text_input, True, self.hovering_color)  # si me paro arriba del rectangulo del texto, cambio de colorla palabra
#         else:
#             self.text = self.font.render(self.text_input, True, self.base_color)


