import pygame as pyg
import ship 
import endless_bg 
import rock

pyg.init()
screen = pyg.display.set_mode((720,720))
pyg.display.set_caption('UF-ROCKS')

running = True

ship1 = ship.Ship(screen=screen, x=330, y=600, frames=60)

background = endless_bg.Endless_BG(frames=60, screen=screen)

rock1 = rock.Rock(screen=screen, frames=60)

obstacles = []

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    background.tick(2)
    background.draw()

    ship1.move()
    ship1.draw()

    rock1.tick()
    if ship1.y == rock1.y and (rock1.x >= ship1.x - 20 and rock1.x <= ship1.x + 60):
        running = False

    rock1.draw()

    pyg.display.update()
