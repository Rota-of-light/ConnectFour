import pygame
from static_features import *

class Line(pygame.sprite.Sprite):
    def __init__(self, x1, y1, x2, y2):
        # we will be using this later
        if hasattr(self, "containers"):
            super().__init__(self.containers)
        else:
            super().__init__()

        self.position_start = pygame.Vector2(x1, y1)
        self.position_end = pygame.Vector2(x2, y2)
        self.width = 5
    
    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.line(screen, white, self.position_start, self.position_end, self.width)

    def update(self):
        pass
