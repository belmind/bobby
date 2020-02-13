import config

from utils import print_divider

END = b'End of /NAMES list'


def join_chat(s):
    try:
        read_buffer = b''
        loading = True
        while loading:
            print_divider()
            read_buffer = read_buffer + s.recv(1024)
            tmp = read_buffer.split(b'\n')
            read_buffer = tmp.pop()
            for line in tmp:
                print(line.strip())
                loading = END in line

        print_divider()

        return True, "Sucessfully joined {}'s the room.".format(config.CHANNEL)

    except Exception as e:
        # Genereic Exception is fine for now
        return False, e
