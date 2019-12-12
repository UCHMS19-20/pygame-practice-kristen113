import sys
import pygame

# Initialize pygame so it runs in the background and manages things
pygame.init()

# Make colors
red = pygame.Color(150, 5, 0)

# Create a display. Size must be a tuple, which is why it's in parentheses
screen = pygame.display.set_mode( (400, 300) )

# Main loop. Your game would go inside this loop
while True:
    # do something for each event in the event queue (list of things that happen)
    for event in pygame.event.get():
        # Check to see if the current event is a QUIT event
        print(event)
        if event.type == pygame.QUIT:
            # If so, exit the program
            sys.exit()

    # Fill the screen with red
    screen.fill(red)
    pygame.display.flip()