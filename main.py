import time

import pygame as pg
import sympy as sp

WINDOW_DIMS = (800, 600)
CELL_DIMS = (20, 20)
CELL_COUNT = (WINDOW_DIMS[0] // CELL_DIMS[0],
              WINDOW_DIMS[1] // CELL_DIMS[1])
TICKS_PER_SEC = 1
BG_COLOR = (64, 64, 64)
CELL_ACTIVE_COLOR = (215, 215, 215)
CELL_INACTIVE_COLOR = (0, 0, 0)
CELL_PADDING = 1

pg.init()

WIN = pg.display.set_mode(WINDOW_DIMS)
pg.display.set_caption('Game of Life in Pygame')


class cell:
    def __init__(self, coords, active=False, size=CELL_DIMS):
        self.coords = coords
        self.active = active
        self.size = size


class board:
    cells = [[]]

    def __init__(self, size):
        for i in range(size[0]):
            temp_list = []

            for j in range(size[1]):
                temp_list.append(cell((i, j)))

            self.cells.append(temp_list)

    def draw(self, window):
        for i in self.cells:
            for j in i:
                cell_color = CELL_ACTIVE_COLOR if j.active else CELL_INACTIVE_COLOR
                cell_properties = (
                    j.coords[0] * CELL_DIMS[0] + CELL_PADDING,
                    j.coords[1] * CELL_DIMS[1] + CELL_PADDING,
                    CELL_DIMS[0] - 2 * CELL_PADDING,
                    CELL_DIMS[1] - 2 * CELL_PADDING
                )
                pg.draw.rect(window, cell_color, cell_properties)


if __name__ == '__main__':
    run = True

    timer_start = time.time()
    time_per_tickrate = 1 / TICKS_PER_SEC

    WIN.fill(BG_COLOR)
    game_board = board(CELL_COUNT)
    game_board.draw(WIN)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
    pg.quit()
