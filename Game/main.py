import pygame as pyg
import ship 
import endless_bg 
from rock import Rock
import random as r
import time

pyg.init()
screen = pyg.display.set_mode((720,720))
pyg.display.set_caption('UF-ROCKS')
clock = pyg.time.Clock()

start_time = time.time()

running = True

ship1 = ship.Ship(screen=screen, x=330, y=600, frames=60)

background = endless_bg.Endless_BG(frames=60, screen=screen)

rocks = []
def add_rocks():
    for i in range(0,5):
        new_rock = Rock(screen=screen, frames=60)
        rocks.append(new_rock)
add_rocks()

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    clock.tick(120)

    end_time = time.time()
    if abs(start_time - end_time) >= 10:
        print("10 seconds passed, new rock added")
        time.sleep(0.001)
        rocks.append(Rock(screen=screen, frames=60))
        start_time = time.time()
        
    background.tick(3)
    ship1.move()

    for rock in rocks:
        if rock.collided(ship1.x, ship1.y):
            running = False
        rock.tick()
    background.draw()
    ship1.draw()

    for rock in rocks:
        rock.draw()

    pyg.display.flip()

