from sense_hat import SenseHat
import random
import time

s = SenseHat()

i = 0

while True:
    n = i % 255
    print(n)
    screen = [(n,n,n)] * 8\
             + [(n,0,0)] * 8 \
             + [(0,n,0)] * 8 \
             + [(0,0,n)] * 8 \
             + [(n,n,0)] * 8 \
             + [(n,0,n)] * 8 \
             + [(0,n,n)] * 8 \
             + [(n//2,n//2,n//2)] * 8
    s.set_pixels(screen)
    i += 1
    time.sleep(.01)
