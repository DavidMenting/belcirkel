#!/usr/local/bin/python
import sys
import re
from dotstar import Adafruit_DotStar

numpixels = 1 # Number of LEDs in strip

# Here's how to control the strip from any two GPIO pins:
datapin   = 16
clockpin  = 26
strip     = Adafruit_DotStar(numpixels, datapin, clockpin)

strip.begin()
strip.setBrightness(16)
strip.setPixelColor(0,0xFFFF00)
strip.show()

keyphrases = [line.rstrip(' /1e-0123456789\n') for line in open('keyphrase.list')]

while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        strip.setPixelColor(0, 0x000000)
        strip.show()
        break

    if not line:
        break

    if re.match('INFO: cmn_prior.c',line):
        strip.setPixelColor(0, 0x0000FF)

    # Timestamp and log line to a file that shouldn't become too big
    # See if it matches one of the keywords
    if line.rstrip('. /1e-0123456789\n') in keyphrases:
      print('match')
      strip.setPixelColor(0, 0x00FF00)

    strip.show()
