from sense_hat import SenseHat

from time import sleep

import math

sense = SenseHat()
sense.set_rotation(90)

sense.clear(0, 0, 0,)

while True:
    sense.show_message(" %s F" % round(sense.get_temperature() * 1.8 + 32))
    sleep(1)

# From here: https://github.com/BenIanGifford/sense-hat/blob/master/sense_repeat_temp_f.py
