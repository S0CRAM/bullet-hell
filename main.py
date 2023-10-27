import pygame

pygame.init()

FramePerSec = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    FramePerSec.tick(60)


def main():
    while True:


        update_game_display()


if __name__ == "__main__":
    main()
