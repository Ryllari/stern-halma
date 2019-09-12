def receive_packet(playerid, gameserver, chat, screen):
    while True:
        msg = gameserver.request_info(playerid)
        if msg is not None:
            chat.history.append(msg)
            chat.send_msg(screen)

        gameserver.reset_msg_controller(playerid)
