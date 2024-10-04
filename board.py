import pygame
from static_features import *
from cell import Cell

class Board():
    def __init__(self):
        self.board_list = []
        self.create_board()
        self.victory = False
        self.tie = False
        self.counter = 0
    
    def create_board(self):
        for a in range(0, BOARD_WIDTH):
            c_list = []
            for d in range(0, BOARD_HEIGHT):
                c_list.append(Cell(a, d))
            self.board_list.append(c_list)
    
    def playing_piece(self, x_position, player):
        if self.victory == True:
            return None
        for i in range(1, BOARD_WIDTH + 1):
            if x_position > ENDING_X - 70 * i:
                across = BOARD_WIDTH - i
                break
        for i in range(1, BOARD_HEIGHT + 1):
            current_cell = self.board_list[across][BOARD_HEIGHT - i]
            if current_cell.state == None:
                if player == "player_1":
                    color = PLAYER_1_COLOR
                else:
                    color = PLAYER_2_COLOR
                current_cell.state = color
                return current_cell

    
    def winner(self, player):
        print(f"Congradulations: {player}!")
        self.victory = True
    
    def tied_game(self):
        print(f"Tied Game: No Winners!")
        self.tie = True
        
    
    def in_a_row(self, starting_cell, player):
        self.counter += 1
        left_counter = 0
        right_counter = 0
        down_counter = 0
        left_up_counter = 0
        left_down_counter = 0
        right_up_counter = 0
        right_down_counter = 0
        if player == "player_1":
            color = PLAYER_1_COLOR
        else:
            color = PLAYER_2_COLOR
        if starting_cell.column > 0: #Checking left
            left_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "left")
        if starting_cell.column < BOARD_WIDTH - 1:
            #Checking right
            right_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "right")
        if starting_cell.row < BOARD_HEIGHT - 1:
            #Checking down
            down_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "down")
        if starting_cell.column > 0 and starting_cell.row > 0:
            #Checking left and up
            left_up_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "left + up")
        if starting_cell.column > 0 and starting_cell.row < BOARD_HEIGHT - 1:
            #Checking left and down
            left_down_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "left + down")
        if starting_cell.column < BOARD_WIDTH - 1 and starting_cell.row > 0:
            #Checking right and up
            right_up_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "right + up")
        if starting_cell.column < BOARD_WIDTH - 1 and starting_cell.row < BOARD_HEIGHT - 1:
            #Checking right and down
            right_down_counter = self.matching_function(starting_cell.column, starting_cell.row, color, "right + down")
        if  (
            (left_counter + right_counter >= 3) or
            (left_up_counter + right_down_counter >= 3) or
            (left_down_counter + right_up_counter >= 3) or
            (down_counter >= 3)
        ):
            self.winner(player)
        if self.counter == 42:
            self.tied_game()

        
    def matching_function(self, c, r, color, direct):
        counter = 1
        if direct == "left":
            checking_cell = self.board_list[c - 1][r]
            if checking_cell.state != color:
                return 0
            if checking_cell.column <= 0:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter
        if direct == "right":
            checking_cell = self.board_list[c + 1][r]
            if checking_cell.state != color:
                return 0
            if checking_cell.column >= BOARD_WIDTH - 1:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter
        if direct == "down":
            checking_cell = self.board_list[c][r + 1]
            if checking_cell.state != color:
                return 0
            if checking_cell.row >= BOARD_HEIGHT - 1:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter
        if direct == "left + up":
            checking_cell = self.board_list[c - 1][r - 1]
            if checking_cell.state != color:
                return 0
            if checking_cell.column <= 0 or checking_cell.row <= 0:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter
        if direct == "left + down":
            checking_cell = self.board_list[c - 1][r + 1]
            if checking_cell.state != color:
                return 0
            if checking_cell.column <= 0 or checking_cell.row >= BOARD_HEIGHT - 1:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter
        if direct == "right + up":
            checking_cell = self.board_list[c + 1][r - 1]
            if checking_cell.state != color:
                return 0
            if checking_cell.column >= BOARD_WIDTH - 1 or checking_cell.row <= 0:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter
        if direct == "right + down":
            checking_cell = self.board_list[c + 1][r + 1]
            if checking_cell.state != color:
                return 0
            if checking_cell.column >= BOARD_WIDTH - 1 or checking_cell.row >= BOARD_HEIGHT - 1:
                return counter
            counter += self.matching_function(checking_cell.column, checking_cell.row, color, direct)
            return counter