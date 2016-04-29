from sense_hat import SenseHat

sense = SenseHat()

sense.clear(0, 0, 0,)

while True:
    from time import sleep
    import math
    sleep(2)
    sense.show_message(" %s prh" % (math.ceil((sense.get_humidity)())))

# From here: https://github.com/BenIanGifford/sense-hat/blob/master/sense_repeat_hum.py
