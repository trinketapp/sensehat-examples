# atexit may need to be removed or stubbed
#!/usr/bin/python

from sense_hat import SenseHat
from time import sleep
import atexit 

# init
sense = SenseHat()
sense.set_rotation(180)
sense.low_light = True
atexit.register(sense.clear)

# colors
R = [255,  92,   0] # Red
Y = [255, 255,   0] # Yellow
G = [  0, 255,   0] # Green
B = [  0, 153, 255] # Blue
DR = [x // 2 for x in R] # Dark Red
DY = [x // 2 for x in Y] # Dark Yellow
DG = [x // 2 for x in G] # Dark Green
DB = [x // 2 for x in B] # Dark Blue
E = [186, 145, 105] # Ecru
T = [186,   0, 186] # Tart
C = [ 80,  80,  80] # Cat
N = [  0,   0,   0] # Noir

# sequences
seq_1 = [
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N,
DR, R, E, T, T, C, E, C,
DY, C, T, T, T, N, C, N,
DG, G, T, T, T, C, C, C,
DB, B, E, T, T, T, E, N,
N, N, N, C, N, N, C, N,
N, N, N, N, N, N, N, N
]

seq_2 = [
N, N, N, N, N, N, N, N,
N, N, N, N, N, N, N, N,
R, DR, E, T, T, T, E, N,
Y, DY, T, T, T, C, T, C,
G,  C, T, T, T, N, C, N,
B, DB, E, T, T, C, C, C,
N, N, C, N, N, C, N, N,
N, N, N, N, N, N, N, N
]

# loop
while True:
    sense.set_pixels(seq_1)
    sleep(0.3)
    sense.set_pixels(seq_2)
    sleep(0.3)

# From here: https://github.com/elsamuko/sense/blob/master/nyan/nyan.py
