"""
DOC
"""
from toml import load as toml_load, dump as toml_dump
from pyxhook import HookManager


def get_input(inp_stream) -> None:
    # todo get constant input stream
    key = inp_stream.Key
    if key.isalpha():  # gets also other keys that are identified by str (like !=exclam,
        print(inp_stream.Key)


# todo construct expression from keypresses- for example if backspace is perssed, delete last char
def construct_expr():
    ...


hm = HookManager()
# Define the callback to handle keypress events
hm.KeyDown = get_input
# Hook the keyboard
hm.HookKeyboard()

# Start the keyboard hook loop
hm.start()


def correct_word(word: str) -> str:
    # todo try to check keys in proximity
    # todo try to check closest to furthest words
    return ''


def correct_expr(expr: str) -> str:
    # todo try with correct_word()
    # todo check for misuse of wording
    return ''


def predict_word(word: str) -> str:
    # todo predict single word based on context
    return ''


def predict_expr(expr: str) -> str:
    # todo predict whole expression based on context
    return ''


class Corrector:
    def __init__(self, expr: str):
        # todo perhaps update dictionary
        self._words = expr.strip(' ')  # todo also try to strip other chars if typo
        self._suggest_word = [correct_word(cw) for cw in self._words]
        self._suggest_expr = correct_expr(expr)
        self._prediction_word = [predict_word(pw) for pw in self._words]
        self._prediction_expr = predict_word(expr)
        # todo perhaps its not practical to predict words as lists

    def learn_word(self):
        ...

    def learn_expr(self):
        ...
