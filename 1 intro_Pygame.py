import pygame

# initialize pygame
pygame.init()

# define the window size
display_width = 800
display_height = 600

# create display window
display = pygame.display.set_mode((display_width,display_height))

# set a caption
pygame.display.set_caption("NEW GAME!!!!!")

# define FPS with clock
clock = pygame.time.Clock()


# create logic for game to begin and end
ended = False
while not ended:

    # check if game has ended, print events in terminal
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ended = True
        print(event)

    # update screen
    pygame.display.update()

    # set clock to FPS
    clock.tick(60)

# quit pygame and exit program once out of loop
pygame.quit()
quit()
