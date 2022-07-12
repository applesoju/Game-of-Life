import time

import pygame as pg

import const
from board import Board
from button import Button
from input_field import InputField
from text import Text

pg.init()
pg.display.set_caption('Game of Life in Pygame')

WIN = pg.display.set_mode(const.WINDOW_DIMS)


def main():
    run = True

    timer_start = time.time()

    WIN.fill(const.BG_COLOR)
    menu = {
        'exit':
        Button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'stop':
        Button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             6 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'start':
        Button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             4 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'clear':
        Button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - 4 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'randomize':
        Button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - 6 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        ),

        'next_step':
        Button(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.WINDOW_DIMS[1] - 8 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (const.MENU_WIDTH * 0.9, const.BUTTON_HEIGHT)
        )
    }

    input_fields = {
        'tickrate':
        InputField(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH + const.BUTTON_PADDING,
             const.BUTTON_HEIGHT + const.BUTTON_PADDING),
            (const.MENU_WIDTH * 0.9, 2 * const.BUTTON_HEIGHT + const.BUTTON_PADDING),
            float
        )
    }

    labels = {
        'exit':
        Text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2,
             const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT / 2 + const.BUTTON_PADDING)),
            (0, 0, 0),
            'EXIT',
            24
        ),

        'stop':
        Text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2,
             const.BUTTON_HEIGHT / 2 + 6 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'STOP',
            24
        ),

        'start':
        Text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2,
             const.BUTTON_HEIGHT / 2 + 4 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'START',
            24
        ),

        'clear':
        Text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2,
             const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT / 2 + const.BUTTON_PADDING) - 3 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'CLEAR',
            24
        ),

        'randomize':
        Text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2,
             const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT / 2 + const.BUTTON_PADDING) - 5 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'RANDOMIZE',
            24
        ),

        'next_step':
        Text(
            (const.WINDOW_DIMS[0] - const.MENU_WIDTH / 2,
             const.WINDOW_DIMS[1] - (const.BUTTON_HEIGHT / 2 + const.BUTTON_PADDING) - 7 * (const.BUTTON_HEIGHT + const.BUTTON_PADDING)),
            (0, 0, 0),
            'NEXT STEP',
            24
        )
    }

    game_board = Board(WIN, const.CELL_COUNT, menu, labels, input_fields)
    game_board.draw()
    pg.display.update()

    while run:
        time_passed = time.time() - timer_start

        if time_passed > 1 / game_board.tickrate:

            if game_board.run:
                game_board.next_step()
                timer_start = time.time()

        game_board.draw()
        pg.display.update()

        for event in pg.event.get():
            run = game_board.event_handler(event)

    pg.quit()


if __name__ == '__main__':
    main()
