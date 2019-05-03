# EstebanEscapes
from settings import *
import pygame as pg
from os import path
import os
from sp2 import *
import math



class Game:

    def __init__(self):
        # init game window etc
        self.running = True  # set the while loop to true
        pg.font.init()  # allows for text to be printed onscreen
        pg.mixer.init()  # init sound
        pg.init()  # initilazie pygame
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))  # set the display size
        pg.display.set_caption(TITLE)  # set the name of the game
        self.clock = pg.time.Clock()  # set fps
        self.load_data()  # runs a function that reads the map file

    def load_data(self):
        game_folder = os.path.dirname(__file__)  # sets a path to the same folder as the code
        self.map_data = []  # creates an empty list to add the contents of a text file
        with open(path.join(game_folder, 'map.txt'), 'rt') as f:  # opens path to map file as a readable
            for line in f:  # adds everything in the map file to the list self.map_data
                self.map_data.append(line)


    def new(self):
        # new game -  creates various sprite groups and instances of classes such as platforms
        # some values that need to be defined at the beginning of the game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.trophy = pg.sprite.Group()
        self.endgametile = pg.sprite.Group()
        self.skulls = pg.sprite.Group()
        self.enemy_list = pg.sprite.Group()
        self.tiles = pg.sprite.Group()
        # self.skully = Skull(self)
        self.Esteban = Player(self)
        self.all_sprites.add(self.Esteban)
        self.momentum = 0
        self.sspinCount = 0
        self.trophy_status = False
        # read text file give every element an x, y based on col and row in file
        for row, tiles in enumerate(self.map_data):
            for col, tile in enumerate(tiles):
                if tile == '1':
                    np = Platform(col, row)
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'u':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/tl.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'i':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/mt.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'o':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/tr.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'j':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/ml.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'k':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/m.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'l':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/mr.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'v':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/v.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'b':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/b.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'n':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/n.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == 'f':
                    np = Platform(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/f.png')).convert()
                    self.all_sprites.add(np)
                    PLATFORM_LIST.append(np)
                    self.platforms.add(np)
                    self.tiles.add(np)
                if tile == "s":
                    skll = Skull(col, row)
                    self.all_sprites.add(skll)
                    self.skulls.add(skll)
                    self.tiles.add(skll)
                if tile == "e":
                    end = endtile(col, row)
                    self.all_sprites.add(end)
                    self.endgametile.add(end)
                if tile == "t":
                    np = trophy(col, row)
                    np.image = pg.image.load(os.path.join(game_folder, 'images/tiles/f.png')).convert()
                    self.all_sprites.add(np)
                    self.trophy.add(np)
                    self.tiles.add(np)
                    for event in pg.event.get():
                        if event.type == pg.KEYDOWN:
                            if event.key == pg.K_f and pg.sprite.spritecollide(self.Esteban, self.trophy, False):
                                self.trophy_status = True
                                np.kill()
                                self.trophy.empty()
                                self.all_sprites.remove(self, np)
                                self.tiles.remove(self, np)

                # each character in the text file relates to a instance of a class and this is basically where the map is created
                # from the map
        sk1 = pg.image.load(os.path.join(game_folder, 'images/skull/' + str(0)) + '.png').convert()
        sk2 = pg.image.load(os.path.join(game_folder, 'images/skull/' + str(1)) + '.png').convert()
        sk3 = pg.image.load(os.path.join(game_folder, 'images/skull/' + str(2)) + '.png').convert()
        sk4 = pg.image.load(os.path.join(game_folder, 'images/skull/' + str(3)) + '.png').convert()
        sk5 = pg.image.load(os.path.join(game_folder, 'images/skull/' + str(4)) + '.png').convert()
        self.sk = [sk1, sk2, sk3, sk4, sk5]
        self.run()


    def run(self):
        # game loop - calls all the functions in the order they run in in the game loop
        self.playing = True
        self.espinCount = 0
        self.sspinCount = 0
        if self.sspinCount == 4:
            self.sspinCount = 0
        while self.playing:
            # self.momentum += 0.005 code that is wip for acceleration
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()



            for skl in self.skulls:
                if (0 < skl.rect.x <  800):
                    skl.image = self.sk[round(self.sspinCount)]
                    skl.image.set_colorkey(BLACK)
                    self.sspinCount += 0.0075
                    if round(self.sspinCount) == 4:
                        self.sspinCount = 0


            if self.Esteban.change_x == 0:
                self.Esteban.image = pg.image.load(
                    os.path.join(game_folder, 'images/Esteban/' + str(round(0)) + '.png')).convert()
                self.Esteban.image.set_colorkey(BLACK)
            else:
                self.Esteban.image = pg.image.load(
                    os.path.join(game_folder, 'images/Esteban/' + str(round(self.espinCount)) + '.png')).convert()
                self.Esteban.image.set_colorkey(BLACK)
                self.espinCount += 0.5
                if self.espinCount == 7:
                    self.espinCount = 0

                # last line in loop (AFTER DRAWING EVERYTHING)
            pg.display.flip()


    def events(self):
        # game loop - events
        for event in pg.event.get():
            # check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:  # events when a button is pushed down - currently only controls character movement
                if event.key == pg.K_LEFT or event.key == pg.K_a:
                    self.Esteban.go_left()
                if event.key == pg.K_RIGHT or event.key == pg.K_d:
                    self.Esteban.go_right()
                    # self.Esteban.change_x += self.momentum code that is wip for acceleration
                if event.key == pg.K_UP or event.key == pg.K_SPACE:
                    self.Esteban.jump()
                if event.key == pg.K_f and pg.sprite.spritecollide(self.Esteban, self.trophy, False):
                    self.trophy_status = True

            if event.type == pg.KEYUP:  # when the button is no longer being pressed
                if event.key == pg.K_LEFT or event.key == pg.K_a and self.Esteban.change_x < 0:
                    self.Esteban.stop()
                if event.key == pg.K_RIGHT or event.key == pg.K_d and self.Esteban.change_x > 0:
                    # self.Esteban.change_x = PLAYER_SPEED code that is wip for acceleration
                    # self.momentum = 0 code that is wip for acceleration
                    self.Esteban.stop()

        if self.Esteban.health <= 0:  # checkes players health if it is equal to or less than 0
            print("Oh, dios mio Esteban died")
            if self.playing:
                self.playing = False
            self.running = False


    def update(self):
        # game loop - update
        self.all_sprites.update()  # updates all sprites in the all sprites group
        self.enemy_list.update()

        if self.Esteban.rect.right >= WIDTH / 5:  # Locks player to the left section of the sreen
            self.Esteban.rect.right = WIDTH / 5
        if self.Esteban.rect.right <= WIDTH / 7:
            self.Esteban.rect.right = WIDTH / 7

        if self.Esteban.change_x > 0:
            self.Esteban.pos += -1.2 * (
                self.Esteban.change_x)  # moves the platforms to the left depending the players velocity gives the illusion of movemtent
            for plat in self.platforms:
                plat.rect.x += -1.2 * (self.Esteban.change_x)
            for skl in self.skulls:
                skl.rect.x += -1.2 * (self.Esteban.change_x)
            for end in self.endgametile:
                end.rect.x += -1.2 * (self.Esteban.change_x)
            for end in self.trophy:
                end.rect.x += -1.2 * (self.Esteban.change_x)
        ends = pg.sprite.spritecollide(self.Esteban, self.endgametile,
                                       False)  # checks for collisions with the last tiles in the level and if it collides closes the game
        if ends and self.trophy_status == True:
            if self.playing:
                self.playing = False
            self.running = False


    def draw(self):
        # render game
        self.screen.fill(BLACK)
        self.screen.blit(bg, (0, 0))  # background
        self.enemy_list.draw(self.screen)  # draws sprite group on screen
        self.all_sprites.draw(self.screen)  # draws sprite group on screen
        self.platforms.draw(self.screen)  # draws sprite group on screen
        self.myfont = pg.font.SysFont('Comic Sans MS', 20)  # defines a font that allows for printing on screens
        self.textsurface = self.myfont.render('Health: ' + (str(self.Esteban.health)), False,
                                              (WHITE))  # prints players health on screen
        self.screen.blit(self.textsurface, (WIDTH / 8, HEIGHT - 600))  # prints players health on screen
        self.textsurface2 = self.myfont.render('Velocity: ' + (str(self.Esteban.change_x)), False,
                                               (WHITE))  # prints velocity health on screen
        self.screen.blit(self.textsurface2, (WIDTH - 150, HEIGHT - 600))  # prints velocity health on screen

        self.espinP = []
        for pic in range(8):
            self.espin = pg.image.load('images/Esteban/' + str(pic) + '.png')
            self.espinP.append(self.espin)

        self.sspinP = []
        for pic in range(5):
            self.sspin = pg.image.load('images/skull/' + str(pic) + '.png')
            self.sspinP.append(self.sspin)


    def show_start_screen(self):
        # start screen
        menuIMG = pg.image.load('MainMenuBackground.png')
        menuIMG = pg.transform.scale(menuIMG, (800, 608))
        clearBlack75 = pg.image.load('transpBlack75.png')
        clearBlack75 = pg.transform.scale(clearBlack75, (800, 200))

        pg.mixer.music.load('Ancient, Desert, Thoughtful Song - Non Copyright, Royalty Free.ogg')
        pg.mixer.music.set_volume(1)
        pg.mixer.music.play(-1)

        fontGlobal = 'Arial'

        spinP = []

        for pic in range(32):
            if pic <= 9:
                spin = pg.image.load('pyramidSpinIMG/frame_0' + str(pic) + '_delay-0.06s.png')
            else:
                spin = pg.image.load('pyramidSpinIMG/frame_' + str(pic) + '_delay-0.06s.png')
            spin = pg.transform.scale(spin, (210, 160))
            spinP.append(spin)

        class button():
            def __init__(self, x, y, font, font_size, text='', boldness=False):
                self.x = x
                self.y = y
                self.text = text
                self.font = font
                self.font_size = font_size
                self.boldness = boldness
                self.screen = pg.display.set_mode((WIDTH, HEIGHT))
                pg.font.init()

            def draw(self, win, outline=None):
                font = pg.font.SysFont(self.font, self.font_size, bold=self.boldness)
                text = font.render(self.text, 1, (255, 255, 255))
                if outline:
                    pg.draw.rect(win, outline, (self.x, self.y, text.get_width(), text.get_height()), 0)

                if self.text != '':
                    font = pg.font.SysFont(self.font, self.font_size, bold=self.boldness)
                    text = font.render(self.text, 1, (255, 255, 255))
                    self.screen.blit(text, (self.x, self.y))

            def isOver(self, pos):
                font = pg.font.SysFont(self.font, self.font_size, bold=self.boldness)
                text = font.render(self.text, 1, (255, 255, 255))
                if pos[0] > self.x and pos[0] < self.x + text.get_width():
                    if pos[1] > self.y and pos[1] < self.y + text.get_height():
                        return True

                return False

        def redrawWindow():
            startButton.draw(self.screen)
            storeButton.draw(self.screen)
            optionsButton.draw(self.screen)
            objectivesButton.draw(self.screen)
            invButton.draw(self.screen)
            statsButton.draw(self.screen)

        run = True
        startButton = button(250, 470, fontGlobal, 18, 'Start Game')
        storeButton = button(250, 535, fontGlobal, 18, 'Store')
        optionsButton = button(435, 470, fontGlobal, 18, 'Options')
        objectivesButton = button(435, 535, fontGlobal, 18, 'Objectives')
        invButton = button(620, 470, fontGlobal, 18, 'Invite Friends')
        statsButton = button(620, 535, fontGlobal, 18, 'Stats')

        spinCount = 0
        while run:
            self.screen.blit(menuIMG, (0, 0))
            self.screen.blit(clearBlack75, (0, 445))
            self.screen.blit(spinP[spinCount], (0, 445))
            spinCount += 1
            if spinCount == 32:
                spinCount = 0
            redrawWindow()
            pg.display.update()

            for event in pg.event.get():
                pos = pg.mouse.get_pos()

                if event.type == pg.QUIT:
                    run = False
                    pg.quit()
                    quit()

                if event.type == pg.MOUSEBUTTONDOWN:
                    if startButton.isOver(pos):
                        while g.running:  # runs the game loop
                            g.new()
                            g.show_go_screen()
                        run = False
                    if storeButton.isOver(pos):
                        print('clicked the store button')
                    if optionsButton.isOver(pos):
                        print('clicked the options button')
                    if objectivesButton.isOver(pos):
                        print('clicked the objectives button')
                    if invButton.isOver(pos):
                        print('clicked the invite friends button')
                    if statsButton.isOver(pos):
                        print('clicked the stats button')

                if event.type == pg.MOUSEMOTION:
                    if startButton.isOver(pos):
                        startButton.boldness = True
                    elif storeButton.isOver(pos):
                        storeButton.boldness = True
                    elif optionsButton.isOver(pos):
                        optionsButton.boldness = True
                    elif objectivesButton.isOver(pos):
                        objectivesButton.boldness = True
                    elif invButton.isOver(pos):
                        invButton.boldness = True
                    elif statsButton.isOver(pos):
                        statsButton.boldness = True
                    else:
                        startButton.boldness = False
                        storeButton.boldness = False
                        optionsButton.boldness = False
                        objectivesButton.boldness = False
                        invButton.boldness = False
                        statsButton.boldness = False


    def show_go_screen(self):
        # game over screen
        pass


g = Game()  # creates of an instance of the game class
g.show_start_screen()  # shows start screen
