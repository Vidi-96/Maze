import pygame as pg

from constants import *


class Player:
    def __init__(self):
        self.img = pg.Surface((50, 50))
        self.img.fill("pink")
        self.rect = self.img.get_frect()
        self.position = pg.Vector2(WIN_SIZE) / 2

        self.direction = pg.Vector2()
        self.speed = 250
        self.velocity = pg.Vector2()

    def update(self, keys, dt):
        self.direction.xy = (0, 0)
        if keys[pg.K_w]:
            self.direction.y -= 1
        if keys[pg.K_s]:
            self.direction.y += 1
        if keys[pg.K_a]:
            self.direction.x -= 1
        if keys[pg.K_d]:
            self.direction.x += 1

        if self.direction:
            self.direction.normalize_ip()

        self.velocity = self.direction * self.speed
        self.position += self.velocity * dt

        self.position.x = pg.math.clamp(self.position.x, 0, WIN_WIDTH - self.rect.w)
        self.position.y = pg.math.clamp(self.position.y, 0, WIN_HEIGHT - self.rect.h)
        self.rect.topleft = self.position

    def draw(self, screen):
        screen.blit(self.img, self.rect)
