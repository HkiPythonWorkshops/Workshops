# Workshop 2 Material

PyGame docs are here: [PyGame Doc](http://www.pygame.org/docs/index.html)


### Pre-Requirements
* [Python](https://github.com/HkiPythonWorkshops/Workshops)
* install pygame with **Pip**  
```pip install pygame```
* or see this [doc](http://webprojects.eecs.qmul.ac.uk/fa303/pgs/install.html) (win/linux/osx)


## import and set up pygame

Create a new file and call it e.g. snake.py. 

The first thing we want to do is import PyGame:
```python
import pygame
```

Once we do this, we can set up PyGame: 

```python
import pygame

pygame.init()
```

If you run this, you'll notice it does absolutely nothing by itself just yet.

## Set up the background

To make a game, we need a background or *screen*.

To create the screen, add this to the file: 

```python
#screen initialization
screen_size= [840, 480]
screen = pygame.display.set_mode(screen_size)
```

If you try running this, a window will briefly pop up and then exit. That's because our game is initializing and then immediately exiting. 

## MainLoop

The main loop of the game is where we handle all the events happening in the game, like movement, user's key presses, and so on. 

A main loop has a condition that is true until we need to break out from it when the user exits the game. Let's add this to the end of our file:

```python
def MainLoop():
    """This is the Main Loop of the Game"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                pygame.quit()
                sys.exit()
                
if __name__ == "__main__":
    MainLoop()
```

We also need to import sys so the program will exit cleanly. Add this to the start of the program: 
```python
import sys
```

Now run the game, and the black screen should stay there. 
Bonus: this is a good time to play around with the screen size!

## Quit Game

So far we can only interact with the game in one way: exit it. 

In the main loop, we catch all events happening in our game, and react to them. When the event is *QUIT*, which means the user presses the X in the corner, we exit the game.  

```python
for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
```

Now let's finally do something more interesting!

## Draw the snake to the screen
### Load sprite sheet

To get the hero of our game, the snake, to appear on the screen, we need to load an image and create a sprite. In this example we'll use sprite sheets, which are collections of images for a game, e.g. different kinds of textures, items, characters, and so on. 

For the loading to work, you need to have the *pygame_assets* folder inside the same folder as your game.

Let's add this before the main loop: 
```python
character_sheet = pygame.image.load('pygame_assets/creatures.png')
```
Running this does nothing interesting, yet. It just loads the sprite sheet for us to use. 

### Load tile from sprite sheet

Now we have loaded the sprite sheet, but we haven't actually gotten the snake out of the sheet yet. 

To do that, we have to **clip** from the sheet:

```python
character_sheet.set_clip(pygame.Rect(32 * 5,
                                      32 * 0,
                                      32, 32))

snake = character_sheet.subsurface(character_sheet.get_clip())

```

What we're doing here is give set_clip 4 arguments:
* rect_x/y    (x,y) location where we can find the sprite
* tile_x/y    is the size of the sprite we are going to load (in our case 32x32)

Now run it! And... nothing is still happening that you can see.

Bonus: think of the sprite sheet as a set of coordinates, and the snake is at (5,0). How would you load a sprite from (3, 3) instead and which character is it? 

### Draw snake to screen

To draw the snake on the screen, we'll call the **blit** method, which draws an image on top of another image, in this case our snake on the background. Add this in your MainLoop, inside the while loop but outside the for loop: 

```python
screen.blit(snake, (0,0))
pygame.display.update()
```

So first we draw the snake, and then we update the screen to show the change. If you run the game, you should finally see the snake in the top left corner!

Your game should look something like this now: 
```python
import pygame
import sys

pygame.init()

#screen initialization
screen_size= [840, 480]
screen = pygame.display.set_mode(screen_size)

character_sheet = pygame.image.load('pygame_assets/creatures.png')

character_sheet.set_clip(pygame.Rect(32 * 5,
                                      32 * 0,
                                      32, 32))

snake = character_sheet.subsurface(character_sheet.get_clip())


def MainLoop():
    """This is the Main Loop of the Game"""
    while True:
		for event in pygame.event.get():
		            if event.type == pygame.QUIT:
		                pygame.quit()
		                sys.exit()

		screen.blit(snake, (0,0))
		pygame.display.update()


if __name__ == "__main__":
    MainLoop()
```

## Getting the snake to move
Alright, so just having a snake on the screen isn't so interesting. Let's get it to move.

Let's start by getting the initial coordinates and setting the speed for the snake. Add this right inside the MainLoop, before the while loop: 
```python
snake_position = snake.get_rect()
speed = 3
```

Then let's change the drawing with **blit** to this: 

```python
snake_position.x = snake_position.x + speed
snake_position.y = snake_position.y + speed
screen.blit(snake, snake_position)
```
And finally, after display.update(), let's add a delay: 
```python
pygame.time.delay(100)
```

When you run the game now, you should see the snake move slowly across the screen to the bottom right corner. What we're doing is just changing the location of the snake and then updating the screen. It doesn't look very nice since we're not cleaning up after ourselves though.
So let's add this right before the **blit**: 

```python
screen.fill((0, 0, 0))
```
Now the old images will be removed before the new one is drawn. 

## Move the snake with arrow keys

Of course we want to be in control of the snake by ourselves. So let's make the game respond to key presses instead of always moving by itself.

Inside the MainLoop, in the while loop right after the for loop, add this: 

```python
key_pressed = pygame.key.get_pressed()
if key_pressed[pygame.K_UP]:
    snake_position.y -= speed
elif key_pressed[pygame.K_DOWN]:
    snake_position.y += speed
elif key_pressed[pygame.K_LEFT]:
    snake_position.x -= speed
elif key_pressed[pygame.K_RIGHT]:
    snake_position.x += speed
```

And remove the lines 
```python
snake_position.x = snake_position.x + speed
snake_position.y = snake_position.y + speed
```

We're getting the keys pressed by the user and moving the snake the appropriate amount in the right direction. 

Now your MainLoop should look like this: 
```python
def MainLoop():
    """This is the Main Loop of the Game"""

    snake_position = snake.get_rect()
    speed = 3

    while True:
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            snake_position.y = snake_position.y - speed
        elif key_pressed[pygame.K_DOWN]:
            snake_position.y = snake_position.y + speed
        elif key_pressed[pygame.K_LEFT]:
            snake_position.x = snake_position.x - speed
        elif key_pressed[pygame.K_RIGHT]:
            snake_position.x = snake_position.x + speed

        screen.fill((0, 0, 0))
        screen.blit(snake, snake_position)
        pygame.display.update()
        pygame.time.delay(100)
```

Now when you run the game, you should be able to move the snake around with the arrow keys.

Bonus: experiment with the speed, starting coordinates (by setting snake_position.x and snake_position.y before the while loop) and delay, and see how those affect the feeling of moving the snake. 


## Create the level around the snake

Alright, now we have a moving snake. Let's create something else in the game!

First, let's make the background a nice green color. Change the fill color of our background in the main loop:

```python
screen.fill((0, 100, 0))
```


## Draw a flower that the snake can eat

Next, let's load a flower from the second sprite sheet. Let's go through the same steps as for the snake: 

```python
plants_sheet = pygame.image.load('pygame_assets/plants.png')
plants_sheet.set_clip(pygame.Rect(32 * 3,
                                      32 * 0,
                                      32, 32))

flower = plants_sheet.subsurface(plants_sheet.get_clip())
```

Now let's draw the flower by adding this in the MainLoop
```python
flower_position = flower.get_rect()
flower_position.x = 400
flower_position.y = 300

screen.blit(flower, flower_position)
```
Now we should have a flower in the game as well as the snake. What happens when the snakes tries to eat the flower? 


## Taking our game to the next level

Before we get to collisions, let's tidy up our game. Let's use good coding practices like using variables instead of numbers inside the code, and let's move some code into functions so it won't clutter up our MainLoop. Otherwise the game will stay the same. See the file [pygame_snake.py](pygame_snake.py).

We've also created the GameObject class and made the snake and flower GameObjects. Why? So that it will be easier to handle each item in the game as an object, and so that we can customize the movement etc for each item. 

## Collisions

Alright, now we're ready to tackle the idea of collisions. When two objects in the game meet, such as the snake and the flower, they **collide**. Usually some sort of event is triggered when a collision happens. 

In [pygame_snake.py](pygame_snake.py) you can see that after handling each movement, we check for collisions after movement. But for collisions to work, we have to make the snake and flower into GameObjects first: 

So before the main loop, we define a new class:

```python
class GameObject(object):
    """
    Let's have a simple GameObject to hold our surface (sprite)
    and the Rect that we can move around
    """
    def __init__(self, surface, rect):
        if surface: self.surface = surface
        if rect: self.rect = rect
```

Now let's make our snake and flower into game objects after loading them: 

```python
snake_c = GameObject(snake, snake.get_rect())
flower_c = GameObject(flower, flower.get_rect())

# set Rect positions
snake_position = snake_c.rect
flower_position = flower_c.rect
```

Now we can use the positions like we have so far and also check for collisions.

```python
if pygame.sprite.collide_rect(snake_c, flower_c):
     # if we have collision, move flower to new random position and update score
     flower_position.x = random.randint(0, screen.get_width()-20)
     flower_position.y = random.randint(0, screen.get_height()-20)
     score += 1
```

We also need to add an import for the random library and initialize score as 0 before our main loop.
```python
import random

score = 0
```

PyGame offers us a ready-made function for checking if two objects have collided. If that happens, we change the location of the flower to a new random location.

## Tasks

1. Print the score of the game to console when the game quits.
2. Increase the speed of the snake whenever he eats a flower. 
3. Add a check to see if the snake goes out of the screen and make it so the snake can't go out of the view. 
4. Make the flower move around randomly every 10 seconds so it's harder to catch.

## All done? 

Have a look at more PyGame tutorials and projects: 
* [PyGame Tutorials](http://pygame.org/wiki/tutorials)
* [PyGame Tutorial by Nerd Paradise](http://www.nerdparadise.com/tech/python/pygame/basics/part1/)
* [Simple Snake by sparkon](https://github.com/sparkon/ss_simple_snake_py)
* [Pacman with PyGame](http://www.learningpython.com/2006/03/12/creating-a-game-in-python-using-pygame-part-one/)
  
If you are interested to create your first *"real"* game, then the suggestion is to use framework that can handle most things out-of-the-box like [Cocos2d](http://en.wikipedia.org/wiki/Cocos2d) (see the pyton docs [here](http://python.cocos2d.org/doc.html)]
