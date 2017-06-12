import pygame
import random
import sys

## 	Initialize the display module
pygame.init()
## 	Initialize a window or screen for display
screen = pygame.display.set_mode((640, 480))

## caption of pygame windows frame
pygame.display.set_caption("Example code for blank windows with text")

## define a text
font = pygame.font.SysFont("Sans", 42)
text = font.render("This is a text", True, (0, 0, 0))

while 1:

    ## check game events
    for event in pygame.event.get():
        ### check QUIT event to cleanly shutdown
        if event.type == pygame.QUIT:
            sys.exit()

    ## Change background RGB color
    screen.fill((50,130,255))

    ## draw a text into screen
    position = (320-text.get_width()//2,240-text.get_height()//2)
    screen.blit(text,position)

    ## 	Update portions of the screen for software displays
    pygame.display.update()

    ## Pause the program for an amount of time
    pygame.time.delay(100)
