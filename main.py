from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.combos import Combos, Chord
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

# Layer Tap
SYMBOLS = KC.LT(1, KC.A)
NUMBER  = KC.LT(2, KC.S)
MORESYM = KC.LT(3, KC.E)
MEDIA   = KC.LT(4, KC.O)

combos = Combos()

keyboard = KMKKeyboard()
keyboard.modules.append(combos)
keyboard.modules.append(Layers())
keyboard.extensions.append(MediaKeys())

combos.combos = [
    # Combos are from the documentation
    # https://raw.githubusercontent.com/artseyio/artsey/main/layout%20diagrams/beta.jpg

    # Base Layer Section 0
    Chord((KC.E, KC.O),             KC.B),
    Chord((KC.Y, KC.I, KC.O),       KC.M),
    Chord((KC.E, KC.Y),             KC.C),
    Chord((KC.H, KC.I),             KC.N),
    Chord((KC.A, KC.R, KC.T),       KC.D),
    Chord((KC.E, KC.I, KC.O),       KC.P),
    Chord((KC.A, KC.R),             KC.F),
    Chord((KC.A, KC.R, KC.S),       KC.Q),
    Chord((KC.R, KC.T),             KC.G),
    Chord((KC.Y, KC.I),             KC.U),
    Chord((KC.E, KC.I),             KC.H),
    Chord((KC.R, KC.S),             KC.V),
    Chord((KC.T, KC.S),             KC.J),
    Chord((KC.A, KC.S),             KC.W),
    Chord((KC.Y, KC.O),             KC.K),
    Chord((KC.R, KC.T, KC.S),       KC.X),
    Chord((KC.E, KC.Y, KC.I),       KC.L),
    Chord((KC.A, KC.R, KC.T, KC.S), KC.Z),
    
    # Base Layer Section 1
    Chord((KC.A, KC.Y),             KC.COMMA),
    Chord((KC.R, KC.Y),             KC.QUOTE),
    Chord((KC.A, KC.I),             KC.DOT),
    Chord((KC.T, KC.I),             KC.EXCLAIM),
    Chord((KC.A, KC.O),             KC.SLASH),
    Chord((KC.S, KC.O),             KC.QUESTION),
    
    # Base Layer Section 2
    Chord((KC.E, KC.Y, KC.I, KC.O), KC.SPACE),
    Chord((KC.A, KC.E),             KC.ENTER),
    Chord((KC.R, KC.E),             KC.BACKSPACE),
    Chord((KC.A, KC.R, KC.O),       KC.ESC),
    Chord((KC.R, KC.I),             KC.DEL),
    Chord((KC.A, KC.R, KC.T, KC.O), KC.TAB),

    # Base Layer Section 3
    Chord((KC.S, KC.O),             KC.RCTRL),
    Chord((KC.A, KC.Y, KC.I, KC.O), KC.CAPS),
    Chord((KC.S, KC.Y),             KC.RGUI),
    Chord((KC.R, KC.T, KC.S, KC.E), KC.SHIFT),
    Chord((KC.S, KC.I),             KC.RALT),
    Chord((KC.A, KC.R, KC.T, KC.S, KC.E, KC.Y, KC.I, KC.O), 
                                    KC.F12),
]

keyboard.keymap = [
    
    # BASE LAYER
    # Took me too long to realise tne board is an ARTSEYIO because the main keys are...
    [KC.A, KC.R, KC.T, KC.S, KC.E, KC.Y, KC.I, KC.O],
    
    # SYMBOL LAYER 1
    [KC.TRNS, KC.RSHIFT(KC.N9), KC.LBRACKET, KC.RSHIFT(KC.LBRACKET), KC.TRNS, KC.RSHIFT(KC.N0), KC.RBRACKET, KC.RSHIFT(KC.RBRACKET)],

    # NUMBER LAYER
    [KC.N1, KC.N2, KC.N3, KC.TRNS, KC.N4, KC.N5, KC.N6, KC.TRNS],
    
    # MORE SYMBOLS - MORESYM
    [KC.RSHIFT(KC.N3), KC.GRV, KC.SCOLON, KC.BSLASH, KC.TRNS, KC.AT, KC.MINUS, KC.KP_EQUAL],
    
    # MEDIA
    [KC.MPLY, KC.MUTE, KC.VOLU, KC.F12, KC.MRWD, KC.MFFD, KC.VOLD, KC.TRNS],
    
    # LOCK NAV
    [KC.HOME, KC.UP, KC.END, KC.PGUP, KC.LEFT, KC.DOWN, KC.RIGHT, KC.PGDN]
]

if __name__ == '__main__':
    keyboard.go()