import pygame as pyg
from ship import Ship
from endless_bg import Endless_BG
from rock import Rock
import time
import random as r
from controller import Hand_Controller

pyg.init()
screen = pyg.display.set_mode(size=(720,720))
pyg.display.set_caption(title='UF-ROCKS')
clock = pyg.time.Clock()

start_time = time.time()

running = True

ship1 = Ship(screen=screen, x=330, y=600)

background = Endless_BG(frames=60, screen=screen)

rocks = [Rock(screen=screen, x=r.randint(20, 700), y=r.randint(-150, 1)) for _ in range(5)]

hand_controller = Hand_Controller()

while running:
    # Closing game 
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            hand_controller.close_cam()
            running = False

    # Timer
    end_time = time.time()
    if abs(start_time - end_time) >= 10:
        rocks.append(Rock(screen=screen, x=r.randint(20, 700), y=r.randint(-150, 1)))
        start_time = time.time()

    # Updates and Logic
    background.tick(speed=2)
    background.draw()

    hand_controller.detect_hand()
    ship1.rect.x = 720 * hand_controller.get_hand_position()
    ship1.move()
    ship1.draw()

    for rock in rocks:
        rock.tick()
        rock.draw()

        if ship1.mask.overlap(other=rock.mask, offset=(rock.rect.x - ship1.rect.x, rock.rect.y - ship1.rect.y)):
            running = False

    pyg.display.flip()
    clock.tick(60)

