import config
import socket

from oauth import OAUTH
from utils import b

def open_socket():
    s = socket.socket()
    s.connect((config.HOST, config.PORT))
    s.send(b('PASS ' + OAUTH + '\r\n'))
    s.send(b('NICK ' + config.BOT_NAME + '\r\n'))
    s.send(b('JOIN # ' + config.CHANNEL + '\r\n'))
    return s
