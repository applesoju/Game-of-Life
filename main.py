import time

import pygame as pg
import sympy as sp
# test
WINDOW_DIMS = (1920, 1080)
MENU_WIDTH = 200
CELL_DIMS = (20, 20)
CELL_COUNT = ((WINDOW_DIMS[0] - MENU_WIDTH) // CELL_DIMS[0],
              WINDOW_DIMS[1] // CELL_DIMS[1])
TICKS_PER_SEC = 1
BG_COLOR = (64, 64, 64)
CELL_PADDING = 1
BUTTON_HEIGHT = 40
BUTTON_PADDING = 0.05 * MENU_WIDTH

pg.init()

WIN = pg.display.set_mode(WINDOW_DIMS)
pg.display.set_caption('Game of Life in Pygame')


class cell:
    ACTIVE_COLOR = (215, 215, 215)
    INACTIVE_COLOR = (0, 0, 0)

    def __init__(self, coords, active=False, size=CELL_DIMS) -> None:
        self.coords = coords
        self.active = active
        self.size = size
        self.box = (
            self.coords[0] * CELL_DIMS[0] + CELL_PADDING,
            self.coords[1] * CELL_DIMS[1] + CELL_PADDING,
            CELL_DIMS[0] - 2 * CELL_PADDING,
            CELL_DIMS[1] - 2 * CELL_PADDING
        )

    def draw(self, window):
        color = self.ACTIVE_COLOR if self.active else self.INACTIVE_COLOR
        pg.draw.rect(window, color, self.box)


class button:
    COLOR = (192, 192, 192)
    BORDER_COLOR = (0, 0, 0)
    BORDER_WIDTH = 1

    def __init__(self, coords, size) -> None:
        self.coords = coords
        self.size = size

    def draw(self, window) -> None:
        pg.draw.rect(window, self.COLOR, self.coords + self.size)
        
        for i in range(4):
            border_coords = (
                self.coords[0] - i,
                self.coords[1] - i,
                self.size[0] + self.BORDER_WIDTH * 2,
                self.size[1] + self.BORDER_WIDTH * 2
            )
            pg.draw.rect(window, self.BORDER_COLOR, border_coords, 1)


class board:
    cells = [[]]
    buttons = []

    def __init__(self, size, buttons) -> None:
        for i in range(size[0]):
            temp_list = []

            for j in range(size[1]):
                temp_list.append(cell((i, j)))

            self.cells.append(temp_list)
        
        for b in buttons:
            self.buttons.append(b)

    def draw(self, window) -> None:
        for i in self.cells:
            for j in i:
                j.draw(WIN)

        for b in self.buttons:
            b.draw(WIN)


def main():
    run = True

    timer_start = time.time()
    time_per_tickrate = 1 / TICKS_PER_SEC

    WIN.fill(BG_COLOR)
    menu = [
        button(
            (WINDOW_DIMS[0] - MENU_WIDTH + BUTTON_PADDING,
             WINDOW_DIMS[1] - (BUTTON_HEIGHT + BUTTON_PADDING)),
            (MENU_WIDTH * 0.9,
             BUTTON_HEIGHT)
            )
    ]
    game_board = board(CELL_COUNT, menu)
    game_board.draw(WIN)

    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        pg.display.update()
    pg.quit()


if __name__ == '__main__':
    main()
