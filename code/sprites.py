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
        self.rect.center = (WIDTH , HEIGHT)
        self.pos = vec(100, 400)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)



    def collisions(self, direction):
        for i in self.game.platforms:
            if pg.sprite.collide_rect(i, self):
                if direction == "horizontal":
                    if self.rect.right == i.rect.left:
                        # self.rect.right = i.rect.left
                        self.acc.x = 0
                        self.vel.x = 3
                    if self.rect.left == i.rect.right:
                        # self.rect.left = i.rect.right
                        self.acc.x = 0
                        self.vel.x = -3
                if direction == "vertical":
                    if self.rect.bottom >= i.rect.top:
                        self.rect.bottom = i.rect.top
                        self.acc.y = 0
                        self.vel.y = 0
                    if self.rect.top >= i.rect.bottom:
                        self.rect.bottom = i.rect.top
                        self.acc.y = 0
                        self.vel.y = 0



    def jump(self):
        # #jump only if platform
        # self.rect.x += 1
        # hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        # self.rect.x -= 1
        #if hits:
        self.vel.y = JUMP + 5


    def update(self):
        self.acc = vec(0, PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_a] or keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_d] or keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC


         #more normal movement
        '''if keys[pg.K_a]:
            self.acc.x = -5
        if keys[pg.K_a] == False:
            self.vel.x = 0
        if keys[pg.K_d]:
            self.acc.x = 5
        if keys[pg.K_d] == False:
            self.vel.x = 0'''

        #apply friction
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #equations of motion
        self.vel += self.acc
        self.pos.x += self.vel.x + (0.5*self.acc.x)
        self.rect.centerx = self.pos.x
        self.collisions('horizontal')
        self.pos.y += self.vel.y + (0.5 * self.acc.y)
        self.rect.bottom = self.pos.y
        self.collisions('vertical')
        #self.rect.midbottom = self.pos

        #dont leave screen
        if self.pos.x >= WIDTH:
            self.pos.x = WIDTH
        if self.pos.x <= 32:
            self.pos.x = 32



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
