import argparse

import config
import utils
from chat import ChatSession
from utils import Color


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-f',
        '--file_name',
        type=str,
        help='chatlog output filename, .txt format'
    )
    return parser.parse_args()


def main():
    session = ChatSession()
    utils.create_folder()
    session.send_message("The friendly chatbot is here! 🤖")
    args = parser()
    file_name = utils.generate_file_name(args.file_name)

    # Main loop
    try:
        while True:
            session.run(
                read_buffer=b'',
                file_name=file_name,
                path=config.PATH,
                print_flag=config.PRINT_CHAT
            )

    except KeyboardInterrupt:
        print(f'\n{Color.OKGREEN}Great session! The chatlogs has been saved to `{config.PATH}/{file_name}`{Color.ENDC}')  # noqa: E501, E999


if __name__ == '__main__':
    main()
