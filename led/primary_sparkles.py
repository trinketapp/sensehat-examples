from sense_hat import SenseHat
from random import randint, choice
from time import sleep

sense = SenseHat()
for b in range(255):
    x = randint(0, 7)
    y = randint(0, 7)
    r = choice([0,255])
    g = choice([0,255])
    b = choice([0,255])
    sense.set_pixel(x, y, r,g, b)
    print(b)
    # input()
print("end")
