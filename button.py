import pygame as pg


class Button:
    def __init__(self, position):
        self.idle = pg.Surface((150, 100))
        self.clicked = pg.Surface((150, 100))
        self.idle.fill((255, 120, 203))  # PINK
        self.clicked.fill((128, 50, 128))  # PURPLE

        self.rect = self.idle.get_frect(center=position)
        self.collision_rect = self.rect.copy()
        self.down = False

    def handle_input(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == pg.BUTTON_LEFT:
            if self.rect.collidepoint(event.pos):
                self.down = True
        elif event.type == pg.MOUSEBUTTONUP and event.button == pg.BUTTON_LEFT:
            self.down = False

    def update(self):
        self.rect.topleft = self.collision_rect.topleft
        if self.down:
            self.rect.y += 8

    def draw(self, screen):
        screen.blit(self.clicked if self.down else self.idle, self.rect)
