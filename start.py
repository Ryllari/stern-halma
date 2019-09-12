# -*-coding: utf-8-*-

import pygame as pg
import Pyro4

from board import Table, colors, view_playertime
from chat import Chat
from constants import *
from pygame.locals import *
from threading import Thread
from threads import wait_gameserver

PLAYERS = ['Verde', 'Vermelho']

gameserver = Pyro4.Proxy("PYRONAME:gameserver")
playerid = gameserver.choose_player()

SCREEN_SIZE = (1200, 800)
BACKGROUND_COLOR = (0, 0, 0)
CAPTION = "Damas Chinesas"
pg.init()
pg.font.init()

screen = pg.display.set_mode(SCREEN_SIZE)
screen.fill(BACKGROUND_COLOR)
pg.display.set_caption(CAPTION)


if playerid in [1, 2]:
    other = playerid + 1 if playerid == 1 else 1
    bg_image = pg.image.load("background.png")
    font = pg.font.SysFont("arial", 20)

    screen.blit(bg_image, (0, 0))
    screen.blit(
        font.render(f'Você é o Player {playerid} ({PLAYERS[playerid-1]})', True, colors[f'p{playerid}']),
        (700, 750)
    )
    gameboard = Table()
    gameboard.render(screen)
    pg.display.update()

    gamechat = Chat()

    receive = Thread(target=wait_gameserver, args=(playerid, gameserver, gamechat, screen))
    receive.daemon = True
    receive.start()

    finish = False
    playertime = playerid is 1
    while not finish:
        view_playertime(screen, font, playerid)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                gameserver.send_info(playerid, QUIT_INFO, f'Player {playerid} desistiu! PLAYER {other} VENCEU!')
                finish = True

            elif event.type == KEYDOWN:
                gamechat.write(event, screen, playerid, gameserver)

            elif event.type == pg.MOUSEBUTTONDOWN:
                x, y = pg.mouse.get_pos()
                if 670 <= y <= 730:  # Botoes
                    if 600 <= x <= 800:  # Reiniciar
                        gameserver.send_info(playerid, RESET_INFO, f'Player {playerid} reiniciou a partida!')
                    elif 900 <= x <= 1100:  # Desistir
                        gameserver.send_info(playerid, QUIT_INFO, f'Player {playerid} desistiu! PLAYER {other} VENCEU!')
                        finish = True

else:
    font = pg.font.SysFont("arial", 40)
    screen.blit(font.render('Servidor cheio. Tente mais tarde!', True, (255, 255, 255)), (350, 380))
    pg.display.update()

    finish = False
    while not finish:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True



