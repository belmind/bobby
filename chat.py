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


        return True, f"{Color.OKBLUE}Sucessfully joined {config.CHANNEL}'s chat.{Color.ENDC}"
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

    with open(path + '/' + file_name, 'a+') as f:
        for line in tmp:
            user = get_username(line)
            msg = get_message(line)
            ts = str_timestamp()
            # Twitch will ping every bot once every 5 min with a msg that
            # contains the string `PING`, the bot needs to respond with
            # the same message but with `PONG` instead.
            if 'PING' in msg:
                msg = msg.replace('PING', 'PONG')
                s.sendall(b(msg))

            elif print_flag:
                print(f'{random_color()}[{ts}] {user} < : {msg}{Color.ENDC}')

            f.write(f'[{ts}] {user} < : {msg} \n')


def get_username(line):
    """Returns the username. """
    _line = str(line)
    s = _line.split(':', 2)
    return s[1].split('!', 1)[0]



def get_message(line):
    """Returns the message. """
    _line = str(line)
    s = _line.split(':', 2)
    try:
        return s[2].replace("\\r'", '')
    except Exception as e:
        print(e)
        return ''
