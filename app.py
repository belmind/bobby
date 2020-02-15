import config
import chat

from connect import open_socket
from datetime import datetime
from utils import str_timestamp, Color, print_divider, bobby
from oauth import OAUTH


def start_up():
    s = open_socket()
    status, msg = chat.join(s)

    if status:
        print(bobby())
        print(msg)
        print_divider()
        return s

    print('BEEP BOOP - Task failed successfully!')
    exit()


def main():
    s = start_up()
    chat.send_message(s, "Fear not! The friendly chatbot is here! 🤖")

    # Main loop
    while True:
        chat.read_messages(s, b'', True)


if __name__ == '__main__':
    main()

