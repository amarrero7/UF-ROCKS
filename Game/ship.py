import pygame as pyg
import os
from rock import Rock

class Ship():

    def __init__(self, screen, x, y):
        self.image = pyg.image.load(os.getcwd() + "/Resources/Ships/spaceship.png")
        self.image = pyg.transform.scale(self.image, (60,60))
        self.screen = screen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.mask = pyg.mask.from_surface(self.image)

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):

        key = pyg.key.get_pressed()

        if key[pyg.K_a]:
            if self.rect.x - 5 >= -5:
                self.rect.x -= 5
        if key[pyg.K_d]:
            if self.rect.x + 5 <= 665:
                self.rect.x += 5

