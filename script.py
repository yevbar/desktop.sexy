from time import sleep
from os import system

while True:
    sleep(3)
    
    system(
        """osascript -e ‘tell application “Finder” to set desktop picture to POSIX file “~/114.jpg”’"""
        )
