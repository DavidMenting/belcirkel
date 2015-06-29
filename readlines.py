#!/usr/local/bin/python
import sys

keyphrases = [line.rstrip(' /1e-0123456789\n') for line in open('keyphrase.list')]


while 1:
    try:
        line = sys.stdin.readline()
    except KeyboardInterrupt:
        break

    if not line:
        break

    if line.rstrip('. /1e-0123456789\n') in keyphrases:
      print('match')