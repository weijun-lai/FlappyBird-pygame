import pygame
import random
import sys

## 	Initialize the display module
pygame.init()
## 	Initialize a window or screen for display
screen = pygame.display.set_mode((640, 480))

## caption of pygame windows frame
pygame.display.set_caption("Example code for loading sound")

sound = pygame.mixer.music.load('assets/sound/song.wav')
pygame.mixer.music.play()

while 1:

    ## check game events
    for event in pygame.event.get():
        ### check QUIT event to cleanly shutdown
        if event.type == pygame.QUIT:
            sys.exit()

    ## Change background RGB color
    screen.fill((50,130,255))

    ## 	Update portions of the screen for software displays
    pygame.display.update()

    ## Pause the program for an amount of time
    pygame.time.delay(100)
