import board
from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.combos import Combos, Chord
from kmk.extensions.media_keys import MediaKeys

combos = Combos()

keyboard = KMKKeyboard()
keyboard.modules.append(Layers())
keyboard.modules.append(combos)
keyboard.extensions.append(MediaKeys())

SYMBOLS = KC.LT(1, KC.A, prefer_hold=True, tap_interrupted=False, tap_time=500)
NUMBER  = KC.LT(2, KC.S, prefer_hold=True, tap_interrupted=False, tap_time=500)
MORESYM = KC.LT(3, KC.E, prefer_hold=True, tap_interrupted=False, tap_time=500)
MEDIA   = KC.LT(4, KC.O, prefer_hold=True, tap_interrupted=False, tap_time=500)

NAV     = KC.TO(5)

combos.combos = [
    # Combos are from the documentation
    # https://raw.githubusercontent.com/artseyio/artsey/main/layout%20diagrams/beta.jpg

    # Nav Layer Select
    Chord((KC.R, KC.E, KC.I),               NAV),


    # Base Layer Section 0
    Chord((MORESYM, MEDIA),                 KC.B),
    Chord((KC.Y, KC.I, MEDIA),              KC.M),
    Chord((MORESYM, KC.Y),                  KC.C),
    Chord((KC.H, KC.I),                     KC.N),
    Chord((SYMBOLS, KC.R, KC.T),            KC.D),
    Chord((MORESYM, KC.I, MEDIA),           KC.P),
    Chord((SYMBOLS, KC.R),                  KC.F),
    Chord((SYMBOLS, KC.R, NUMBER),          KC.Q),
    Chord((KC.R, KC.T),                     KC.G),
    Chord((KC.Y, KC.I),                     KC.U),
    Chord((MORESYM, KC.I),                  KC.H),
    Chord((KC.R, NUMBER),                   KC.V),
    Chord((KC.T, NUMBER),                   KC.J),
    Chord((SYMBOLS, NUMBER),                KC.W),
    Chord((KC.Y, MEDIA),                    KC.K),
    Chord((KC.R, KC.T, NUMBER),             KC.X),
    Chord((MORESYM, KC.Y, KC.I),            KC.L),
    Chord((SYMBOLS, KC.R, KC.T, NUMBER),    KC.Z),
    
    # Base Layer Section 1
    Chord((SYMBOLS, KC.Y),                  KC.COMMA),
    Chord((KC.R, KC.Y),                     KC.QUOTE),
    Chord((SYMBOLS, KC.I),                  KC.DOT),
    Chord((KC.T, KC.I),                     KC.EXCLAIM),
    Chord((SYMBOLS, MEDIA),                 KC.SLASH),
    Chord((NUMBER, MEDIA),                  KC.QUESTION),
    
    # Base Layer Section 2
    Chord((MORESYM, KC.Y, KC.I, MEDIA),     KC.SPACE),
    Chord((SYMBOLS, MORESYM),               KC.ENTER),
    Chord((KC.R, MORESYM),                  KC.BACKSPACE),
    Chord((SYMBOLS, KC.R, MEDIA),           KC.ESC),
    Chord((KC.R, KC.I),                     KC.DEL),
    Chord((SYMBOLS, KC.R, KC.T, MEDIA),     KC.TAB),

    # Base Layer Section 3
    Chord((NUMBER, MEDIA),                  KC.RCTRL),
    Chord((SYMBOLS, KC.Y, KC.I, MEDIA),     KC.CAPS),
    Chord((NUMBER, KC.Y),                   KC.RGUI),
    Chord((KC.R, KC.T, NUMBER, MORESYM),    KC.LSHIFT),
    Chord((NUMBER, KC.I),                   KC.RALT),
    Chord((SYMBOLS, KC.R, KC.T, NUMBER, MORESYM, KC.Y, KC.I, MEDIA), 
                                            KC.F12),
    
    # Number Layer Combos
    Chord((KC.N1, KC.N2),                   KC.N7),
    Chord((KC.N2, KC.N3),                   KC.N8),
    Chord((KC.N4, KC.N5),                   KC.N9),
    Chord((KC.N5, KC.N6),                   KC.N0),
]

keyboard.keymap = [
    
    # BASE LAYER
    # Took me too long to realise tne board is an ARTSEYIO because the main keys are...
    [SYMBOLS, KC.R, KC.T, NUMBER, MORESYM, KC.Y, KC.I, MEDIA],
    
    # SYMBOLS LAYER 1
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
