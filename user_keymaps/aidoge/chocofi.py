from kb import KMKKeyboard

from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.modules.combos import Combos, Chord

combos = Combos()
keyboard = KMKKeyboard()
keyboard.debug_enabled = True

# TODO Comment one of these on each side
split_side = SplitSide.LEFT
#split_side = SplitSide.RIGHT
split = Split(split_type=SplitType.UART, split_side=split_side)

layers = Layers()

keyboard.modules = [layers, split, combos]
#
# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO

LOWER = KC.MO(1)
RAISE = KC.MO(2)
ADJUST = KC.LT(3, KC.SPC)

combos.combos = [
    Chord((3, 4), KC.ESC, match_coord=True)
]

keyboard.keymap = [
    [  #QWERTY
        XXXXXXX,    KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,   KC.P,  KC.BSPC,\
        XXXXXXX,   KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN, KC.QUOT,\
        XXXXXXX,   KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH, KC.RSFT,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #LOWER
        XXXXXXX,   KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                         KC.N6,   KC.N7,  KC.N8,   KC.N9,   KC.N0, KC.BSPC,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.LEFT, KC.DOWN, KC.UP,   KC.RIGHT, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #RAISE
        KC.ESC, KC.EXLM,   KC.AT, KC.HASH,  KC.DLR, KC.PERC,                         KC.CIRC, KC.AMPR, KC.ASTR, KC.LPRN, KC.RPRN, KC.BSPC,\
        KC.LCTL, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.MINS,  KC.EQL, KC.LCBR, KC.RCBR, KC.PIPE,  KC.GRV,\
        KC.LSFT, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        KC.UNDS, KC.PLUS, KC.LBRC, KC.RBRC, KC.BSLS, KC.TILD,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ],
    [  #ADJUST
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,\
                                            KC.LGUI,   LOWER,  ADJUST,     KC.ENT,   RAISE,  KC.RALT,
    ]
]

if __name__ == '__main__':
    keyboard.go()
