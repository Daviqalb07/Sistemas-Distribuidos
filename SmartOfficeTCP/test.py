from Lampada import *

lamp = Lampada()
lamp.ParseFromString(b'\x08\x00\x10\x02\x18\x01')
lamp.print_fancy()