import config

from chat import join_chat
from connect import open_socket
from datetime import datetime
from oauth import OAUTH
from utils import b, str_timestamp


def start_up():
    s = open_socket()
    status, msg = join_chat(s)

    if status:
        print(msg)
        return s


def send_message(s, msg):
    ts = str_timestamp()
    _msg = b('PRIVMSG #' + config.CHANNEL + ' :' + msg + '\r\n')
    s.sendall(_msg)
    print('[' + ts + ']' + ' bobby > : ' + msg)


def main():
    s = start_up()
    send_message(s, "I'm Bobby! The friendly chatbot!")

if __name__ == '__main__':
    main()
