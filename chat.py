# -*-coding: utf-8-*-

import pygame as pg
from pygame.locals import *

pg.font.init()
font = pg.font.SysFont("arial", 15)


class Chat(object):
    def __init__(self):
        self.char = []
        self.msg = ''
        self.history = []

    def write(self, event, screen, playerid, gameserver):
        if event.key == K_BACKSPACE:
            self.char = self.char[0:-1]
        elif event.key == K_RETURN:
            self.msg = f"P{playerid}: " + self.msg
            self.history.append(self.msg)
            self.char = []
            gameserver.send_info(playerid, self.msg)
            self.send_msg(screen)
        elif event.key <= 255:
            if len(self.char) < 30:
                self.char.append(event.unicode)

        self.msg = ''.join(self.char)
        pg.draw.rect(screen, (255, 255, 255), (40, 700, 380, 45))
        screen.blit(font.render(self.msg, True, (0, 0, 0)), (50, 710))
        screen.blit(font.render(f'{len(self.msg)}/30', True, (0, 0, 0)), (375, 730))
        pg.display.update()

    def send_msg(self, screen):
        if len(self.history) == 33:
            self.history.pop(0)
            pg.draw.rect(screen, (72, 72, 72), (0, 40, 450, 650))

        pos_y = 50
        for msg in self.history:
            screen.blit(font.render(msg, 1, (255, 255, 255)), (40, pos_y))
            pos_y += 20

        pg.display.update()
