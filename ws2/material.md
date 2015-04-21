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

## Quit Game

So far we can only interact with the game in one way: exit it. 

In the main loop, we catch all events happening in our game, and react to them. When the event is *QUIT*, which means the user presses the X in the corner, we exit the game.  

```python
for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
```

We can also assign shortcut key to Quit the game to iterate faster. Let's add new check to catch Key events.
```python
for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if pygame.K_q:
                    pygame.quit()
                    sys.exit()
```

Now pressing **q** will also quit the game.  

Now let's finally do something more interesting!

## Draw the snake to the screen
### Load sprite sheet

To get the hero of our game, the snake, to appear on the screen, we need to load an image and create a sprite. In this example we'll use sprite sheets, which are collections of images for a game, e.g. different kinds of textures, items, characters, and so on. 

For the loading to work, you need to have the *pygame_assets* folder inside the same folder as your game!

Let's add this before the main loop: 
```python
character_sheet = pygame.image.load('pygame_assets/creatures.png')
```



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

### Draw snake to screen

To draw the snake on the screen, we'll call the **blit** method, which draws an image on top of another image, in this case our snake on the background. Add this in your MainLoop, inside the while loop but outside the for loop: 



```python
screen.blit(snake, (0,0))
pygame.display.update()
```

So first we draw the snake, and then we update the screen to show the change. 

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
		            elif event.type == pygame.KEYDOWN:
		                if pygame.K_q:
		                    pygame.quit()
		                    sys.exit()

		screen.blit(snake, (0,0))
		pygame.display.update()


if __name__ == "__main__":
    MainLoop()
```

## Move the snake

## Create the level around the snake

## Draw the blip (what snake can eat)
