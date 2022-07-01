import random
import time
from turtle import color

import numpy as np
import pygame as pg
import sympy as sp

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
pg.display.set_caption('Game of Life in Pygame')

WIN = pg.display.set_mode(WINDOW_DIMS)
TEXT_FONT = 'arial'


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

    def switch(self):
        self.active = not self.active


class button:
    COLOR = (192, 192, 192)
    BORDER_COLOR = (0, 0, 0)
    BORDER_WIDTH = 4

    def __init__(self, coords, size) -> None:
        self.coords = coords
        self.size = size
        self.rect = pg.Rect(self.coords + self.size)

    def draw(self, window) -> None:
        pg.draw.rect(window, self.COLOR, self.rect)
        for i in range(-self.BORDER_WIDTH // 2, self.BORDER_WIDTH // 2):
            border_coords = (
                self.coords[0] + i,
                self.coords[1] + i,
                self.size[0],
                self.size[1]
            )
            pg.draw.rect(window, self.BORDER_COLOR, border_coords, 1)


class text:
    def __init__(self, coords, color, content, text_size) -> None:
        self.coords = coords
        self.color = color
        self.content = content
        self.text_size = text_size
        self.font = pg.font.SysFont(TEXT_FONT, self.text_size)

    def draw(self, window):
        text = self.font.render(self.content, True, self.color)
        text_box = text.get_rect()
        text_box.center = self.coords
        window.blit(text, text_box)


class board:
    cells = []
    buttons = {}
    texts = {}

    def __init__(self, window, size, buttons, texts) -> None:
        self.window = window

        for i in range(size[0]):
            temp_list = []

            for j in range(size[1]):
                temp_list.append(cell((i, j)))

            self.cells.append(temp_list)

        self.number_of_cells = size[0] * size[1]

        for b in buttons:
            self.buttons[b] = buttons[b]

        for t in texts:
            self.texts[t] = texts[t]

    def draw(self) -> None:
        for i in self.cells:
            for j in i:
                j.draw(self.window)

        for b in self.buttons:
            self.buttons[b].draw(self.window)

        for t in self.texts:
            self.texts[t].draw(self.window)


    def randomize_cells(self):
        for col in self.cells[0]:
            for cell in col:

                random_bit = random.getrandbits(1)
                cell.active = True if random_bit else False
                cell.draw(self.window)


    def event_handler(self, event) -> bool:
        match event.type:

            case pg.QUIT:
                return False

            case pg.MOUSEBUTTONDOWN:

                if self.buttons['exit'].rect.collidepoint(event.pos):
                    return False

            case pg.MOUSEMOTION:

                if self.buttons['exit'].rect.collidepoint(event.pos):
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)

                else:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        return True


def main():
    run = True

    timer_start = time.time()
    time_per_tickrate = 1 / TICKS_PER_SEC

    WIN.fill(BG_COLOR)
    menu = {
        'exit':
        button(
            (WINDOW_DIMS[0] - MENU_WIDTH + BUTTON_PADDING,
             WINDOW_DIMS[1] - (BUTTON_HEIGHT + BUTTON_PADDING)),
            (MENU_WIDTH * 0.9, BUTTON_HEIGHT)
        ),

        'stop':
        button(
            (WINDOW_DIMS[0] - MENU_WIDTH + BUTTON_PADDING,
             WINDOW_DIMS[1] - 4 * (BUTTON_HEIGHT + BUTTON_PADDING)),
            (MENU_WIDTH * 0.9, BUTTON_HEIGHT)
        ),

        'start':
        button(
            (WINDOW_DIMS[0] - MENU_WIDTH + BUTTON_PADDING,
             WINDOW_DIMS[1] - 3 * (BUTTON_HEIGHT + BUTTON_PADDING)),
            (MENU_WIDTH * 0.9, BUTTON_HEIGHT)
        )
    }
    labels = {
        'exit':
        text(
            (WINDOW_DIMS[0] - MENU_WIDTH / 2, WINDOW_DIMS[1] -
             (BUTTON_HEIGHT / 2 + BUTTON_PADDING)),
            (0, 0, 0),
            'EXIT',
            24
        ),

        'stop':
        text(
            (WINDOW_DIMS[0] - MENU_WIDTH / 2, WINDOW_DIMS[1] - (BUTTON_HEIGHT /
             2 + BUTTON_PADDING) - 2 * (BUTTON_HEIGHT + BUTTON_PADDING)),
            (0, 0, 0),
            'STOP',
            24
        ),

        'start':
        text(
            (WINDOW_DIMS[0] - MENU_WIDTH / 2, WINDOW_DIMS[1] - (BUTTON_HEIGHT /
             2 + BUTTON_PADDING) - 3 * (BUTTON_HEIGHT + BUTTON_PADDING)),
            (0, 0, 0),
            'START',
            24
        )
    }
    game_board = board(WIN, CELL_COUNT, menu, labels)
    game_board.draw()

    while run:

        for event in pg.event.get():
            run = game_board.event_handler(event)

        time_passed = time.time() - timer_start

        if run and time_passed > time_per_tickrate:
            game_board.randomize_cells()

            timer_start = time.time()

        pg.display.update()
    pg.quit()


if __name__ == '__main__':
    main()

# git commit -m "added 'board.randomize_cells' method and fixed an error with list of cells, changed the way the window is referenced"
