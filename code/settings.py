import os
import pygame as pg


#game options
TITLE = "Esteban Escapes"
WIDTH = 800
HEIGHT = 608
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
bg = pg.image.load(os.path.join(game_folder, 'templewip1.png'))
plt = pg.image.load(os.path.join(game_folder, 'platform-1.png'))

#player properties
PLAYER_GRAVITY = 0.7
JUMP = -10
PLAYER_SPEED = 6

#platfroms
PLATFORM_LIST = [(0, HEIGHT - 40),
                 (WIDTH/ 2 -50, HEIGHT *0.75),
                 (WIDTH/ 4 -50, HEIGHT *0.85),
                 (600, HEIGHT *0.75)]

#skulls
SKULL_LIST = [(300, 550)]


TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE



