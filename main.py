import pygame

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import *
from player import Player
from shot import Shot


def main():
    window = init_game()
    clock, dt = set_timer()

    # groups creation - reduce perf cost
    drawables = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    # groups containers
    player_groups = (drawables, updatables)
    asteroid_groups = (asteroids, *player_groups)
    shot_groups = (shots, *player_groups)
    entities_groups = {
        "drawables": drawables,
        "updatables": updatables,
        "asteroids": asteroids,
        "shots": shots
    }

    # instantiation and setup
    player = create_player(player_groups)
    set_element_containers(Asteroid, asteroid_groups)
    set_element_containers(Shot, shot_groups)
    create_asteroid_field(updatables)

    setup_game_launch(window, clock, dt, player, entities_groups)


def init_game() -> pygame.surface.Surface:
    pygame.init()

    window = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    return window


def setup_game_launch(window, clock, dt, player, entities_groups):
    try:
        while True:
            # short circuit if user quits - enable close window btn
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    print("User quitted the game.")
                    return

                    # change background color
            pygame.Surface.fill(window, color='black')
            # ----------------------------- CHANGES TO APPLY ----------------------------- #

            for thing in entities_groups['updatables']:
                # apply updates
                thing.update(dt)

            for asteroid in entities_groups["asteroids"]:
                is_colliding = asteroid.is_colliding(player)
                if is_colliding:
                    print('Game over!')
                    return

                for bullet in entities_groups["shots"]:
                    is_bullet_colliding = asteroid.is_colliding(bullet)
                    if is_bullet_colliding:
                        asteroid.split()
                        bullet.kill()

            for thing in entities_groups['drawables']:
                # draw shapes
                thing.draw(window)

            # ------------------------------- UPDATE FRAMES ------------------------------ #

            # update screen with changes
            pygame.display.flip()

            # pausing the loop until 1/60th of a second has passed
            dt = clock.tick(60) / 1000

    except KeyboardInterrupt:
        print("Keyboard quitted the game.")
        return


def set_timer():
    clock = pygame.time.Clock()
    dt = 0
    return clock, dt


# ------------------------- INSTANCES WITH CONTAINERS ------------------------ #

def create_player(containers):
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    Player.containers = containers
    player = Player(x, y, PLAYER_RADIUS)
    return player


def create_asteroid_field(containers):
    AsteroidField.containers = containers
    asteroid_field = AsteroidField()
    return asteroid_field

# ------------------------- UPDATE GROUPS CONTAINERS ------------------------- #


def set_element_containers(Element, containers):
    Element.containers = containers


if __name__ == "__main__":
    main()
