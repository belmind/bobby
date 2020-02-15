import config

from utils import b, str_timestamp, Color

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


        return True, f"{Color.OKBLUE}Sucessfully joined {config.CHANNEL}'s the room.{Color.ENDC}"
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


def read_messages(s, read_buffer, print_flag=False): 
    """
    Listens and reads messages in chat. Will call `respond_to_message`
    when relevant.
    
    Args:
        s - Connection.
        read_buffer (string) - The read_buffer, usually empty string.
        print_flag (bool) - Flag to determine if we should print the messages.
    
    """
    read_buffer = read_buffer + s.recv(1024)
    tmp = read_buffer.split(b'\n')        
    read_buffer = tmp.pop()

    for line in tmp:
        user = get_username(line)
        msg = get_message(line)
        ts = str_timestamp()

        if print_flag:
            print(f'{Color.OKGREEN}[{ts}] {user} < : {msg}{Color.ENDC}'.format(ts, user, msg)) 


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
        return ''

