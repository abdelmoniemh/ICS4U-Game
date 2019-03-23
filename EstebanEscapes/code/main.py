#EstebanEscaper
from settings import *
import pygame as pg

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


    def new(self):

        #new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.skulls = pg.sprite.Group()

        #self.skully = Skull(self)
        self.Esteban = Player(self)
        self.all_sprites.add(self.Esteban)

        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)

        for skl in SKULL_LIST:
            s = Skull(*skl)
            self.all_sprites.add(s)
            self.skulls.add(s)

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
            pg.quit()



    def update(self):
        #game loop - update
        self.all_sprites.update()
        burn = pg.sprite.spritecollide(self.Esteban, self.skulls, False)
        if burn:
            print("collide with fire")
            self.Esteban.pos.y = burn[0].rect.top + 1
            self.Esteban.vel.y = 0
            self.Esteban.health -= 1
        #if player hits platform
        if self.Esteban.vel.y > 0:
            hits = pg.sprite.spritecollide(self.Esteban, self.platforms, False)
            if hits:
                print("collide with platform")
                self.Esteban.pos.y = hits[0].rect.top +1
                self.Esteban.vel.y = 0


        '''#check for furthest right, FAILED ATTEMPT AT SCROLLING
        if self.Esteban.rect.right >= WIDTH -400:
            self.Esteban.pos.x += -(5)
            for plat in self.platforms:
                plat.rect.x += -(5)
                if plat.rect.right <= WIDTH:
                    plat.kill()'''

    def draw(self):
        #render game
        self.screen.fill(BLACK)

        self.screen.blit(bg, (0,0))
        self.all_sprites.draw(self.screen)
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