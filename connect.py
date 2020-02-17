import socket

import config
from oauth import OAUTH
from utils import b


def open_socket():
    s = socket.socket()
    s.connect((config.HOST, config.PORT))
    s.sendall(b('PASS ' + OAUTH + '\r\n'))
    s.sendall(b('NICK ' + config.BOT_NAME + '\r\n'))
    s.sendall(b('CAP REQ :twitch.tv/commands' + '\r\n'))
    s.sendall(b('CAP REQ :twitch.tv/tags' + '\r\n'))
    s.sendall(b('CAP REQ :twitch.tv/membership' + '\r\n'))
    s.sendall(b('JOIN #' + config.CHANNEL.lower() + '\r\n'))
    return s
