# SPDX-FileCopyrightText: 2018 Dan Halbert for Adafruit Industries
#
# SPDX-License-Identifier: MIT

# Imports need.
import board
import digitalio
import time
# Notice that you need "adafruit_pixelbuf.mpy" in our LIB
import neopixel


"""
This is a hello world porgramm, let's call it slow blinky. 
"""

# Color Coding 
#
# COLOR (Red, Green, Blue)
COLORS = (
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
)

# How many pixels are there ;-)?
num_pixels = 25

# There are three cables going to the LEDS. Ground, Power, and Data.
# You need to select the DATA pin to pogramm the LEDS.
pixels = neopixel.NeoPixel(board.D2, num_pixels, brightness=1)


# Infinit while loop, this is the processing loop.
while True:
    pixels.fill(COLORS[0])
    time.sleep(1)
    pixels.fill(COLORS[1])
    time.sleep(1)
    pixels.fill(COLORS[2])
    time.sleep(1)