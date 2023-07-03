import pygame as pyg
import ship 
import endless_bg 
from rock import Rock
import time
import random as r

pyg.init()
screen = pyg.display.set_mode((720,720))
pyg.display.set_caption('UF-ROCKS')
clock = pyg.time.Clock()

start_time = time.time()

running = True

ship1 = ship.Ship(screen=screen, x=330, y=600)

background = endless_bg.Endless_BG(frames=60, screen=screen)

rocks = [Rock(screen=screen, x=r.randint(20, 700), y=r.randint(-150, 1)) for _ in range(5)]

while running:
    # Closing game 
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    # Timer
    end_time = time.time()
    if abs(start_time - end_time) >= 10:
        rocks.append(Rock(screen=screen, x=r.randint(20, 700), y=r.randint(-150, 1)))
        start_time = time.time()

    # Updates and Logic
    background.tick(2)
    background.draw()
    ship1.move()
    ship1.draw()

    for rock in rocks:
        rock.tick()
        rock.draw()

        if ship1.mask.overlap(rock.mask, (rock.rect.x - ship1.rect.x, rock.rect.y - ship1.rect.y)):
            running = False

    pyg.display.flip()
    clock.tick(60)

