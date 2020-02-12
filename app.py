import config


from chat import join_chat
from datetime import datetime
from utils import b
from connect import open_socket
from oauth import OAUTH

def start_up():
    s = open_socket()
    status, msg = join_chat(s)

    if status:
        print(msg)
        return s


def send_message(s, msg):
    dt = str(datetime.now().strftime("%H:%M:%S"))
    _msg = b('PRIVMSG #' + config.CHANNEL + ' :' + msg)
    s.send(_msg)
    print('[' + dt + ']' + ' bobby > : ' + msg)


def main():
    s = start_up()
    send_message(s, "I'm Bobby! The friendly chatbot!")

if __name__ == '__main__':
    main()
