import pygame 
class sprite:
    def __init__(self,fname):
        self.img = pygame.image.load(fname)
        self.pa = pygame.PixelArray(self.img)

    def render(self):
        for i in range(self.pa.shape()[0]):
            for j in range(self.pa.shape()[1]):

