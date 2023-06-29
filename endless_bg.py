import os
import pygame as pyg

class Endless_BG():
    def __init__(self, frames, screen):
        self.frames = frames
        self.screen = screen
        self.bg_image = pyg.image.load(os.getcwd() + "/Resources/Backgrounds/parallax_scrolling_bg.png")
        self.bg_image = pyg.transform.scale(self.bg_image, (720,720),)
        self.bg1 = self.bg_image
        self.bg2 = self.bg_image
        self.bg1_dy = 0
        self.bg2_dy = -720

    def draw(self):
        self.screen.blit(self.bg1,(0,self.bg1_dy))

        self.screen.blit(self.bg2,(0,self.bg2_dy))
            
    
    def tick(self, speed):
        speed = (self.frames * speed) / 60

        self.bg1_dy += (speed)

        self.bg2_dy += (speed)

        if self.bg2_dy == 0:
            self.bg1_dy = 0
            self.bg2_dy = -720





