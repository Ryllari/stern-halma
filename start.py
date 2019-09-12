# -*-coding: utf-8-*-

import pygame as pg
import Pyro4

from board import Table, colors
from chat import Chat
from pygame.locals import *
from threading import Thread
from threads import receive_packet

PLAYERS = ['Verde', 'Vermelho']

gameserver = Pyro4.Proxy("PYRONAME:gameserver")
playerid = gameserver.choose_player()


SCREEN_SIZE = (1200, 800)
BACKGROUND_COLOR = (0, 0, 0)
CAPTION = "Damas Chinesas"

pg.init()
pg.font.init()
bg_image = pg.image.load("background.png")
font = pg.font.SysFont("arial", 20)

screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUND_COLOR)
pg.display.set_caption(CAPTION)
screen.blit(bg_image, (0, 0))
screen.blit(font.render(f'Player {playerid} ({PLAYERS[playerid-1]})', True, colors['p1']), (700, 750))
gameboard = Table()
gameboard.render(screen)
pg.display.update()


gamechat = Chat()

receive = Thread(target=receive_packet, args=(playerid, gameserver, gamechat, screen))
receive.daemon = True
receive.start()

finish = False
while not finish:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
        if event.type == KEYDOWN:
            gamechat.write(event, screen, playerid, gameserver)

