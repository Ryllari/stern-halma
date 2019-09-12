# -*-coding: utf-8-*-

import Pyro4


@Pyro4.expose
@Pyro4.behavior(instance_mode='single')
class GameServer(object):
    def __init__(self):
        self.players = []
        self.msg = [{'type_info': None, 'info': None}] * 2

    def choose_player(self):
        if not self.players:
            self.players.append('Verde')
            return 1
        elif len(self.players) == 1:
            self.players.append('Vermelho')
            return 2
        else:
            return 0

    def send_info(self, player, type_info, info,):
        self.msg[player-1] = {
            'type_info': type_info,
            'info': info,
        }

    def request_info(self, player):
        return self.msg[player-2]

    def reset_msg_controller(self, player):
        self.msg[player-2] = {
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
