import pygame 
from root.settings import WIDTH, HEIGHT

class Background:
    def __init__(self, image):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (WIDTH, HEIGHT))