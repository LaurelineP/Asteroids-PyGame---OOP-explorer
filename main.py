import pygame

from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    window = init_game()
    clock, dt = set_timer()
    updatable, drawable = create_updatable_and_drawable_groups()
    player = create_player(drawable, updatable)

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

            for thing in player.containers[1]:
                # apply updates
                thing.update(dt)

            # Group encapsulation
            for thing in player.containers[0]:
                # draw shapes
                thing.draw(window)
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


def create_player(updatable, drawable):
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = (updatable, drawable)
    player = Player(x, y)
    return player


def create_updatable_and_drawable_groups():
    drawable = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    return updatable, drawable


if __name__ == "__main__":
    main()
