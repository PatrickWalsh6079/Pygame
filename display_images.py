import pygame

# initialize pygame
pygame.init()

# define the window size
display_width = 1000
display_height = 800

# create display window
display = pygame.display.set_mode((display_width,display_height))

# set a caption
pygame.display.set_caption("NEW GAME!!!!!")

# define RGB colors for display
black = (0,0,0)
white = (255,255,255)


# image to be displayed
game_img = pygame.image.load(r"C:\Users\raleighcoderschool\Desktop\Pygame tutorials\Cartoon-PNG-Pic.png")


# function that loads image onto display
def image(x,y):
    display.blit(game_img, (x,y))
x = (display_width * 0.2)
y = (display_height * 0.03)


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

    # set display color
    display.fill(white)


    # call image function to print on top display
    image(x,y)

    # update screen
    pygame.display.update()

    # set clock to FPS
    clock.tick(60)

# quit pygame and exit program once out of loop
pygame.quit()
quit()