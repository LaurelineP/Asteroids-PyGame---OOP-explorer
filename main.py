import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    window = init_game()
    clock, dt = set_timer()
    player = create_player()

    setup_game_launch(window, clock, dt, player)


def init_game() -> pygame.surface.Surface:
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return window


def setup_game_launch(window, clock, dt, player):
    try:
        while True:
            # short circuit if user quits - enable close window btn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User quitted the game")
                    return

                    # change background color
            pygame.Surface.fill(window, color='black')
            # ----------------------------- CHANGES TO APPLY ----------------------------- #

            # draw shape
            player.draw(window)

            # rotate & move - self position
            player.update(dt)

            # ------------------------------- UPDATE FRAMES ------------------------------ #

            # update screen with changes
            pygame.display.flip()

            # pausing the loop until 1/60th of a second has passed
            dt = clock.tick(60) / 1000

    except KeyboardInterrupt:
        print("Keyboard quitted the game")
        return


def set_timer():
    clock = pygame.time.Clock()
    dt = 0
    return clock, dt


def create_player():
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player = Player(x, y)
    return player


if __name__ == "__main__":
    main()
