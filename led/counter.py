import time
from sense_hat import SenseHat

sense = SenseHat()

def get_num(num, alpha):
    c = [255,255,255]
    w = [0,0,0]
    one="0000100000011000000010000000100000001000000010000000100000011100"
    two="0001110000100010000000100000010000001000000100000010000000111110"
    three="0001110000100010000000100000110000000010000000100010001000011100"
    four="0000010000001100000101000010010000111110000001000000010000000100"
    five="0011111000100000001000000011110000000010000000100010001000011100"
    six="0000110000010000001000000011110000100010001000100010001000011100"
    seven="0011111000000010000001000000010000001000000010000001000000010000"
    eight="0001110000100010001000100001110000100010001000100010001000011100"
    nine="0001110000100010001000100010001000011110000000100000010000011000"
    zero="0001110000100010001000100010001000100010001000100010001000011100"
    cur = ""
    if num == 1:
        cur = one
    elif num == 2:
        cur = two
    elif num == 3:
        cur = three
    elif num == 4:
        cur = four
    elif num == 5:
        cur = five
    elif num == 6:
        cur = six
    elif num == 7:
        cur = seven
    elif num == 8:
        cur = eight
    elif num == 9:
        cur = nine
    else:
        cur = zero
    img = []
    for i in range(8):
        for j in range(8):
            if cur[i*8+j] == '1':
                img.append([int(round(float(cc)*alpha, 0)) for cc in c])
            else:
                img.append(w)
    return img

msleep = lambda x: time.sleep(x/100.0)

for n in range(10):
    j = 9-n
    for i in range(30):
        img = get_num(j,i/30.0)
        sense.set_pixels(img)
        msleep(1)
    msleep(40)
    for i in range(20):
        img = get_num(j, (20-i)/20.0)
        sense.set_pixels(img)
        msleep(1)

# from https://github.com/yjlo123/sense/blob/master/counter.py
