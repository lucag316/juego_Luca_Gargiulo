import pygame

#---------COLORES--------------------------
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 106, 0)
PINK = (255, 46, 241)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

#COLOR_LASER = (191, 4, 4)
#---------COLORES--------------------------


#------------------------COORDENADAS----------------------------------
WIDTH = 1200
HEIGHT = 700
ORIGIN = (0, 0)
CENTER = (WIDTH // 2, HEIGHT // 2)

DISPLAY_BOTTOM = HEIGHT
DISPLAY_TOP = 0
DISPLAY_LEFT = 0
DISPLAY_RIGHT = WIDTH
DISPLAY_CENTER_X = WIDTH // 2
DISPLAY_CENTER_Y = HEIGHT // 2
DISPLAY_MIDTOP = (DISPLAY_CENTER_X, DISPLAY_TOP)
DISPLAY_MIDBOTTOM = (DISPLAY_CENTER_X, HEIGHT)
#------------------------COORDENADAS----------------------------------


#----------------------TAMAÑOS-------------------------------
SIZE_SCREEN = (WIDTH, HEIGHT)
SIZE_ICON = (32, 32)

SIZE_PLAYER = (100, 150)
SIZE_BALL = (50, 50)
SIZE_PROJECTILE = (25, 25)
#----------------------TAMAÑOS-------------------------------


#--------------------TIEMPO----------------------------
FPS = 60 

SPEED_PLAYER = 5
SPEED_BALL = 5
SPEED_PROJECTILE = 7
#--------------------TIEMPO----------------------------


#--------------------CANTIDADES---------------------------------
MAX_BALLS = 10
#--------------------CANTIDADES---------------------------------


#------------------------POSICIONES-------------------------------------
START_POS_PLAYER = (WIDTH // 2, HEIGHT - 50)
SCORE_POS = (25, 25)
#------------------------POSICIONES-------------------------------------


#------------------------------------PATHS----------------------------------------------
PATH_IMAGE_BACKGROUND = "./juego_Luca_Gargiulo/assets/images/fondo1.png"
PATH_IMAGE_ICON = "./juego_Luca_Gargiulo/assets/images/icon.png"
PATH_IMAGE_PLAYER = "./juego_Luca_Gargiulo/assets/images/goku.png"
PATH_IMAGE_PROJECTILE = "./juego_Luca_Gargiulo/assets/images/bomba.png"
PATH_IMAGE_BALL_1 = "./juego_Luca_Gargiulo/assets/images/ball_1.png"

PATH_BACKGROUND_MUSIC = "./juego_Luca_Gargiulo/assets/sounds/musica_fondo.mp3"
PATH_PUNCH_SOUND = "./juego_Luca_Gargiulo/assets/sounds/piña.mp3"

PATH_FONT_DBZ = "./juego_Luca_Gargiulo/assets/fonts/fuente_dbz.ttf"

# PATH_IMAGEN_NAVE = "./juego_nave_2/assets/images/nave.png"
# PATH_IMAGEN_ASTEROIDE = "./juego_nave_2/assets/images/aesteroide.png"
#------------------------------------PATHS----------------------------------------------


GAME_TITTLE = "Dragon Ball Z"

#DEBUG = True   # podria  hacer un modo que si lo cambio me muestre todos los  rectangulos  


DIRECTION_LEFT = 0
DIRECTION_RIGHT = 1