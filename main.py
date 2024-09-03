import pygame

from constants import *


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    window = init_game()
    setup_game_launch(window)


def init_game():
    pygame.init()
    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return window


def setup_game_launch(window):
    try:
        while True:
            # short circuit if user quits - enable close window btn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User quitted the game")
                    return

                    # change background color
            pygame.Surface.fill(window, color='black')

            # update screen with changes
            pygame.display.flip()
    except KeyboardInterrupt:
        print("Keyboard quitted the game")
        return


if __name__ == "__main__":
    main()
