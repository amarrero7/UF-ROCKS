import pygame as pyg
import os

class Ship():

    def __init__(self, screen, x, y, frames):
        self.image = pyg.image.load(os.getcwd() + "/Resources/Ships/spaceship.png")
        self.image = pyg.transform.scale(self.image, (60,60))
        self.screen = screen
        self.frames = frames
        self.x = x
        self.y = y
        self.rect = self.image.get_rect()

    def draw(self):
        self.screen.blit(self.image, (self.x, self.y),) 

    def move(self):
        dt = pyg.time.Clock().tick(self.frames) / 1000

        key = pyg.key.get_pressed()

        if key[pyg.K_a]:
            if self.x - (400 * dt) > -5:
                self.x -= 400 * dt
        if key[pyg.K_d]:
            if self.x + (400 * dt) < 665:
                self.x += 400 * dt
