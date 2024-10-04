import pygame
from circleshape import CircleShape
from static_features import *

class Piece(CircleShape):
    def __init__(self, y, cell_x, cell_y, player=None):
        super().__init__(cell_x, cell_y, PIECE_SIZE)
        self.cell_x = cell_x
        self.cell_y = cell_y
        if player == "player_1":
            self.color = PLAYER_1_COLOR
        else:
            self.color = PLAYER_2_COLOR
    
    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius, 2)
    
    def update(self, dt):
        pass
