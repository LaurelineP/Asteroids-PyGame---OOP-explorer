import pygame

from circleshape import CircleShape
from constants import *
from shot import Shot


class Player(CircleShape):

    def __init__(self, x: int, y: int, radius: int):
        super().__init__(x, y, radius)
        self.rotation = 0
        self.timer = 0

    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(
            self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def draw(self, screen):
        super().draw(screen)
        points_list = self.triangle()
        pygame.draw.polygon(
            surface=screen,
            color="white",
            points=points_list,
            width=2
        )

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def move(self, dt):
        # unit vector
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def shoot(self):
        if self.timer <= 0:
            shot = Shot(self.position.x, self.position.y + 20, SHOT_RADIUS)
            shot.velocity = pygame.Vector2(0, 1).rotate(
                self.rotation
            ) * PLAYER_SHOOT_SPEED

            self.timer += PLAYER_SHOOT_COOLDOWN

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.rotate(-dt)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.rotate(dt)

        if keys[pygame.K_w] or keys[pygame.K_UP]:
            self.move(dt)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            self.move(-dt)

        if keys[pygame.K_SPACE]:
            self.shoot()

        self.timer -= dt
