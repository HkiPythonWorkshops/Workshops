import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('pyGame test Window')

background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill((100, 100, 142))

font = pygame.font.Font(None, 42)
text = font.render("Hello, everything seems to be OK", 1, (250, 250, 250))
textpos = text.get_rect()
textpos.centerx = background.get_rect().centerx
textpos.centery = background.get_rect().centery

background.blit(text, textpos)

screen.blit(background, (0, 0))
pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            print("Exiting pyGame..")
            pygame.quit()
            sys.exit()
    screen.blit(background, (0, 0))
    pygame.display.flip()
