from constants import *

def wait_gameserver(playerid, gameserver, chat, screen):
    while True:
        info = gameserver.request_info(playerid)
        if info.get('type_info', None) is CHAT_INFO:
            chat.history.append(info.get('info'))
            chat.send_msg(screen)
        elif info.get('type_info', None) is RESET_INFO:
            chat.history.append(f"INFO: LÁ VAMOS NÓS DE NOVO! {info.get('info')}")
            chat.send_msg(screen)
        elif info.get('type_info', None) is QUIT_INFO:
            chat.history.append(f"INFO: {info.get('info')}")
            chat.send_msg(screen)
        gameserver.reset_msg_controller(playerid)
