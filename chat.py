import config
from utils import Color, b, random_color, str_timestamp

END = b'End of /NAMES list'


def join(s):
    """Joins a chatroom / channel """
    try:
        read_buffer = b''
        loading = True
        while loading:
            read_buffer = read_buffer + s.recv(1024)
            tmp = read_buffer.split(b'\n')
            read_buffer = tmp.pop()
            for line in tmp:
                loading = END in line

        return True, f"{Color.OKBLUE}Sucessfully joined {config.CHANNEL}'s chat.{Color.ENDC}"  # noqa: E501, E999
    except Exception as e:
        # Genereic Exception is fine for now
        return False, e


def send_message(s, msg):
    """
    Sends a message.

    Args:
        s - Connection.
        msg (string) - Message to send.
    """
    try:
        ts = str_timestamp()
        _msg = b('PRIVMSG #' + config.CHANNEL + ' :' + msg + '\r\n')
        s.sendall(_msg)
        print(f'[{ts}] bobby > : {msg}')
        return True
    except Exception as e:
        # Genereic Exception is fine for now
        return False, e


def run(
    s,
    read_buffer,
    file_name,
    path,
    print_flag=False,
):
    """
    Listens and reads messages in chat. Will call `respond_to_message`
    when relevant. Acts as the main-loop for the bot. Might need to
    refractor later.

    Args:
        s - Connection.
        read_buffer (string) - The read_buffer, usually empty string.
        file_name (string) - Name of file created.
        path (string) - Path to chatlogs, defaults to dir `chatlogs`.
        print_flag (bool) - Determines if print the messages.
    """
    read_buffer = read_buffer + s.recv(1024)
    tmp = read_buffer.split(b'\n')
    read_buffer = tmp.pop()
    contains_emote = False
    emotes = load_emotes()

    with open(path + '/' + file_name, 'a+') as f:
        for line in tmp:
            contains_emote = check_emotes(line, emotes)
            user = get_username(line, contains_emote)
            msg = get_message(line, contains_emote)
            ts = str_timestamp()
            # Twitch will ping every bot once every 5 min with a msg that
            # contains the string `PING`, the bot needs to respond with
            # the same message but with `PONG` instead.
            if 'PING' in msg:
                msg = msg.replace('PING', 'PONG')
                s.sendall(b(msg))

            elif print_flag and msg != '' and user != '':
                print(f'{random_color()}[{ts}] {user} < : {msg}{Color.ENDC}')

            f.write(f'[{ts}] {user} < : {msg} \n')


def get_username(line, emote):
    """
    Returns the username.

    Args:
        line (binary) - Line which we parse.
        emote (bool) - Flag to determine if there is a emote in the line.
    """
    _line = str(line)
    # `i` and `j` are indexes for where we can fetch the username. If a
    # emote is invloved it adds a bunch of flags wich messes up the original
    # parsing. Definitly a hacky implementation but it is fine for now.
    i, j = 1, 2
    if emote:
        i = i + 1
        j = j + 1

    s = _line.split(':', j)
    try:
        return s[i].split('!', 1)[0]
    except IndexError:
        return ''


def get_message(line, emote):
    """
    Returns the message.

    Args:
        line (binary) - Line which we parse.
        emote (bool) - Flag to determine if there is a emote in the line.
    """
    _line = str(line)
    # `i` and `j` are indexes for where we can fetch the username. If a
    # emote is invloved it adds a bunch of flags wich messes up the original
    # parsing. Definitly a hacky implementation but it is fine for now.)
    i, j = 2, 2
    if emote:
        i = i + 1
        j = j + 1

    s = _line.split(':', j)
    try:
        return s[i].replace("\\r'", '')
    except IndexError:
        return ''


def check_emotes(line, emotes=[]):
    """Checks if a specific lines contains at least one emote. """
    _line = str(line).split()
    for word in _line:
        _word = word
        try:
            _word = _word.split(':')[1]
            _word = _word.split('\\')[0]
        except IndexError:
            pass
        if _word in emotes:
            return True

    return False


def load_emotes():
    emotes = []
    with open('emotes.txt', 'r') as f:
        for line in f:
            emotes.append(line.strip())

    return emotes
