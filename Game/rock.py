import pygame as pyg
import os 
import random as r

class Rock():
    def __init__(self, screen, frames):
        self.screen = screen
        self.frames = frames
        self.x = r.randint(20,700)
        self.y = 0
    
    def draw(self) -> None:
        pyg.draw.rect(self.screen, "white", pyg.Rect((self.x,self.y), (15,15)))

    def tick(self) -> None:
        if self.y + 5 >= 740:
            self.y = r.randint(-150,0)
            self.x = r.randint(20,700)
        self.y += 5
    
    def collided(self, ship) -> bool:
        if ship.y == self.y and (self.x >= ship.x - 20 and self.x <= ship.x + 60):
            return True
