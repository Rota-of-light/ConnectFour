import pygame
from static_features import *

class Cell():
    def __init__(self, across, down):
        self.state = None
        self.column = across
        self.row = down
        self.position_x = STARTING_X + (70 * across)
        self.position_y = STARTING_Y + (70 * down)
    
    '''def check_for_four(self, previous_cell):
        if previous_cell.state == self.state:
            count = 1

            count += .check_for_four()'''

