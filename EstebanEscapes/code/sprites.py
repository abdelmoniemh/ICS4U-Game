#sprite classes
import pygame as pg
from settings import *
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game):
        pg.sprite.Sprite.__init__(self)
        self.health = 60
        self.game = game
        self.image = pg.image.load(os.path.join(game_folder, 'idle.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH , HEIGHT)
        self.pos = vec(100, 550)
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def jump(self):
        #jump only if platform
        self.rect.x += 1
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1
        if hits:
            self.vel.y = JUMP

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
        self.pos += self.vel + (0.5*self.acc)

        self.rect.midbottom = self.pos
        #dont leave screen
        if self.pos.x >= WIDTH:
            self.pos.x = WIDTH
        if self.pos.x <= 32:
            self.pos.x = 32

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w, h))
        self.image.fill(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Skull(pg.sprite.Sprite):
    def __init__(self, x, y):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.image.load(os.path.join(game_folder, 'skull.png')).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
