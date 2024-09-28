import pygame
from circleshape import CircleShape
from static_features import *

class Curser(CircleShape):
    def __init__(self, x, y, player):
        super().__init__(x, y, CURSER_RADIUS)
        self.rotation = 0
        self.timer = 0
        self.player = player
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self, screen):
        if self.player == "player_1":
            pygame.draw.polygon(screen, PLAYER_1_COLOR, self.triangle(), 2)
        if self.player == "player_2":
            pygame.draw.polygon(screen, PLAYER_2_COLOR, self.triangle(), 2)
    
    def update(self, dt):
        keys = pygame.key.get_pressed()

        if self.player == "player_1":
            if keys[pygame.K_LEFT]:
                if self.position.x >= 0:
                    self.move(-dt)
            if keys[pygame.K_RIGHT]:
                if self.position.x <= SCREEN_WIDTH:
                    self.move(dt)
        if self.player == "player_2":
            if keys[pygame.K_a]:
                if self.position.x >= 0:
                    self.move(-dt)
            if keys[pygame.K_d]:
                if self.position.x <= SCREEN_WIDTH:
                    self.move(dt)

    
    def move(self, dt):
        right = pygame.Vector2(1, 0).rotate(self.rotation)
        self.position += right * CURSER_SPEED * dt