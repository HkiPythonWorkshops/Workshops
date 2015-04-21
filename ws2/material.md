# Workshop 2 Material

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

To create the screen, add this the file: 

```python
#screen initialization
screen_size= [840, 480]
screen = pygame.display.set_mode(screen_size)
```

If you try running this, a window will briefly pop up and then exit. That's because our game is initializing and then immediately exiting. 

## MainLoop

The main loop of the game is where we handle all the events happening in the game, like movement, user's key presses, and so on. 

A main loop has a condition that is true until we need to break out from it when the user exits the game. 

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

snake = sprite_sheet.subsurface(sprite_sheet.get_clip())

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

## Move the snake
Alright, so just having a snake on the screen isn't so interesting. Let's get it to move.

Let's start by adding coordinates and speed for the snake. Add this right inside the MainLoop, before the while loop: 
```python
snake_x = 0
snake_y = 0
speed = 3
```

Then let's change the drawing with **blit** to this: 

```python
snake_y += speed
snake_x += speed
screen.blit(snake, (snake_x,snake_y))
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

## Move the snake

Of course we want to be in control of the snake by ourselves. So let's make the game respond to key presses.

Inside the MainLoop, in the while loop right after the for loop, add this: 

```python
key_pressed = pygame.key.get_pressed()
if key_pressed[pygame.K_UP]:
    snake_y -= speed
elif key_pressed[pygame.K_DOWN]:
    snake_y += speed
elif key_pressed[pygame.K_LEFT]:
    snake_x -= speed
elif key_pressed[pygame.K_RIGHT]:
    snake_x += speed
```

We're getting the keys pressed by the user and moving the snake the appropriate amount in the right direction. 

Now your MainLoop should look like this: 
```python
def MainLoop():
    """This is the Main Loop of the Game"""

    snake_x = 0
    snake_y = 0
    speed = 3

    while True:
        for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                        
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_UP]:
            snake_y -= speed
        elif key_pressed[pygame.K_DOWN]:
            snake_y += speed
        elif key_pressed[pygame.K_LEFT]:
            snake_x -= speed
        elif key_pressed[pygame.K_RIGHT]:
            snake_x += speed
            
        screen.fill((0, 0, 0))
        screen.blit(snake, (snake_x,snake_y))
        pygame.display.update()
        pygame.time.delay(100)
```

Now when you run the game, you should be able to move the snake around with the arrow keys.

Bonus: experiment with the speed, starting coordinates and delay and see how those affect the feeling of moving the snake. 

## Create the level around the snake

## Draw the blip (what snake can eat)
