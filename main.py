import pygame
from static_features import *
from curser import Curser
from curser2 import Curser2
from line import Line
from board import Board
from piece import Piece
import time

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    cursers = pygame.sprite.Group()
    lines = pygame.sprite.Group()
    board = Board()
    Curser.containers = (updatable, cursers)
    Curser2.containers = (updatable, cursers)
    Line.containers = (lines)
    Piece.containers = (drawable)
    starting_x = SCREEN_WIDTH / 2 - 35 - 70 * 3
    starting_y = SCREEN_HEIGHT / 2 + 70 * 3
    for i in range(8):
        wall_i = Line(starting_x, LINE_MAX_HEIGHT, starting_x, starting_y)
        starting_x += 70
    starting_x = SCREEN_WIDTH / 2 - 35 - 70 * 3
    for i in range(6):
        floor_i = Line(starting_x, starting_y, LINE_MAX_WIDTH, starting_y)
        starting_y -= 70
    print("Let's play Connect Four!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    curser2 = Curser2(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20, "player_2", board)
    curser1 = Curser(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20, "player_1", board)
    curser1.other = curser2
    curser2.other = curser1
    white = (255, 255, 255)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or board.victory == True or board.tie == True:  
                if board.victory == True or board.tie == True:
                    time.sleep(5)
                    if board.tie == True:
                        print("GAME OVER")
                    return
                print("GAME OVER")  
                return
        for item in updatable:
            item.update(dt)
        screen.fill((0, 0, 0))
        for line in lines:
            line.draw(screen)
        for curser in cursers:
            curser.draw(screen)
        for item in drawable:
            item.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
    

if __name__ == "__main__":
    main()