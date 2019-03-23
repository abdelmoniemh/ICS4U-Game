import os
import pygame as pg
#game options
TITLE = "Esteban Escapes"
WIDTH = 800
HEIGHT = 600
FPS = 60

# define colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

#set up assets
game_folder = os.path.dirname(__file__)
est_folder = os.path.join(game_folder, "EstebanEscapes")
img_folder = os.path.join(est_folder, "testimg")

#camera/bg
speed = 30
bg = pg.image.load(os.path.join(game_folder, 'background.png'))
bg2 = pg.image.load(os.path.join(game_folder, 'background.png'))
bgX = 0
bgX2 = bg.get_width()
#player properties
PLAYER_ACC = 0.7
PLAYER_FRICTION = -0.1
PLAYER_GRAVITY = 0.5
JUMP = -10

#platfroms
PLATFORM_LIST = [(0, HEIGHT - 40, WIDTH*10, 40),
                 (WIDTH/ 2 -50, HEIGHT *0.75, 100, 20),
                 (WIDTH/ 4 -50, HEIGHT *0.85, 120, 20),
                 (600, HEIGHT *0.75, 50, 20)]
#skulls
SKULL_LIST = [(300 , 550)]