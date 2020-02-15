
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


def b(str):
    """ Casts the string to bytes """
    # Poor naming but it's namely for keeping it tidy
    return str.encode()


def print_divider():
    print(f'{Color.OKBLUE}====================================={Color.ENDC}')


def str_timestamp():
    return str(datetime.now().strftime("%H:%M:%S"))


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
