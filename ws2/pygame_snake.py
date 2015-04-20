import pygame
import sys
import os
import random
import time

# Sprites from: http://opengameart.org/content/goblin-camp-graphics
ASSET_DIR = 'pygame_assets/'
CREATURE_SPRITE_SHEET = 'creatures.png'
PLANTS_SPRITE_SHEET='plants.png'
# See ASSET_DIR/tilesetV2.dat
SPRITE_TILE_WIDTH=32
SPRITE_TILE_HEIGHT=32
# the x,y number of the tile we want to load (from the tilesheet)
SNAKE_SPRITE_NUM_X = 5
SNAKE_SPRITE_NUM_Y = 0
FLOWER_SPRITE_NUM_X = 3
FLOWER_SPRITE_NUM_Y = 0

############## TESTING
def draw_text(background, text, location=(10,10)):
    fill_background(background)
    blit_background(background, text, random_object_location(background, text))

def render_text(font, text_msg, color=(250, 250, 250)):
    text = font.render(text_msg, 1, color)
    return text

def setup_font(size):
    font = pygame.font.Font(None, size)
    return font
############## TESTING

def setup_pygame(screen_y, screen_x, window_title):
    pygame.init()
    screen = pygame.display.set_mode((screen_y, screen_x))
    pygame.display.set_caption(window_title)
    return screen

def setup_background(screen, colors=()):
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(colors)
    screen.blit(background, (0, 0))
    pygame.display.flip()
    return background

def quit_pygame():
    print("Exiting pyGame..")
    pygame.quit()
    sys.exit()

def fill_background(background):
    background.fill(background.get_at((0,0)))

def blit_background(background, source, dest):
    background.blit(source, dest)

def random_object_location(background, obj):
    obj_rect = obj.get_rect()
    rand_width = random.randint(0, background.get_width())
    rand_height = random.randint(0, background.get_height())
    obj_rect.centerx = rand_width
    obj_rect.centery = rand_height

    print("spawned random place for object (height: %d, width: %d)" % (rand_height, rand_width))
    return obj_rect


def load_sprite_sheet(sheet_name):
    print("Loading Spritesheet: %s" % sheet_name)
    return pygame.image.load(ASSET_DIR+sheet_name)

def load_sprite_from_sheet(sprite_sheet, sprite_num_x, sprite_num_y):
    """
    Load Rect from the sprite_sheet
    pygame.image.set_clip takes 4 arguments:
        rect_x/y    (x,y) location where we can find the sprite
        tile_x/y    is the size of the sprite we are going to load (in our case 32x32)
    """
    # rect_x, rect_y
    # len_x, len_y
    sprite_sheet.set_clip(pygame.Rect(SPRITE_TILE_WIDTH * sprite_num_x,
                                      SPRITE_TILE_HEIGHT * sprite_num_y,
                                      32, 32))
    return sprite_sheet.subsurface(sprite_sheet.get_clip())
    
def main():
    screen = setup_pygame(800, 600, 'my awesume pygame thingy')
    background = setup_background(screen, (0, 100, 0))

    # Load the spritesheet where we load the images
    creature_sheet = load_sprite_sheet(CREATURE_SPRITE_SHEET)
    plants_sheet = load_sprite_sheet(PLANTS_SPRITE_SHEET)

    # load the tile we want to draw to screen
    snake = load_sprite_from_sheet(creature_sheet, SNAKE_SPRITE_NUM_X, SNAKE_SPRITE_NUM_Y)
    flower = load_sprite_from_sheet(plants_sheet, FLOWER_SPRITE_NUM_X, FLOWER_SPRITE_NUM_Y)

    # MainLoop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit_pygame()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if pygame.key.get_pressed()[pygame.K_LCTRL] and event.key == pygame.K_q:
                    quit_pygame()
        screen.blit(background, (0, 0))
        # Draw the snake+flower
        screen.blit(snake, (0,0))
        screen.blit(flower,(42,42))

        # Update screen
        pygame.display.update()

if __name__ == '__main__':
    main()
