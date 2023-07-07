import pygame as pyg
import os 
import random as r

class Rock():
    def __init__(self, x, y, screen):
        self.screen = screen
        self.rect = pyg.Rect(x, y, 15, 15)
        self.rect.x = x
        self.rect.y = y
        self.mask = pyg.mask.from_surface(pyg.Surface((15, 15)))
        self.mask.fill()

    def draw(self):
        pyg.draw.rect(self.screen, "white", self.rect)

    def tick(self) -> None:
        if self.rect.y + 8 >= 740:
            self.rect.x = r.randint(20,700)
            self.rect.y = r.randint(-150,1)
        self.rect.y += 8
