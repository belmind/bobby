
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


def load_emotes(file_name='emotes.txt'):
    emotes = []
    with open(file_name, 'r') as f:
        for line in f:
            emotes.append(line.strip())

    return emotes
