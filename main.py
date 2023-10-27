import pygame

pygame.init()

fps = pygame.time.Clock()


def update_game_display():
    pygame.display.update()
    fps.tick(60)


def main():
    while True:


        update_game_display()


if __name__ == "__main__":
    main()
