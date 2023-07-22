import pygame as pyg
import os 
import random as r

class Rock():
    def __init__(self, screen, frames):
        self.screen = screen
        self.frames = frames
        self.x = r.randint(20,700)
        self.y = r.randint(-150,1)
    
    def draw(self) -> None:
        pyg.draw.rect(self.screen, "white", pyg.Rect((self.x,self.y), (15,15)))

    def tick(self) -> None:
        self.y += 6
        if self.y + 6 >= 740:
            self.x = r.randint(20,700)
            self.y = r.randint(-150,1)
    
    def collided(self, ship_x, ship_y):
        if ship_y == self.y and (self.x >= ship_x - 20 and self.x <= ship_x + 60):
            return True
