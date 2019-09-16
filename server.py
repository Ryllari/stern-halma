# -*-coding: utf-8-*-

import Pyro4

from constants import *


@Pyro4.expose
@Pyro4.behavior(instance_mode='single')
class GameServer(object):
    def __init__(self):
        self.players = []
        self.msg = [[]] * 2
        self.board = [[]] * 2
        self.action = [{'type_info': None, 'info': None}] * 2

    def choose_player(self):
        if not self.players:
            self.players.append('Verde')
            return 1
        elif self.players[0] == None:
            self.players[0] = 'Verde'
            return 1
        elif len(self.players) == 1:
            self.players.append('Vermelho')
            return 2
        elif self.players[1] == None:
            self.players[1] = 'Vermelho'
            return 2
        else:
            return 0

    def send_info(self, player, type_info, info,):
        if type_info == CHAT_INFO:
            self.msg[player - 1].append(info)
        if type_info == BOARD_INFO:
            self.board[player-1] = info
        else:
            if type_info == QUIT_INFO:
                self.players[player-1] = None
            self.action = [{
                'type_info': type_info,
                'info': info,
            }] * 2

    def request_chat(self, player):
        return self.msg[player-2]

    def request_board(self, player):
        return self.board[player-2]

    def request_action(self, player):
        return self.action[player-2]

    def reset_msg_controller(self, player):
        self.msg[player-2] = []

    def reset_board_controller(self, player):
        self.board[player-2] = []

    def reset_action_controller(self, player):
        self.action[player-2] = {
            'type_info': None,
            'info': None,
        }


if __name__ == "__main__":
    Pyro4.Daemon.serveSimple(
        {
            GameServer: "gameserver"
        },
        ns=True
    )
