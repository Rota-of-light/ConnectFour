import pygame
from static_features import *
from curser import Curser

def main():
    pygame.init()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    cursers = pygame.sprite.Group()
    Curser.containers = (updatable, cursers)
    print("Let's play Connect Four!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0
    curser2 = Curser(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20, "player_2")
    curser1 = Curser(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 20, "player_1")
    current_player = "player_1"
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for item in updatable:
            item.update(dt)
        screen.fill((0, 0, 0))
        for curser in cursers:
            curser.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()