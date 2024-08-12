# SPDX-FileCopyrightText: 2018 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

import board
import digitalio
import time
import neopixel

# Color Coding 
#
# COLOR (Red, Green, Blue)

COLORS = (
    (0, 0, 255),
    (0, 255, 0),
    (255, 0, 0),
)

# How many pixels are there ;-)?
num_pixels = 25

# There are three cables going to the LEDS. Ground, Power, and Data.
# You need to select the DATA pin to pogramm the LEDS.
pixels = neopixel.NeoPixel(board.D2, num_pixels, brightness=0.5)


# Infinit while loop, this is the processing loop.
while True:
    for i in range(256):
        pixels.fill((255-i,0,i))
        time.sleep(0.001)
    for i in range(256):
        pixels.fill((0,i,255-i))
        time.sleep(0.001)
    for i in range(256):
        pixels.fill((i,255-i,0))
        time.sleep(0.001)
