print("Starting")
import board
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
from kmk.extensions.media_keys import MediaKeys

usb_hid.enable(boot_device=1)
keyboard.extensions.append(MediaKeys())
keyboard.modules.append(Layers())

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP29,board.GP28,board.GP27,board.GP26,board.GP15,board.GP14,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0)
keyboard.row_pins = (board.GP13,board.GP12,board.GP11,board.GP10,board.GP9)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

_____ = KC.NO
xxxxx = KC.TRNS

keyboard.keymap = [
    #LAYER0
    [
     KC.ESC,   KC.N1,  KC.N2, KC.N3, KC.N4, KC.N5,  KC.N6, KC.N7,   KC.N8,  KC.N9,    KC.N0,  KC.MINS,   KC.EQL, KC.BSPC,  KC.DEL, 
     KC.TAB,    KC.Q,   KC.W,  KC.E,  KC.R,  KC.T,   KC.Y,  KC.U,    KC.I,   KC.O,     KC.P,  KC.LBRC,  KC.RBRC, KC.BSLS, KC.MUTE,
    KC.CAPS,    KC.A,   KC.S,  KC.D,  KC.F,  KC.G,   KC.H,  KC.J,    KC.K,   KC.L,  KC.SCLN,  KC.QUOT,   KC.ENT,   _____, KC.VOLU,
    KC.LSFT,    KC.Z,   KC.X,  KC.C,  KC.V,  KC.B,   KC.N,  KC.M, KC.COMM, KC.DOT,  KC.SLSH,  KC.RSFT,    _____,   KC.UP, KC.VOLD,
    KC.LCLT, KC.LGUI, KC.ALT, _____, _____, _____, KC.SPC, _____,   _____,  _____, KC.MO(1),    _____,  KC.LEFT, KC.DOWN, KC.RGHT,   
    ]
    #LAYER1
    [
     KC.GRV,   KC.F1,  KC.F2, KC.F3, KC.F4, KC.F5,  KC.F6, KC.F7,   KC.F8,  KC.F9,   KC.F10,   KC.F11,   KC.F12,   xxxxx,   xxxxx, 
      xxxxx,    KC.Q,   KC.W,  KC.E,  KC.R,  KC.T,   KC.Y,  KC.U,    KC.I,   KC.O,     KC.P,  KC.LBRC,  KC.RBRC, KC.BSLS, KC.MPLY,
      xxxxx,    KC.A,   KC.S,  KC.D,  KC.F,  KC.G,   KC.H,  KC.J,    KC.K,   KC.L,  KC.SCLN,  KC.QUOT,    xxxxx,   _____,   xxxxx,
      xxxxx,    KC.Z,   KC.X,  KC.C,  KC.V,  KC.B,   KC.N,  KC.M,   xxxxx,  xxxxx,    xxxxx,    xxxxx,    _____, KC.PGUP,   xxxxx,
      xxxxx,   xxxxx,  xxxxx, _____, _____, _____, KC.SPC, _____,   _____,  _____, KC.MO(1),    _____,  KC.HOME, KC.PGDN,  KC.END,   
    ]
]

if __name__ == '__main__':
    keyboard.go()
