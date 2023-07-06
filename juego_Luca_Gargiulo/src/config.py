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


#--------------------CANTIDADES---------------------------------
#MAX_BALLS = 10
#--------------------CANTIDADES---------------------------------


#--------------------TIEMPO----------------------------
FPS = 60 
#--------------------TIEMPO----------------------------


#----------------------TAMAÑOS-------------------------------
SIZE_SCREEN = (WIDTH, HEIGHT)
SIZE_ICON = (32, 32)

SIZE_PLAYER = (100, 150)
SIZE_BALL = (50, 50)
SIZE_PROJECTILE = (50, 50)
SIZE_BOLA_ENERGIA = (30, 30)

SIZE_GROUND = (WIDTH, 10)

SIZE_PISO = (1200, 100)
SIZE_PLATAFORMA_1 = (50, 25)
SIZE_PLATAFORMA_2 = (1000, 25)
SIZE_PLATAFORMA_3 = (100, 25)
SIZE_PLATAFORMA_4 = (1000, 25)
SIZE_PLATAFORMA_5 = (100, 25)
SIZE_PLATAFORMA_6 = (100, 25)
SIZE_PLATAFORMA_7 = (25, 275)
SIZE_PLATAFORMA_8 = (800, 25)
SIZE_PLATAFORMA_9 = (100, 25)
SIZE_PLATAFORMA_10 = (25, 150)
SIZE_PLATAFORMA_11 = (400, 25)
SIZE_PLATAFORMA_12 = (50, 25)
SIZE_PLATAFORMA_13 = (100, 25)
SIZE_PLATAFORMA_14 = (100, 25)
#----------------------TAMAÑOS-------------------------------

#--------------------VELOCIDADES----------------------------
SPEED_PLAYER = 15
SPEED_FREEZER = 5
SPEED_CELL = 5

SPEED_TRAMPA_1 = 3
SPEED_TRAMPA_2 = 3
SPEED_TRAMPA_3 = 3
SPEED_TRAMPA_4 = 10
SPEED_TRAMPA_5 = 5
SPEED_TRAMPA_6 = 5

SPEED_BALL = 6
SPEED_PROJECTILE = 7
SPEED_BOLA_ENERGIA = 7
#--------------------VELOCIDADES----------------------------


#------------------------POSICIONES-------------------------------------

POS_SCORE = (25, 25)
POS_START_PLAYER = (WIDTH // 2, HEIGHT - 100)
POS_START_FREEZER = (100, 80)
POS_START_CELL = (200, 235)

POS_PISO = (0, 650)

POS_PLATAFORMA_1 = (150, 450)
POS_PLATAFORMA_2 = (0, 150)
POS_PLATAFORMA_3 = (1100, 225)
POS_PLATAFORMA_4 = (200, 300)
POS_PLATAFORMA_5 = (0, 375)
POS_PLATAFORMA_6 = (0, 550)
POS_PLATAFORMA_7 = (200, 325)
POS_PLATAFORMA_8 = (225, 400)
POS_PLATAFORMA_9 = (1100, 475)
POS_PLATAFORMA_10 = (1000, 425)
POS_PLATAFORMA_11 = (500, 500)
POS_PLATAFORMA_12 = (1025, 550)
POS_PLATAFORMA_13 = (350, 550)
POS_PLATAFORMA_14 = (1100, 75)

POS_ITEM_1 = (50, 50)
POS_ITEM_2 = (250, 350)
POS_ITEM_3 = (1150, 265)
POS_ITEM_4 = (1170, 25)
POS_ITEM_5 = (950, 450)
POS_ITEM_6 = (25, 200)
POS_ITEM_7 = (25, 600)

POS_START_TRAMPA_1 = (0, 625)
POS_START_TRAMPA_2 = (1025, 325)
POS_START_TRAMPA_3 = (0, 250)
POS_START_TRAMPA_4 = (1025, 250)
POS_START_TRAMPA_5 = (450, 625)
POS_START_TRAMPA_6 = (900, 625)




#POS_TIME = ()
#POS_LIVES = ()
#------------------------POSICIONES-------------------------------------


#------------------------------------PATHS----------------------------------------------
PATH_IMAGE_BACKGROUND = "./juego_Luca_Gargiulo/assets/images/fondo1.png"
PATH_IMAGE_ICON = "./juego_Luca_Gargiulo/assets/images/icon.png"
PATH_IMAGE_PLAYER = "./juego_Luca_Gargiulo/assets/images/goku.png"

PATH_IMAGE_PROJECTILE = "./juego_Luca_Gargiulo/assets/images/bomba.png"
PATH_IMAGE_BOLA_ENERGIA = "./juego_Luca_Gargiulo/assets/images/disparos/bola.png"

PATH_IMAGE_TRAMPA_VIOLETA = "./juego_Luca_Gargiulo/assets/images/trampas/0.png"

PATH_IMAGE_BALL_1 = "./juego_Luca_Gargiulo/assets/images/items/ball_1.png"

PATH_IMAGE_PLATAFORMA = "./juego_Luca_Gargiulo/assets/images/plataformas/piedra.png"
PATH_IMAGE_PLATAFORMA_1 = "./juego_Luca_Gargiulo/assets/images/plataformas/0.png"
PATH_IMAGE_PLATAFORMA_2 = "./juego_Luca_Gargiulo/assets/images/plataformas/1.png"
PATH_IMAGE_PLATAFORMA_3 = "./juego_Luca_Gargiulo/assets/images/plataformas/2.png"


PATH_BACKGROUND_MUSIC = "./juego_Luca_Gargiulo/assets/sounds/musica_fondo.mp3"
PATH_PUNCH_SOUND = "./juego_Luca_Gargiulo/assets/sounds/piña.mp3"

PATH_FONT_DBZ = "./juego_Luca_Gargiulo/assets/fonts/fuente_dbz.ttf"
#------------------------------------PATHS----------------------------------------------


DEBUG = False   # podria  hacer un modo que si lo cambio me muestre todos los  rectangulos  
GAME_TITTLE = "Dragon Ball Z"

DIRECTION_LEFT = "izquierda"
DIRECTION_RIGHT = "derecha"

GROUND_LEVEL = 600

# delta time para el tiempo
GRAVITY_PLAYER = 15
JUMP_POWER_PLAYER = 15
FRAME_RATE_MS_PLAYER = 80
MOVE_RATE_MS_PLAYER = 20
JUMP_HEIGHT_PLAYER = 100