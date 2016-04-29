from sense_hat import SenseHat
import time

sense = SenseHat()

sense.show_letter("J")

for r in (0, 90, 180, 270, 0, 90, 180, 270):
    sense.set_rotation(r)
    time.sleep(0.5)

# From here: https://github.com/raspberrypilearning/getting-started-with-the-sense-hat/blob/master/code/spinning_j.py
