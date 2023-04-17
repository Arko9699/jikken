import board

from kmk.kmk_keyboard import KMKKeyboard as _KMKKeyboard
from kmk.scanners import DiodeOrientation
from kmk.extensions.media_keys import MediaKeys

class KMKKeyboard(_KMKKeyboard):
    col_pins = [board.GP29,board.GP28,board.GP27,board.GP26,board.GP15,board.GP14,board.GP8,board.GP7,board.GP6,board.GP5,board.GP4,board.GP3,board.GP2,board.GP1,board.GP0]
    row_pins = [board.GP13,board.GP12,board.GP11,board.GP10,board.GP9]
    diode_orientation = DiodeOrientation.COL2ROW
