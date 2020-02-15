import config
import os
import random
import sys

from datetime import datetime


class Color():
    """Chat colors for the terminal"""
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def random_color():
    """
    Returns a random color.
    Excludes `BOLD`, `UNDERLINE` and `ENDC`.
    """
    colors = [
        Color.HEADER,
        Color.OKBLUE,
        Color.WARNING,
        Color.FAIL
    ]
    return random.choice(colors)


def b(str):
    """ Casts the string to bytes """
    # Poor naming but it's namely for keeping it tidy
    return str.encode()


def print_divider():
    print(f'{Color.OKBLUE}====================================={Color.ENDC}')


def str_timestamp():
    return str(datetime.now().strftime("%H:%M:%S"))


def str_datetime():
    return str(datetime.now().strftime("%d-%m-%y"))


def bobby():
    return """
 _           _     _
| |__   ___ | |__ | |__  _   _
| '_ \ / _ \| '_ \| '_ \| | | |
| |_) | (_) | |_) | |_) | |_| |
|_.__/ \___/|_.__/|_.__/ \__, |
                         |___/

- The friendly chatbot! 🤖
"""


def create_folder():
    """
    Creates a new directory and saves the chat logs in files. Defaults
    to `chatlogs`.

    If a file_name is specified the file will be `file_name.txt`
    otherwise will default to date.
    """
    # define the name of the directory to be created
    path = config.PATH

    # define the access rights
    mode = 0o755
    if not os.path.exists(path):
        os.mkdir('chatlogs', mode=mode)

    return path


def generate_file_name():
    try:
        file_name = str(sys.argv[1]) + '.txt'
    except IndexError:
        file_name = str_datetime() + '.txt'

    return file_name

