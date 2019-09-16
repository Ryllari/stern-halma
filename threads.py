import pygame as pg
from constants import *


def wait_gameserver(playerid, gameserver, chat, screen, gameboard):
    info = gameserver.request_action(playerid)
    print(info)
    if info is not None:
        if info.get('type_info', None) is RESET_INFO:
            chat.history.append(f"INFO: LÁ VAMOS NÓS DE NOVO! {info.get('info')}")
            chat.send_msg(screen)
            gameboard.reset_board()
            gameboard.render(screen)
        elif info.get('type_info', None) is QUIT_INFO:
            chat.history.append(f"INFO: {info.get('info')}")
            chat.send_msg(screen)
        elif info.get('type_info', None) is WIN_INFO:
            chat.history.append(f"FIM DE JOGO: {info.get('info')}")
            chat.send_msg(screen)
        gameserver.reset_action_controller(playerid)


def wait_chat_gameserver(playerid, gameserver, chat, screen):
    info = gameserver.request_chat(playerid)
    chat.history += info
    chat.send_msg(screen)
    gameserver.reset_msg_controller(playerid)


def wait_board_gameserver(playerid, gameserver, gameboard):
    info = gameserver.request_board(playerid)
    if info:
        player_point = gameboard.get_point_by_coord(info[0][0], info[0][1])
        other_point = gameboard.get_point_by_coord(info[1][0], info[1][1])
        gameboard.move_points(player_point, other_point)
        gameboard.set_playertime(True)
        gameserver.reset_board_controller(playerid)
