import pygame
import random
import sys

## 	Initialize the display module
pygame.init()
## 	Initialize a window or screen for display
screen = pygame.display.set_mode((640, 480))

## caption of pygame windows frame
pygame.display.set_caption("Example code for a ball movement")

## ball position and speed
posX = 40
speedX = 5

while 1:

    ## check game events
    for event in pygame.event.get():
        ### check QUIT event to cleanly shutdown
        if event.type == pygame.QUIT:
            sys.exit()

    ## Change background RGB color
    screen.fill((0,0,0))

    # Draw a circle
    radius = 40
    if (posX>640-radius)or(posX<radius):speedX=-speedX
    posX = (posX + speedX) % 640
    pygame.draw.circle(screen, (250,0,0), [posX, 240], radius)

    ## 	Update portions of the screen for software displays
    pygame.display.update()

    ## Pause the program for an amount of time
    pygame.time.delay(10)
