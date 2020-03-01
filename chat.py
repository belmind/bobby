import random
import socket

import config
from emotes import check_emotes, load_emotes
from utils import Color, b, bobby, print_divider, random_color, str_timestamp

END = b'End of /NAMES list'


class ChatSession():
    def __init__(self):
        self.oauth = config.OAUTH
        self.host = config.HOST
        self.port = config.PORT
        self.bot_name = config.BOT_NAME
        self.channel = config.CHANNEL
        self.session = self.open_socket()
        self.counter = 0
        self.counter_reset = config.COUNTER_RESET
        self.periodic_message = config.PERIODIC_MESSAGE
        status, msg = self.join()

        if status:
            print(bobby())
            print(msg)
            print_divider()
        else:
            print('BEEP BOOP - Task failed successfully!')
            exit()

    def open_socket(self):
        session = socket.socket()
        session.connect((self.host, self.port))
        session.sendall(b('PASS ' + self.oauth + '\r\n'))
        session.sendall(b('NICK ' + self.bot_name + '\r\n'))
        session.sendall(b('CAP REQ :twitch.tv/commands' + '\r\n'))
        session.sendall(b('CAP REQ :twitch.tv/tags' + '\r\n'))
        session.sendall(b('CAP REQ :twitch.tv/membership' + '\r\n'))
        session.sendall(b('JOIN #' + self.channel + '\r\n'))
        return session

    def join(self):
        """Joins a chatroom / channel."""
        try:
            read_buffer = b''
            loading = True
            while loading:
                read_buffer = read_buffer + self.session.recv(1024)
                tmp = read_buffer.split(b'\n')
                read_buffer = tmp.pop()
                for line in tmp:
                    loading = END in line

            return True, f"{Color.OKBLUE}Sucessfully joined {config.CHANNEL}'s chat.{Color.ENDC}"  # noqa: E501, E999
        except Exception as e:
            # Genereic Exception is fine for now
            return False, e

    def send_message(self, msg):
        """Sends a message.

        Args:
            msg (string): Message to send.
        """
        try:
            ts = str_timestamp()
            _msg = b('PRIVMSG #' + config.CHANNEL + ' :' + msg + '\r\n')
            self.session.sendall(_msg)
            print(f'[{ts}] bobby > : {msg}')
            return True
        except Exception as e:
            # Genereic Exception is fine for now
            return False, e

    def run(
        self,
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
            read_buffer (string): The read_buffer, usually empty string.
            file_name (string): Name of file created.
            path (string): Path to chatlogs, defaults to dir `chatlogs`.
            print_flag (bool): Determines if print the messages.
        """
        self.counter = self.counter + 1
        read_buffer = read_buffer + self.session.recv(1024)
        tmp = read_buffer.split(b'\n')
        read_buffer = tmp.pop()
        contains_emote = False
        emotes = load_emotes()
        responses = load_responses()
        bad_words = load_bad_words()

        with open(path + '/' + file_name, 'a+') as f:
            for line in tmp:
                contains_emote = check_emotes(line, emotes)
                user = get_username(line, contains_emote)
                msg = get_message(line, contains_emote)
                ts = str_timestamp()

                # Checks for faul language and immediately bans the user
                _words = line.split()
                for word in _words:
                    if word in bad_words:
                        _msg = b('PRIVMSG #' + ' /ban ' + user + '\r\n')
                        self.session.sendall(_msg)

                # Twitch will ping every bot once every 5 min with a msg that
                # contains the string `PING`, the bot needs to respond with
                # the same message but with `PONG` instead.
                if 'PING' in msg:
                    msg = msg.replace('PING', 'PONG')
                    self.session.sendall(b(msg))

                elif print_flag and msg != '' and user != '':
                    print(f'{random_color()}[{ts}] {user} < : {msg}{Color.ENDC}')  # noqa: E501
                    f.write(f'[{ts}] {user} < : {msg} \n')

                # Responses
                try:
                    if msg[0] == '!' and responses.get(msg):
                        _msg = f'@{user} {responses.get(msg)}'
                        self.send_message(_msg)
                        f.write(f'[{ts}] {self.bot_name} > : {_msg} \n')
                except IndexError:
                    pass

                # Roll defaults to 100
                if '!roll' in msg:
                    try:
                        value = random.randrange(100)
                        _msg = f'@{user} rolled {value} out of {100}! 🎲'
                        self.send_message(_msg)
                        f.write(f'[{ts}] {self.bot_name} > : {_msg} \n')
                    except IndexError:
                        pass

                if self.counter == self.counter_reset:
                    self.counter = 0
                    self.send_message(self.periodic_message)


def get_username(line, emote):
    """
    Returns the username.

    Args:
        line (binary): Line which we parse.
        emote (bool): Flag to determine if there is a emote in the line.
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
        line (binary): Line which we parse.
        emote (bool):  Flag to determine if there is a emote in the line.
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


def load_responses(file_name='responses.txt'):
    """Load responses for chat commands such as `!rank`."""
    responses = dict()
    with open(file_name) as f:
        for rows in f:
            row = rows.split(',', maxsplit=1)
            responses[row[0]] = str(row[1]).strip()

    return responses


def load_bad_words(file_name='bannable_words.txt'):
    """Load faul words"""
    bad_words = []
    with open(file_name) as f:
        for word in f:
            bad_words.append(str(word).strip())

    return bad_words
