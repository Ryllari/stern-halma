import pygame as pg
from constants import *


def wait_gameserver(playerid, gameserver, chat, screen, gameboard):
    while True:
        info = gameserver.request_info(playerid)
        if info.get('type_info', None) is CHAT_INFO:
            chat.history.append(info.get('info'))
            chat.send_msg(screen)
        elif info.get('type_info', None) is RESET_INFO:
            chat.history.append(f"INFO: LÁ VAMOS NÓS DE NOVO! {info.get('info')}")
            chat.send_msg(screen)
            gameboard.reset_board()
            gameboard.render(screen)
        elif info.get('type_info', None) is QUIT_INFO:
            chat.history.append(f"INFO: {info.get('info')}")
            chat.send_msg(screen)
        elif info.get('type_info', None) is BOARD_INFO:
            player_point = gameboard.get_point_by_coord(info.get('info')[0][0], info.get('info')[0][1])
            other_point = gameboard.get_point_by_coord(info.get('info')[1][0], info.get('info')[1][1])
            gameboard.move_points(player_point, other_point)
            gameboard.set_playertime(True)
        gameserver.reset_msg_controller(playerid)
