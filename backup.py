from kmk.modules.oneshot import OneShot

oneshot = OneShot()

keyboard.modules.append(oneshot)

# One Shot Mod
KC_OSSHIFT = KC.OS(KC.RSHIFT, tap_time=None)


combos.combos = [
    # Base Layer Section 3
    Chord((KC.R, KC.T, KC.S, KC.E), KC_OSSHIFT),
    
    # NUMBER LAYER
    Chord((KC.N4, KC.N5),           KC.N9),
    Chord((KC.N5, KC.N6),           KC.N0),
    Chord((KC.N1, KC.N2),           KC.N7),
    Chord((KC.N2, KC.N3),           KC.N8),

    # LOCK NAV
    Chord((KC.E, KC.R, KC.I),       KC.TG(5)),
    Chord((KC.LEFT, KC.DOWN, KC.RIGHT), 
                                    KC.TG(0)),

]

keyboard.keymap = [
    # BASE LAYER
    # Took me too long to realise tne board is an ARTSEYIO because the main keys are...
    [SYMBOLS, KC.R, KC.T, NUMBER, MORESYM, KC.Y, KC.I, MEDIA],
]

if __name__ == '__main__':
    keyboard.go()