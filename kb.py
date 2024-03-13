# Isopad pinout
# Credit: u/bomtarnes aka The Keyboard Magpie
import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKeyboard
from kmk.scanners.keypad import KeysScanner

# GPIO to key mapping
# fmt: off
_KEY_CFG = [
        board.D29, board.D28, board.D27, board.D26, board.D22, board.D20, board.D23, board.D21,
]


# fmt: on
class KMKKeyboard(_KMKeyboard):
    def __init__(self):
        # create and register the scanner
        self.matrix = KeysScanner(_KEY_CFG)