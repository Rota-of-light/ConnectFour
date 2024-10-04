import pygame
from circleshape import CircleShape
from static_features import *
from board import Board
from cell import Cell
from piece import Piece

class Curser2(CircleShape):
    def __init__(self, x, y, player, board):
        super().__init__(x, y, CURSER_RADIUS)
        self.rotation = 0
        self.board = board
        self.player = player
        self.other = None
        self.current = "player_1"
        self.timer = 20
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        pygame.draw.polygon(screen, PLAYER_2_COLOR, self.triangle(), 2)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()
        self.timer -= 20

        if keys[pygame.K_a]:
            if self.position.x >= 0:
                self.move(-dt)
        if keys[pygame.K_d]:
            if self.position.x <= SCREEN_WIDTH:
                self.move(dt)
        if keys[pygame.K_SPACE]:
            if self.position.x > STARTING_X - 35 and self.position.x < ENDING_X:
                if self.current == "player_2":
                    self.play()
        
    def play(self):
        if self.timer > 0:
            return
        self.timer = 500
        cell = self.board.playing_piece(self.position.x, self.player)
        if cell is not None:
            self.place_piece(cell)
            self.switch_players()
    
    def place_piece(self, cell):
        new_piece = Piece(self.position.y, cell.position_x, cell.position_y, self.player)
        self.board.in_a_row(cell, self.player)

    def switch_players(self):
        self.current = "player_1"
        self.other.current = "player_1"
        


    
    def move(self, dt):
        right = pygame.Vector2(1, 0).rotate(self.rotation)
        self.position += right * CURSER_SPEED * dt