import random

import pygame as pg

import cell
from button import button
from input_field import input_field


class board:
    cells = []
    buttons = {}
    texts = {}
    fields = {}

    def __init__(self, window, size, buttons, texts, fields) -> None:
        self.run = False
        self.window = window
        self.tickrate = 1

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

        for f in fields:
            self.fields[f] = fields[f]

    def draw(self) -> None:
        for i in self.cells:
            for j in i:
                j.draw(self.window)

        for b in self.buttons:
            self.buttons[b].draw(self.window)

        for t in self.texts:
            self.texts[t].draw(self.window)

        for f in self.fields:
            self.fields[f].draw(self.window)

    def randomize_cells(self) -> None:
        for col in self.cells:
            for cell in col:

                random_bit = random.getrandbits(1)
                cell.active = True if random_bit else False

    def clear_board(self) -> None:
        for col in self.cells:
            for cell in col:
                cell.active = False

    def next_step(self) -> None:
        return None
        # for col in self.cells:
        #     for cell in col:
                

    def event_handler(self, event) -> bool:
        match event.type:

            case pg.QUIT:
                return False

            case pg.KEYDOWN:
                if self.fields['tickrate'].active:

                    if event.key == pg.K_RETURN:
                        new_tickrate = self.fields['tickrate'].process_input()
                        
                        if new_tickrate is not None:
                            self.tickrate = new_tickrate

                    elif event.key == pg.K_BACKSPACE:
                        self.fields['tickrate'].delete_last_char()

                    else:
                        self.fields['tickrate'].add_char(event.unicode)

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

                if self.fields['tickrate'].box.collidepoint(event.pos):
                    self.fields['tickrate'].active = True
                else:
                    self.fields['tickrate'].active = False

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

                for key, item in self.fields.items():
                    if item.box.collidepoint(event.pos):
                        pg.mouse.set_cursor(pg.SYSTEM_CURSOR_IBEAM)
                        on_button = True

                if not on_button:
                    pg.mouse.set_cursor(pg.SYSTEM_CURSOR_ARROW)

        return True
