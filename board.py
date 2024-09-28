import pygame
from static_features import *
from line import Line

class Board():
    def __init__(self):
        self.center_x = SCREEN_WIDTH / 2
        self.center_y = SCREEN_HEIGHT / 2
        self.board_list = []