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
posY = 40
speedY = 0
gravity = 1
speedUpY = 10

while 1:

    ## check game events
    for event in pygame.event.get():
        ### check QUIT event to cleanly shutdown
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONUP or event.type == pygame.KEYUP:
            print("mouse button up")
            speedY = -speedUpY

    ## Change background RGB color
    screen.fill((0,0,0))

    # Draw a circle
    radius = 40
    speedY = speedY + gravity
    posY = (posY + speedY) % 480

    if (posY>=480-radius)or(posY<radius):posY=440;speedY=0

    pygame.draw.circle(screen, (250,0,0), [160, posY], radius)

    ## 	Update portions of the screen for software displays
    pygame.display.update()

    ## Pause the program for an amount of time
    pygame.time.delay(10)
