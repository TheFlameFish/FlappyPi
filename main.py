# import the pygame module, so you can use it
import pygame
from replit import db

# define a main function
def main():
     
    # initialize the pygame module
    pygame.init()
    # load and set the logo
    logo = pygame.image.load("images/rubix.png")
    pygame.display.set_icon(logo)
    pygame.display.set_caption("  Flappy Pi")
     
    # create a surface on screen that has the size of 240 x 180
    screen = pygame.display.set_mode((300,180))
     
    # define a variable to control the main loop
    running = True
    # Background
    screen.fill((0,100,255))
    # Add the pi
    xPos = 0
    yPos = 0

    xStep = 10
    yStep = 10
    pi = pygame.image.load("images/pi.png")
    screen.blit(pi, (0,0))
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
     
      
# run the main function only if this module is executed as the main script
# (if you import this as a module then nothing is executed)

        # Move the character
        if xPos>screen_width-63 or xPos<0:
          xStep = -xStep
        if yPos>screen_height-40 or yPos<0:
          yStep = -yStep
        xPos

if __name__=="__main__":
    # call the main function
    main()