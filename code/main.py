#EstebanEscaper
from settings import *
import pygame as pg
from os import path
import os
from sprites import *


class Game:

    def __init__(self):
        #init game window etc
        self.running = True
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.load_data()

    def load_data(self):
        game_folder = os.path.dirname(__file__)
        self.map_data = []
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:
            for line in f:
                self.map_data.append(line)

    def new(self):

        #new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.skulls = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        #self.skully = Skull(self)
        self.Esteban = Player(self)
        self.all_sprites.add(self.Esteban)


        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    np =  Platform(self, col, row)
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                if tile == "s":
                    skl = Skull(col, row)
                    self.all_sprites.add(skl)
                    self.skulls.add(skl)

        self.run()

    def run(self):

        #game loop
        self.playing = True
        while self.playing:

            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()

    def events(self):

        #game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.Esteban.jump()
        if self.Esteban.health <= 0:
            print("esteban died")
            if self.playing:
                self.playing = False
            self.running = False

    def update(self):
        #game loop - update
        self.all_sprites.update()
        self.enemy_list.update()
        burn = pg.sprite.spritecollide(self.Esteban, self.skulls, False)
        if burn:
            self.Esteban.pos.y = burn[0].rect.top + 1
            self.Esteban.vel.y = 0
            self.Esteban.health -= 1
        #if player hits platform

        # hits = pg.sprite.spritecollide(self.Esteban, self.platforms, False)
        # if hits:
        #     if hits[0].rect.top < self.Esteban.rect.midbottom[1]:
        #         self.Esteban.pos.y = hits[0].rect.top
        #         self.Esteban.vel.y = 0
        #         print('1')
        #     else:
        #         print('2')
        #         self.Esteban.pos.y = hits[0].rect.top
        #         self.Esteban.vel.y = 10
        # self.Esteban.rect.y += 1
        # hits = pg.sprite.spritecollide(self.Esteban, self.platforms, False)
        # self.Esteban.rect.y -= 1
        # if hits:
        #     self.Esteban.pos.y = hits[0].rect.top
        #     self.Esteban.vel.y = 0
        # blockhit = pg.sprite.spritecollide(self.Esteban, self.platforms, False)
        # for block in blockhit:
        #     if self.Esteban.vel.y > 0:
        #         self.Esteban.rect.bottom = block.rect.top
        #
        #     if self.Esteban.vel.y < 0:
        #         self.Esteban.rect.top = block.rect.bottom



    def draw(self):
        #render game
        self.screen.fill(BLACK)
        self.screen.blit(bg, (0,-75))
        self.enemy_list.draw(self.screen)
        self.all_sprites.draw(self.screen)
        self.platforms.draw(self.screen)
        # last line in loop (AFTER DRAWING EVERYTHING)
        pg.display.flip()

    def show_start_screen(self):
        #start screen
        pass

    def show_go_screen(self):
        #game over screen
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()



pg.quit()