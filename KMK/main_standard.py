from kb import KMKKeyboard
from kmk.keys import KC
from kmk.modules.layers import Layers

keyboard = KMKKeyboard()

_____ = KC.NO
XXXXX = KC.TRNS

keyboard.modules.append(Layers())

keyboard.keymap = [[                                    #LAYER0
     KC.ESC,   KC.N1,   KC.N2, KC.N3, KC.N4, KC.N5,  KC.N6, KC.N7,   KC.N8,   KC.N9,    KC.N0, KC.MINS,  KC.EQL, KC.BSPC,  KC.DEL, 
     KC.TAB,    KC.Q,    KC.W,  KC.E,  KC.R,  KC.T,   KC.Y,  KC.U,    KC.I,    KC.O,     KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.PSCR,
    KC.CAPS,    KC.A,    KC.S,  KC.D,  KC.F,  KC.G,   KC.H,  KC.J,    KC.K,    KC.L,  KC.SCLN, KC.QUOT,  KC.ENT,   _____, KC.HOME,
    KC.LSFT,    KC.Z,    KC.X,  KC.C,  KC.V,  KC.B,   KC.N,  KC.M, KC.COMM,  KC.DOT,  KC.SLSH,   _____, KC.RSFT,   KC.UP,  KC.END,
    KC.LCLT, KC.LGUI, KC.LALT, _____, _____, _____, KC.SPC, _____,   _____, KC.RALT, KC.MO(1),   _____, KC.LEFT, KC.DOWN, KC.RGHT,
    ],[                                                 #LAYER1
     KC.GRV,   KC.F1,   KC.F2, KC.F3, KC.F4, KC.F5,  KC.F6, KC.F7,   KC.F8,   KC.F9,   KC.F10,  KC.F11,  KC.F12,   xxxxx,  KC.INS, 
      xxxxx,    KC.Q,    KC.W,  KC.E,  KC.R,  KC.T,   KC.Y,  KC.U,    KC.I,    KC.O,     KC.P,   xxxxx,   xxxxx,   xxxxx,   xxxxx,
      xxxxx,    KC.A,    KC.S,  KC.D,  KC.F,  KC.G,   KC.H,  KC.J,    KC.K,    KC.L,    xxxxx,   xxxxx,   xxxxx,   _____, KC.PGUP,
      xxxxx,    KC.Z,    KC.X,  KC.C,  KC.V,  KC.B,   KC.N,  KC.M,   xxxxx,   xxxxx,    xxxxx,   _____,   xxxxx,   xxxxx, KC.PGDN,
      xxxxx,   xxxxx,   xxxxx, _____, _____, _____, KC.SPC, _____,   _____,   _____, KC.MO(1),   _____,   xxxxx,   xxxxx,   xxxxx,
]]

if __name__ == '__main__':
    keyboard.go()