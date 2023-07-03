import pygame as pyg
import os 

class Rock():
    def __init__(self, screen, frames):
        self.screen = screen
        self.frames = frames
        self.x = 360
        self.y = 20
    
    def draw(self):
        pyg.draw.rect(self.screen, "white", pyg.Rect((self.x,self.y), (15,15)))

    def tick(self):
        if self.y + 5 >= 740:
            self.y = 0
        self.y += 5
    
