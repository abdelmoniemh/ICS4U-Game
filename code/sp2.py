#sprite classes
import pygame as pg
from settings import *
vec = pg.math.Vector2
game_folder = os.path.dirname(__file__)
class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.health = 60
        self.game = game
        self.image = pg.image.load(os.path.join(game_folder, 'idle.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.change_y = 0
        self.change_x = 0

    def update(self):
        self.calc_grav()

        self.rect.x += self.change_x
        self.pos = self.rect.x

        block_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:

            if self.change_x > 0:
                self.rect.right = block.rect.left

            elif self.change_x < 0:
                self.rect.left = block.rect.right

        self.rect.y += self.change_y

        block_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:

            if self.change_y > 0:
                self.rect.bottom = block.rect.top

            elif self.change_y < 0:
                self.rect.top = block.rect.bottom

            self.change_y = 0











        skull_hit_list = pg.sprite.spritecollide(self, self.game.skulls, False)
        for skl in skull_hit_list:

            if self.change_x > 0:
                self.rect.right = skl.rect.left
                self.health -= 1
            elif self.change_x < 0:
                self.rect.left = skl.rect.right
                self.health -= 1

        self.rect.y += self.change_y

        skull_hit_list = pg.sprite.spritecollide(self, self.game.skulls, False)
        for skl in skull_hit_list:

            if self.change_y > 0:
                self.rect.bottom = skl.rect.top
                self.health -= 1

            elif self.change_y < 0:
                self.rect.top = skl.rect.bottom
                self.health -= 1
            self.change_y = 0








    def calc_grav(self):

        if self.change_y == 0:
            self.change_y = 1

        else:
            self.change_y += 0.7

        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self):
        self.rect.y += 2
        platform_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.change_y = -10

    def go_left(self):
        self.change_x = -6

    def go_right(self):
        self.change_x = 6

    def stop(self):
        self.change_x = 0


class Skull(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder, 'skull.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.platforms
        pg.sprite.Sprite.__init__(self, game.platforms)
        self.game = game
        self.image = plt
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
