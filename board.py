import random

import pygame as pg

import cell
from button import button


class board:
    cells = []
    buttons = {}
    texts = {}

    def __init__(self, window, size, buttons, texts) -> None:
        self.run = False
        self.window = window

        for i in range(size[0]):
            temp_list = []

            for j in range(size[1]):
                temp_list.append(cell.cell((i, j)))

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
        for col in self.cells:
            for cell in col:

                random_bit = random.getrandbits(1)
                cell.active = True if random_bit else False

    def clear_board(self):
        for col in self.cells:
            for cell in col:
                cell.active = False

    def event_handler(self, event) -> bool:
        match event.type:

            case pg.QUIT:
                return False

            case pg.MOUSEBUTTONDOWN:
                if self.buttons['exit'].box.collidepoint(event.pos):
                    return False

                elif self.buttons['start'].box.collidepoint(event.pos):
                    self.run = True

                elif self.buttons['stop'].box.collidepoint(event.pos):
                    self.run = False

                elif self.buttons['clear'].box.collidepoint(event.pos):
                    self.clear_board()
                    
                elif self.buttons['randomize'].box.collidepoint(event.pos):
                    self.randomize_cells()

                for cols in self.cells:
                    for cell in cols:
                        if cell.box.collidepoint(event.pos):
                            cell.switch()

            case pg.MOUSEMOTION:
                on_button = False

                for key, item in self.buttons.items():
                    if item.box.collidepoint(event.pos):
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_HAND)
                        on_button = True

                if not on_button:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        return True
