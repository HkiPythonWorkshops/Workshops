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
def MainLoop(self):
    """This is the Main Loop of the Game"""
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
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


Now let's finally do something more interesting!

## Draw the snake to the screen

## Move the snake

## Create the level around the snake

## Draw the blip (what snake can eat)
