import pygame as pyg
import ship
import endless_bg

pyg.init()
screen = pyg.display.set_mode((720,720))
pyg.display.set_caption('UF-ROCKS')

running = True

ship1 = ship.Ship(screen=screen, x=330, y=600, frames=60)

background = endless_bg.Endless_BG(frames=60, screen=screen)

while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False

    background.tick(2)
    background.draw()

    ship1.move()
    ship1.draw()

    pyg.display.update()

pyg.quit()