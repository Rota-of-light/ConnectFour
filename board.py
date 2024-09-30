import pygame
from static_features import *
from cell import Cell

class Board():
    def __init__(self):
        self.board_list = []
        self.create_board()
    
    def create_board(self):
        for a in range(1, 8):
            c_list = []
            for d in range(1, 7):
                c_list.append(Cell(a, d))
            self.board_list.append(c_list)
    
    def in_a_row(self, starting_cell):
        color = starting_cell.state
        if starting_cell.position_x > STARTING_X:
            pass #Checking left
        if starting_cell.position_Y > STARTING_Y:
            pass #Checking up
        if starting_cell.position_x < STARTING_X + 70 * 7:
            pass #Checking right
        if starting_cell.position_Y < STARTING_Y + 70 * 6:
            pass #Checking down
        if starting_cell.position_x > STARTING_X and starting_cell.position_Y > STARTING_Y:
            pass #Checking left and up
        if starting_cell.position_x > STARTING_X and starting_cell.position_Y < STARTING_Y + 70 * 6:
            pass #Checking left and down
        if starting_cell.position_x < STARTING_X + 70 * 7 and starting_cell.position_Y > STARTING_Y:
            pass #Checking right and up
        if starting_cell.position_x < STARTING_X + 70 * 7 and starting_cell.position_Y < STARTING_Y + 70 * 6:
            pass #Checking right and down