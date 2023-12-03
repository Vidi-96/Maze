import pygame as pg
from constants import *
from player import Player
from button import Button

pg.init()
screen = pg.display.set_mode(WIN_SIZE)
clock = pg.time.Clock()

player = Player()
start_button = Button(pg.Vector2(WIN_SIZE) / 2)


def main():
    done = False
    while not done:
        dt = clock.tick() / 1000
        keys = pg.key.get_pressed()

        for event in pg.event.get():
            if event.type == pg.QUIT:
                done = True
            start_button.handle_input(event)

        player.update(keys, dt)
        start_button.update()

        screen.fill((40, 40, 40))
        player.draw(screen)
        start_button.draw(screen)

        pg.display.flip()


if __name__ == '__main__':
    main()
    pg.quit()
