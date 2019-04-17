#sprite classes
import pygame as pg
from settings import *
vec = pg.math.Vector2
game_folder = os.path.dirname(__file__)
class Player(pg.sprite.Sprite):
    def __init__(self, game):# inits importnt characteristics for thecharacter
        pg.sprite.Sprite.__init__(self)
        self.health = 60
        self.game = game
        self.image = pg.image.load(os.path.join(game_folder, 'images/Esteban/'+ str(0) +'.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (100, 500)
        self.change_y = 0
        self.change_x = 0

    def update(self):
        self.calc_grav()#calls gravity function

        self.rect.x += self.change_x
        self.pos = self.rect.x
        #PLATFORM COLLISIONSSSSSSSS
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
        #SKULLLLLLLL COLLISIONS
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
        for skl in skull_hit_list: # damages player if he collides with skull

            if self.change_y > 0:
                self.rect.bottom = skl.rect.top
                self.health -= 1

            elif self.change_y < 0:
                self.rect.top = skl.rect.bottom
                self.health -= 1


    def calc_grav(self):# calculation of gravity

        if self.change_y == 0:
            self.change_y = 1

        else:
            self.change_y += PLAYER_GRAVITY

        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self): #jumpung, checks if on platform then allowd for jump
        self.rect.y += 2
        platform_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.change_y = JUMP

    def go_left(self):
        self.change_x = -PLAYER_SPEED

    def go_right(self):
        self.change_x = PLAYER_SPEED

    def stop(self):
        self.change_x = 0

"Skull, Platform and end game tile are all pretty much the same type of platform but are seprated because they have different collision requiremetns"
class Skull(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder, 'images/skull.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = plt
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE

class endtile(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder, 'images/hala.jpeg'))
        #self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE