from sense_hat import SenseHat
import datetime
import time

sense = SenseHat()
now = datetime.datetime.now()

zero = [[0,1,1,0],[1,0,0,1],[1,0,0,1],[0,1,1,0]]
one = [[0,1,1,0],[1,0,1,0],[0,0,1,0],[1,1,1,1]]
two = [[0,1,1,0],[1,0,0,1],[0,0,1,0],[1,1,0,1]]
three = [[1,1,1,1],[0,0,1,1],[0,0,0,1],[1,1,1,1]]
four = [[1,0,0,1],[1,1,1,1],[0,0,0,1],[0,0,0,1]]
five = [[1,1,1,1],[1,0,0,0],[0,1,1,1],[1,1,1,1]]
six = [[0,1,1,0],[1,0,0,0],[1,1,1,1],[1,1,1,1]]
seven = [[1,1,1,1],[0,0,0,1],[0,0,1,0],[0,1,0,0]]
eight = [[1,1,1,0],[1,0,1,1],[1,1,0,1],[0,1,1,1]]
nine = [[1,1,1,1],[1,0,0,1],[1,1,1,1],[0,0,0,1]]

b = [0,0,255]
g = [0,255,0]
p = [255,0,255]
o = [255,150,0]
e = [0,0,0]

def num_to_arr(n):
    if n == 0:
        return zero
    elif n == 1:
        return one
    elif n == 2:
        return two
    elif n == 3:
        return three
    elif n == 4:
        return four
    elif n == 5:
        return five
    elif n == 6:
        return six
    elif n == 7:
        return seven
    elif n == 8:
        return eight
    elif n == 9:
        return nine
    else:
        return zero

hh = now.hour
mm = now.minute
n1 = hh/10
n2 = hh%10
n3 = mm/10
n4 = mm%10
nums = [[n1, n2], [n3, n4]]

img = []
color = [p, g]
for n in nums:
    for i in range(0,4):
        img.extend([color[0] if j == 1 else e for j in num_to_arr(n[0])[i]])
        img.extend([color[1] if j == 1 else e for j in num_to_arr(n[1])[i]])
    color = [b,o]

sense.set_pixels(img)
time.sleep(4)
sense.clear()

#tt = str(hh)+" "+str(mm)
#sense.show_message(tt)

# from https://github.com/yjlo123/sense/blob/master/clock.py
