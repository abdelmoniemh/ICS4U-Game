import pygame, sys
from pygame.locals import *

pygame.init()
FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()

win = pygame.display.set_mode((800,600))
pygame.display.set_caption('Animation')
win.fill((255,255, 255))

backIMG = pygame.image.load('WorldMap.png')
backIMG = pygame.transform.scale(backIMG, (800, 600))
TheX = pygame.image.load('TheX.png')
TheX = pygame.transform.scale(TheX, (32, 32))
TheXB = pygame.image.load('TheXB.png')
TheXB = pygame.transform.scale(TheXB, (32, 32))
padlockB = pygame.image.load('padlockIMGB.png')
padlockB = pygame.transform.scale(padlockB, (26, 26))
padlockG = pygame.image.load('padlockIMGG.png')
padlockG = pygame.transform.scale(padlockG, (26, 26))
backButtonR = pygame.image.load('backButtonR.png')
backButtonR = pygame.transform.scale(backButtonR, (32, 18))
backButtonO = pygame.image.load('backButtonO.png')
backButtonO = pygame.transform.scale(backButtonO, (32, 18))


pygame.mixer.music.load('Ancient, Desert, Thoughtful Song - Non Copyright, Royalty Free.ogg')
pygame.mixer.music.set_volume(1)
pygame.mixer.music.play(-1)

fontGlobal = 'Arial'

spinP=[]


class button():
    def __init__(self, x, y, font, font_size, text='', boldness=False):
        self.x = x
        self.y = y
        self.text = text
        self.font = font
        self.font_size = font_size
        self.boldness = boldness

    def draw(self, win, outline=None):
        font = pygame.font.SysFont(self.font, self.font_size, bold=self.boldness)
        text = font.render(self.text, 1, (255, 255, 255))
        if outline:
             pygame.draw.rect(win, outline, (self.x, self.y, text.get_width(), text.get_height()),0)

        if self.text != '':
            font = pygame.font.SysFont(self.font, self.font_size, bold=self.boldness)
            text = font.render(self.text, 1, (255, 255, 255))
            win.blit(text, (self.x, self.y))

    def isOver(self, pos):
        font = pygame.font.SysFont(self.font, self.font_size, bold=self.boldness)
        text = font.render(self.text, 1, (255, 255, 255))
        if pos[0]>self.x and pos[0] < self.x + text.get_width():
            if pos[1] > self.y and pos[1] < self.y + text.get_height():
                return True

        return False

class XButton():
    def __init__(self, x, y, image, image2, image_width, image_height):
        self.x = x
        self.y = y
        self.image = image
        self.image2 = image2
        self.image_width = image_width
        self.image_height = image_height

    def isOver(self, pos):
        if pos[0]>self.x and pos[0] < self.x + self.image_width:
            if pos[1] > self.y and pos[1] < self.y + self.image_height:
                return True

        return False

    def draw(self, win):
        pos = pygame.mouse.get_pos()
        if self.isOver(pos):
            win.blit(self.image2, (self.x, self.y))
        else:
            win.blit(self.image, (self.x, self.y))

def redrawWindow():
    mexicoButton.draw(win)
    greeceButton.draw(win)
    egyptButton.draw(win)
    backButtonIcon.draw(win)


run = True
mexicoButton = XButton(120, 210, TheXB, TheX, 32, 32)
greeceButton = XButton(410, 160, TheXB, TheX, 32, 32)
egyptButton = XButton(430, 195, padlockB, padlockG, 26, 26)
backButtonIcon = XButton(10, 10, backButtonO, backButtonR, 32, 18)

while run:
    win.blit(backIMG, (0, 0))
    redrawWindow()
    pygame.display.update()

    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()

        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if mexicoButton.isOver(pos):
                print('clicked the Mexico button')
            if greeceButton.isOver(pos):
                print('clicked the Greece button')
            if egyptButton.isOver(pos):
                print('Locked')
            if backButtonIcon.isOver(pos):
                print('clicked the Back button')
