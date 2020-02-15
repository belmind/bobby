import chat
import config
import sys
import utils

from connect import open_socket
from datetime import datetime
from utils import (
    str_timestamp, str_datetime, Color, print_divider,
    bobby
)
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
    utils.create_folder()
    chat.send_message(s, "Fear not! The friendly chatbot is here! 🤖")

    # Main loop
    while True:
        chat.run(
            s=s,
            read_buffer=b'',
            file_name=utils.generate_file_name(),
            path=config.PATH,
            print_flag=config.PRINT_CHAT
        )


if __name__ == '__main__':
    main()

