from datetime import datetime

def b(str):
    """ Casts the string to bytes """
    # Poor naming but it's namely for keeping it tidy
    return str.encode()


def print_lines():
    print('================')


def str_timestamp():
    return str(datetime.now().strftime("%H:%M:%S"))
