#!/usr/bin/python

"""
desktop.sexy, inspired by rms.sexy

To 
"""

# To space out the background changes
from time import sleep
from os import system

counter = 0

while True:
    sleep(5)
    system("feh --bg-fill ~/desktop.sexy/" + str(counter) + ".jpg")
    counter += 1
    if counter > 142:
        counter = 0
