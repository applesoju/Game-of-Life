import time
from turtle import color

import numpy as np
import pygame as pg
import sympy as sp

import const
from board import board
from button import button
from text import text

pg.init()
pg.display.set_caption('Game of Life in Pygame')

WIN = pg.display.set_mode(const.WINDOW_DIMS)


def main():
    run = True

    timer_start = time.time()
    time_per_tickrate = 1 / const.TICKS_PER_SEC

    WIN.fill(const.BG_COLOR)
    menu = {
        'exit':
        button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'stop':
        button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - 7 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'start':
        button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - 8 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'clear':
        button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - 4 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        )
    }
    labels = {
        'exit':
        text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2, const.WINDOW_DIMS[1] -
             (const.BUTTON_HEIGHT / 2 + const.BUTTON_PADDING)),
            (0, 0, 0),
            'EXIT',
            24
        ),

        'stop':
        text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2, const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT /
             2 + const.BUTTON_PADDING) - 6 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'STOP',
            24
        ),

        'start':
        text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2, const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT /
             2 + const.BUTTON_PADDING) - 7 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'START',
            24
        ),

        'clear':
        text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2, const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT /
             2 + const.BUTTON_PADDING) - 3 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'CLEAR',
            24
        )
    }

    game_board = board(WIN, const.CELL_COUNT, menu, labels)
    game_board.draw()
    pg.display.update()

    while run:
        time_passed = time.time() - timer_start

        if time_passed > time_per_tickrate:

            if game_board.run:
                game_board.randomize_cells()
                timer_start = time.time()

            game_board.draw()
            pg.display.update()

        for event in pg.event.get():
            run = game_board.event_handler(event)

    pg.quit()


if __name__ == '__main__':
    main()
