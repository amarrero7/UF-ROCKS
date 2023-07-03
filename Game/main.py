import pygame as pyg
import ship 
import endless_bg 
import rock
import random as r

pyg.init()
screen = pyg.display.set_mode((720,720))
pyg.display.set_caption('UF-ROCKS')

running = True

ship1 = ship.Ship(screen=screen, x=330, y=600, frames=60)

background = endless_bg.Endless_BG(frames=60, screen=screen)

rocks = []
for i in range(0,5):
    new_rock = rock.Rock(screen=screen, frames=60)
    rocks.append(new_rock)

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    background.tick(2)
    background.draw()

    ship1.move()
    ship1.draw()

    for rock in rocks:
        rock.tick()
        if rock.collided(ship1):
            running = False
        rock.draw()

    pyg.display.update()
