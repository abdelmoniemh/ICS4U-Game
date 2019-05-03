#Abdelmoniem Hassan, Ahmed Alagial, Ethan Girard, Yazeed Alzughabi
#Revison date - April 16th 2019
#Esteban Escapes
#sprite file, where all classes as created and defined

import pygame as pg
from settings import *
vec = pg.math.Vector2
game_folder = os.path.dirname(__file__)
class Player(pg.sprite.Sprite):
    def __init__(self, game):# inits importnt characteristics for thecharacter
        pg.sprite.Sprite.__init__(self)
        self.health = PLAYER_HEALTH #defines players health, 60 means he will die in 1 sec on skulls
        self.game = game
        self.image = pg.image.load(os.path.join(game_folder, 'images/Esteban/'+ str(0) +'.png')).convert()#defining his image
        self.image.set_colorkey(BLACK)#eliminating black background from image
        self.rect = self.image.get_rect()#defining player rect based on image
        self.rect.center = (50, 500)#defining player spawn point
        self.change_y = 0 #variable for y movement
        self.change_x = 0 #variable for x movement

    def update(self):
        self.calc_grav()#calls gravity function

        self.rect.x += self.change_x # rect changes based on x velocity
        self.pos = self.rect.x # position is defined based on x
        #PLATFORM COLLISIONSSSSSSSS
        block_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False) # if a player collides with the sprite group ’platforms’
        for block in block_hit_list:
            if self.change_x > 0: #if the  right side of esteban collides with left side of block’
                self.rect.right = block.rect.left
                self.change_x = 0

            elif self.change_x < 0:#if the left side of esteban collides with right side of block’
                self.rect.left = block.rect.right
                self.change_x = 0

        self.rect.y += self.change_y #moves player rect based on y velocity

        block_hit_list = pg.sprite.spritecollide(self, self.game.platforms, False)
        for block in block_hit_list:

            if self.change_y > 0: #if the bottom of esteban collides with top of block’
                self.rect.bottom = block.rect.top
                self.change_y = 0

            elif self.change_y < 0: #if the top of esteban collides with bottom of block’
                self.rect.top = block.rect.bottom
                self.change_y = 0

            self.change_y = 0
        #SKULLLLLLLL COLLISIONS
        skull_hit_list = pg.sprite.spritecollide(self, self.game.skulls, False)# damages player if he collides with skull
                                                                                # if a player collides with the sprite group ’skull’
        for skl in skull_hit_list:

            if self.change_x > 0: #if the right of esteban collides with left of skull
                self.rect.right = skl.rect.left
                self.health -= 1
            elif self.change_x < 0: #if the left of esteban collides with right of skull
                self.rect.left = skl.rect.right
                self.health -= 1

        self.rect.y += self.change_y

        skull_hit_list = pg.sprite.spritecollide(self, self.game.skulls, False)
        for skl in skull_hit_list: # damages player if he collides with skull

            if self.change_y > 0:#if the bottom of esteban collides with top of skull
                self.rect.bottom = skl.rect.top
                self.health -= 1

            elif self.change_y < 0: #if the top of esteban collides with bottom of skull
                self.rect.top = skl.rect.bottom
                self.health -= 1


    def calc_grav(self):# calculation of gravity

        if self.change_y == 0:
            self.change_y = 1

        else:
            self.change_y += PLAYER_GRAVITY #If the change in y is greater then 0, a change in y is adding when the chracter is in the air resulting in gravity.

        if self.rect.y >= HEIGHT - self.rect.height and self.change_y >= 0:
            self.change_y = 0
            self.rect.y = HEIGHT - self.rect.height

    def jump(self): #jumping, checks if on platform then allowd for jump
        self.rect.y += 2
        platform_hit_list = pg.sprite.spritecollide(self, self.game.tiles, False)
        self.rect.y -= 2

        if len(platform_hit_list) > 0 or self.rect.bottom >= HEIGHT:
            self.change_y = JUMP

    def go_left(self):#makes the character move left
        self.change_x = -PLAYER_SPEED

    def go_right(self):#character goes right
        self.change_x = PLAYER_SPEED

    def stop(self):#character stops
        self.change_x = 0

"Skull, Platform and end game tile are all pretty much the same type of platform but are seprated because they have different collision requiremetns"
class Skull(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)#defines it as a sprite
        self.image = pg.image.load(os.path.join(game_folder, 'images/skull/'+ str(0)+'.png')).convert()#loads image for skull
        self.image.set_colorkey(BLACK)#removes extra background color
        self.rect = self.image.get_rect()#defines rect based on image
        self.rect.x = x * TILESIZE #multiples x size by tilesize to allow for creation through text file
        self.rect.y = y * TILESIZE #multiples y size by tilesize to allow for creation through text file


class Platform(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = plt #loads image for Platform defined in the settings file
        self.rect = self.image.get_rect()#defines rect based on image
        self.rect.x = x * TILESIZE #multiples x size by tilesize to allow for creation through text file
        self.rect.y = y * TILESIZE #multiples y size by tilesize to allow for creation through text file

class endtile(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder, 'images/tiles/hala.jpeg'))#loads image for end tile
        self.rect = self.image.get_rect() #defines rect based on image
        self.rect.x = x * TILESIZE #multiples x size by tilesize to allow for creation through text file
        self.rect.y = y * TILESIZE #multiples y size by tilesize to allow for creation through text file

class trophy(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder, 'images/tiles/hala.jpeg'))#loads image for end tile
        self.rect = self.image.get_rect() #defines rect based on image
        self.rect.x = x * TILESIZE #multiples x size by tilesize to allow for creation through text file
        self.rect.y = y * TILESIZE #multiples y size by tilesize to allow for creation through text file


