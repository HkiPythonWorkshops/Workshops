import pygame
from pygame.locals import *
import sys

def quit_pygame():
    print("Exiting pyGame..")
    pygame.quit()
    sys.exit()


def main():
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('pyGame test Window')

    # Fill background
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((100, 100, 142))

    # Display some text
    font = pygame.font.Font(None, 42)
    text = font.render("Hello, everything seems to be OK", 1, (250, 250, 250))
    textpos = text.get_rect()
    textpos.centerx = background.get_rect().centerx
    background.blit(text, textpos)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_pygame()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    quit_pygame()
        screen.blit(background, (0, 0))
        pygame.display.flip()

if __name__ == '__main__': main()
