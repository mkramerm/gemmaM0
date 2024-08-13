# SPDX-FileCopyrightText: 2018 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Imports need.
import board
import digitalio
import time
import neopixel

"""
Shift and breath. I'm shifting pixel around in a ring buffer. 
"""

# Let's have some list fun.
red_active =  [1, 1, 1, 1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,0]
blue_active = [0, 0, 0, 0,0,0,1,1,1,1,1,1,0,0,0,0,0,0,1,1,1,1,1,1,1]

# Gamma correction table.
gamma8 = [
0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,
0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  0,  1,  1,  1,  1,
1,  1,  1,  1,  1,  1,  1,  1,  1,  2,  2,  2,  2,  2,  2,  2,
2,  3,  3,  3,  3,  3,  3,  3,  4,  4,  4,  4,  4,  5,  5,  5,
5,  6,  6,  6,  6,  7,  7,  7,  7,  8,  8,  8,  9,  9,  9, 10,
10, 10, 11, 11, 11, 12, 12, 13, 13, 13, 14, 14, 15, 15, 16, 16,
17, 17, 18, 18, 19, 19, 20, 20, 21, 21, 22, 22, 23, 24, 24, 25,
25, 26, 27, 27, 28, 29, 29, 30, 31, 32, 32, 33, 34, 35, 35, 36,
37, 38, 39, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 50,
51, 52, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 66, 67, 68,
69, 70, 72, 73, 74, 75, 77, 78, 79, 81, 82, 83, 85, 86, 87, 89,
90, 92, 93, 95, 96, 98, 99,101,102,104,105,107,109,110,112,114,
115,117,119,120,122,124,126,127,129,131,133,135,137,138,140,142,
144,146,148,150,152,154,156,158,160,162,164,167,169,171,173,175,
177,180,182,184,186,189,191,193,196,198,200,203,205,208,210,213,
215,218,220,223,225,228,231,233,236,239,241,244,247,249,252,255]


# How many pixels are there ;-)?
num_pixels = 25

# There are three cables going to the LEDS. Ground, Power, and Data.
# You need to select the DATA pin to pogramm the LEDS.
pixels = neopixel.NeoPixel(board.D2, num_pixels, brightness=1)


# Intial conditions.
gain = 0
up = 1


# Infinit while loop, this is the processing loop.
while True:
    # Looping over all pixels.
    for i in range(num_pixels):
        pixels[i] = (gamma8[gain],gamma8[200]*red_active[i],gamma8[180]*blue_active[i])
    time.sleep(0.011)

    # Simple trick to do a ring buffer.
    tmp = red_active.pop(0)
    red_active.append(tmp)
    tmp = blue_active.pop(0)
    blue_active.append(tmp)      


    ## Ramping up and down the gain using a state machine approche.  
    if up == 1:
        gain = gain + 10
        if gain >= 255:
            gain = 255
            up = 0
    if up == 0:
        gain = gain - 10
        if gain <= 0:
            gain = 0
            up = 1
