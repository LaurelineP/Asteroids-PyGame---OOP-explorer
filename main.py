import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player


def main():
    print("Starting asteroids!")
    print("Screen width:", SCREEN_WIDTH)
    print("Screen height:", SCREEN_HEIGHT)
    window = init_game()
    clock, dt = set_timer()

    # groups creation - reduce perf cost
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    # groups
    player_groups = (drawables, updatables)
    asteroid_groups = (asteroids, *player_groups)

    player = create_player(player_groups)
    set_asteroids_containers(asteroid_groups)
    asteroid_field = create_asteroid_field(updatables)

    groups = {
        "drawables": drawables,
        "updatables": updatables,
        "asteroids": asteroids
    }

    setup_game_launch(window, clock, dt, player, groups)


def init_game() -> pygame.surface.Surface:
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return window


def setup_game_launch(window, clock, dt, player, groups):
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

            for thing in groups['updatables']:
                # apply updates
                thing.update(dt)

            for thing in groups['drawables']:
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


def create_player(containers):
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = containers
    player = Player(x, y)
    return player


def set_asteroids_containers(containers):
    Asteroid.containers = containers


def create_asteroid_field(containers):
    AsteroidField.containers = containers
    asteroid_field = AsteroidField()
    return asteroid_field


if __name__ == "__main__":
    main()
