from sense_hat import SenseHat
import random
import time

s = SenseHat()

screen = []
for i in range(64):
    n = i * 4
    screen.append((n,n,n))

while True:
    s.set_pixels(screen)
    s.low_light = not s.low_light
    time.sleep(1)
