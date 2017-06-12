import pygame
import random
import sys
from math import pi

## 	Initialize the display module
pygame.init()
## 	Initialize a window or screen for display
screen = pygame.display.set_mode((640, 480))

## caption of pygame windows frame
pygame.display.set_caption("Example code for a ball movement with mouse and key events")

## load new image from a file
# background = pygame.image.load('background.bmp').convert()
## copy graphics from one image to another
# screen.blit(background, (0, 0))

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)
backgroundColor = (0,0,0)

# clock = pygame.time.Clock()

## ball position and speed
posX , posY = 40,40
speedX,speedY = 5,5

def changeBackgroudColor():
    global backgroundColor
    ## Change background RGB color
    r=random.randint(0, 255)
    b=random.randint(0, 255)
    g=random.randint(0, 255)
    backgroundColor = (r,b,g)
    
while 1:
    ## check game events
    for event in pygame.event.get():
        ### check QUIT event to cleanly shutdown
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.MOUSEMOTION:
            ## get the mouse cursor position
            print(pygame.mouse.get_pos())
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print("mouse button down")
        elif event.type == pygame.MOUSEBUTTONUP:
            print("mouse button up")
            backgroundColor = (0,0,0)
        elif event.type == pygame.KEYDOWN:
            print("key down:"+str(event.key % 255)+"["+chr(event.key % 255)+"]")
        elif event.type == pygame.KEYUP:
            print("key up:"+str(event.key % 255)+" ["+chr(event.key % 255)+"]")
            backgroundColor = (0,0,0)


    screen.fill(backgroundColor)

    # Draw a circle
    radius = 40
    if (posX>640-radius)or(posX<radius):speedX=-speedX;changeBackgroudColor()
    if (posY>480-radius)or(posY<radius):speedY=-speedY;changeBackgroudColor()
    posX = (posX + speedX) % 640
    posY = (posY + speedY) % 480
    pygame.draw.circle(screen, (250,0,0), [posX, posY], radius)


    ## 	Update the full display Surface to the screen
    # pygame.display.flip()

    ## 	Update portions of the screen for software displays
    pygame.display.update()

    ## Pause the program for an amount of time
    pygame.time.delay(10)
