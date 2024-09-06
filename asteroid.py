import random

import pygame

from circleshape import CircleShape
from constants import *


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            color="white",
            center=self.position,
            radius=self.radius,
            width=3,
        )

    def update(self, dt):
        self.position += dt * self.velocity

    def split(self):
        self.kill()

        def create_splitted_asteroid(radius, angle):
            asteroid_splitted = Asteroid(*self.position, radius)
            new_velocity = self.velocity.rotate(angle)
            asteroid_splitted.velocity = new_velocity * INCREASING_VELOCITY_FACTOR
            return asteroid_splitted

        if self.radius > ASTEROID_MIN_RADIUS:
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            random_angle = random.uniform(20, 50)

            # asteroid splitted 1
            create_splitted_asteroid(new_radius, random_angle)

            # asteroid splitted 2
            create_splitted_asteroid(new_radius, -random_angle)
